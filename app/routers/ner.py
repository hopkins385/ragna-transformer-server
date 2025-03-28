from gliner import GLiNER
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class NerRequestBody(BaseModel):
    text: str
    labels: list | None = None

model = GLiNER.from_pretrained("urchade/gliner_multi-v2.1")

# function that iterates over the entities and replaces them with *** in the text
def mask_entities(text: str, entities):
    for entity in entities:
        text = text.replace(entity["text"], "***")
    return text

@router.post("/ner/predict")
async def ner(body: NerRequestBody):
    default_labels = ["person", "birthdate", "phone", "iban", "email", "name", "date", "address", "organization", "medical_term"]
    
    if body.labels is None:
        labels = default_labels
    else:
        labels = body.labels

    entities = model.predict_entities(text=body.text, labels=labels)
    masked_text = mask_entities(text=body.text, entities=entities)

    return {
        "masked_text": masked_text,
        "entities": entities
    }