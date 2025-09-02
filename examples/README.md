# Example Usage

This directory contains example scripts and usage patterns for the Ragna Transformer Server.

## Available Examples

### `basic_usage.py`

A comprehensive Python script demonstrating:

- Basic NER extraction with default labels
- Custom entity label specification
- Privacy-focused text processing
- Error handling and server connectivity testing

**Prerequisites:**

- `requests` library: `pip install requests`
- Running server instance

**Usage:**

```bash
# Make sure the server is running first
python examples/basic_usage.py
```

## Quick cURL Examples

### Basic Entity Extraction

```bash
curl -X POST "http://localhost:3030/ner/extract" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "John Doe works at Acme Corp. Email: john@acme.com"
     }'
```

### Custom Labels

```bash
curl -X POST "http://localhost:3030/ner/extract" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Apple Inc. was founded by Steve Jobs in California",
       "labels": ["person", "organization", "location"]
     }'
```

### Privacy-Sensitive Content

```bash
curl -X POST "http://localhost:3030/ner/extract" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Contact Sarah at sarah@company.com or call +1-555-123-4567. Address: 123 Main St, Boston MA"
     }'
```

## Integration Examples

### Python with requests

```python
import requests

def extract_entities(text, labels=None):
    response = requests.post(
        "http://localhost:3030/ner/extract",
        json={"text": text, "labels": labels}
    )
    return response.json()

# Usage
result = extract_entities("John works at Acme Corp")
print(result["masked_text"])
```

### JavaScript/Node.js

```javascript
const fetch = require("node-fetch");

async function extractEntities(text, labels = null) {
  const response = await fetch("http://localhost:3030/ner/extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, labels }),
  });
  return response.json();
}

// Usage
extractEntities("John works at Acme Corp").then((result) =>
  console.log(result.masked_text)
);
```

## Common Use Cases

1. **Document Sanitization**: Remove PII before storing documents
2. **Email Privacy**: Mask sensitive info in customer communications
3. **Log Processing**: Clean logs before analysis
4. **Data Anonymization**: Prepare datasets for sharing
5. **Compliance**: GDPR/CCPA data protection
