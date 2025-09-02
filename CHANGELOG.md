# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Comprehensive documentation and examples
- GitHub issue templates
- CI/CD workflow with GitHub Actions
- Security policy and contributing guidelines

## [0.1.0] - 2025-09-02

### Added

- Initial release of Ragna Transformer Server
- FastAPI-based NER service using GLiNER multi-v2.1 model
- `/ner/extract` endpoint for named entity recognition
- Support for custom entity labels
- Automatic email, URL, and phone number masking
- Docker support with multi-stage builds
- CORS middleware for web application integration
- Comprehensive logging and error handling
- Model caching for improved performance
- Confidence threshold filtering (>0.7)

### Features

- **Default Entity Types**: person, birthdate, phonenumber, iban, address, organization, location
- **Privacy Protection**: Automatic masking of sensitive information
- **High Performance**: GLiNER model with state-of-the-art accuracy
- **Production Ready**: Docker deployment with proper logging
- **Developer Friendly**: FastAPI with automatic OpenAPI documentation

### Technical Details

- Python 3.13+ support
- UV package manager integration
- FastAPI with Pydantic validation
- GLiNER transformer model
- Docker multi-stage builds
- Model persistence in cache directory

---

## Legend

- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes
