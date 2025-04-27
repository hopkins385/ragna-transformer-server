from gliner import GLiNER
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import os
import logging
import sys

from utils.hide import hide_emails

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Ensure logs go to stdout for container visibility
)
logger = logging.getLogger(__name__)

router = APIRouter()

class NerRequestBody(BaseModel):
    text: str
    labels: list | None = None

cwd = os.getcwd()
model_name = "urchade/gliner_multi-v2.1"
model_cache_dir = os.path.join(cwd, "cache")

try:
    model = GLiNER.from_pretrained(model_name, cache_dir=model_cache_dir, local_files_only=False)
    logger.info(f"Model loaded successfully from {model_cache_dir}")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    raise RuntimeError(f"Failed to load NER model: {str(e)}")

def mask_entities(text: str, entities):
    for entity in entities:
        text = text.replace(entity["text"], "<" + entity["label"] + ">")
    return text

@router.post("/ner/extract")
async def ner(body: NerRequestBody):
    try:
        default_labels = ["person", "birthdate", "phonenumber", "iban", "address", "organization", "location"]

        if body.labels is None:
            labels = default_labels
        else:
            labels = body.labels

        # Pre-process text
        # Hide sensitive information
        body.text = hide_emails(body.text)

        try:
            entities = model.predict_entities(text=body.text, labels=labels)
        except Exception as e:
            logger.error(f"Model prediction failed: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Model prediction failed: {str(e)}")

        # Post-process entities
        filtered_entities = []
        for entity in entities:
            # Only include entities with confidence score > 0.7
            if entity["score"] < 0.7:
                continue

            filtered_entities.append(entity)

        masked_text = mask_entities(text=body.text, entities=filtered_entities)

        return {
            "masked_text": masked_text,
            "entities": filtered_entities
        }
    except Exception as e:
        logger.error(f"Unexpected error in NER processing: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")