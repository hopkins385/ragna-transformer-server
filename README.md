# RAGNA Studio - NER Server

A FastAPI-based Named Entity Recognition (NER) service powered by GLiNER, designed to extract and mask sensitive information from text.

## Features

- **Named Entity Recognition**: Extract entities like persons, organizations, locations, phone numbers, IBANs, addresses, and birthdates
- **Privacy Protection**: Automatically mask sensitive information including emails, URLs, and detected entities
- **Flexible Labels**: Support for custom entity labels or use default comprehensive set
- **High Accuracy**: Uses GLiNER multi-v2.1 model with configurable confidence thresholds
- **Production Ready**: Dockerized with proper logging and error handling
- **CORS Enabled**: Ready for web application integration

## Quick Start

### Using Docker (Recommended)

```bash
# Pull and run the latest image
docker run -p 3030:3030 ghcr.io/hopkins385/ragna-transformer-server:latest
```

### Local Development

1. **Prerequisites**

   - Python 3.13+
   - [uv](https://docs.astral.sh/uv/) package manager

2. **Installation**

   ```bash
   git clone https://github.com/hopkins385/ragna-transformer-server.git
   cd ragna-transformer-server
   uv sync
   ```

3. **Run the server**
   ```bash
   uv run app/main.py
   ```

The server will start on `http://localhost:3030`

## API Usage

### Extract Named Entities

**POST** `/ner/extract`

Extract and mask named entities from text.

#### Request Body

```json
{
  "text": "John Doe works at Acme Corp. His email is john@acme.com and phone is +1-555-0123.",
  "labels": ["person", "organization", "email", "phonenumber"] // Optional
}
```

#### Response

```json
{
  "masked_text": "John Doe works at <organization>. His email is <email> and phone is +1-555-0123.",
  "entities": [
    {
      "text": "John Doe",
      "label": "person",
      "score": 0.95,
      "start": 0,
      "end": 8
    },
    {
      "text": "Acme Corp",
      "label": "organization",
      "score": 0.89,
      "start": 18,
      "end": 27
    }
  ]
}
```

### Default Entity Labels

When no labels are specified, the service uses these default categories:

- `person` - Names of individuals
- `birthdate` - Birth dates
- `phonenumber` - Phone numbers
- `iban` - International Bank Account Numbers
- `address` - Physical addresses
- `organization` - Company/organization names
- `location` - Geographic locations

## Configuration

### Environment Variables

- **Model Caching**: Models are cached in `./cache` directory by default
- **Confidence Threshold**: Entities with confidence < 0.7 are filtered out
- **Port**: Server runs on port 3030 (configurable in Docker)

### Privacy Features

The service automatically preprocesses text to hide:

- Email addresses → `<email>`
- URLs → `<url>`
- Phone numbers → `<phone>`

## Docker Deployment

### Build from Source

```bash
docker build -t ragna-transformer-server .
docker run -p 3030:3030 ragna-transformer-server
```

### Docker Compose

```bash
docker-compose up
```

## Development

### Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── routers/
│   └── ner.py          # NER endpoint implementation
└── utils/
    └── hide.py         # Text privacy utilities

cache/                   # Model cache directory
docker-compose.yml      # Development compose file
Dockerfile             # Production container
pyproject.toml         # Python dependencies
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Local Testing

```bash
# Install dependencies
uv sync

# Run tests (when available)
uv run pytest

# Run the server
uv run app/main.py
```

## Model Information

This service uses the [GLiNER multi-v2.1](https://huggingface.co/urchade/gliner_multi-v2.1) model:

- **Size**: ~500MB
- **Languages**: Multilingual support
- **Performance**: State-of-the-art NER accuracy
- **License**: MIT

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [GLiNER](https://github.com/urchade/GLiNER) for the excellent NER model
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

## Support

- 🐛 [Report Bug](https://github.com/hopkins385/ragna-transformer-server/issues)
- 💡 [Request Feature](https://github.com/hopkins385/ragna-transformer-server/issues)
- 💬 [Discussions](https://github.com/hopkins385/ragna-transformer-server/discussions)

---

**Note**: This server is designed to work as part of the RAGNA Studio ecosystem but can be used independently for any NER tasks.
