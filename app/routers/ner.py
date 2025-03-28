from gliner import GLiNER
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class NerRequestBody(BaseModel):
    text: str
    labels: list | None = None

model_name = "urchade/gliner_multi-v2.1"
model_cache_dir = "./cache"
model = GLiNER.from_pretrained(model_name, cache_dir=model_cache_dir)

# function that iterates over the entities and replaces them with *** in the text
def mask_entities(text: str, entities):
    for entity in entities:
        text = text.replace(entity["text"], "<" + entity["label"] + ">")
    return text

@router.post("/ner/predict")
async def ner(body: NerRequestBody):
    default_labels = ["person", "birthdate", "phone", "iban", "email", "name", "date", "address", "organization", "medical_term"]
    
    if body.labels is None:
        labels = default_labels
    else:
        labels = body.labels

    entities = model.predict_entities(text=body.text, labels=labels)
    
    # Post-process entities
    filtered_entities = []
    for entity in entities:
        # Only include entities with confidence score > 0.7
        if entity["score"] < 0.7:
            continue
            
        # # Additional validation for IBANs
        # if entity["label"] == "iban":
        #     if not is_valid_iban(entity["text"]):
        #         continue
                
        filtered_entities.append(entity)

    masked_text = mask_entities(text=body.text, entities=filtered_entities)

    return {
        "masked_text": masked_text,
        "entities": filtered_entities
    }