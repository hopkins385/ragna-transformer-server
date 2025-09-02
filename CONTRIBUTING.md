# Contributing to Ragna Transformer Server

Thank you for your interest in contributing to Ragna Transformer Server! We welcome contributions from the community.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ragna-transformer-server.git
   cd ragna-transformer-server
   ```
3. **Set up the development environment**:

   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install dependencies
   uv sync --all-extras
   ```

## Development Workflow

1. **Create a new branch** for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards (see below)

3. **Test your changes**:

   ```bash
   # Run the server locally
   uv run app/main.py

   # Test the API endpoints
   curl -X POST "http://localhost:3030/ner/extract" \
        -H "Content-Type: application/json" \
        -d '{"text": "John Doe works at Acme Corp"}'
   ```

4. **Commit your changes**:

   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork** and **create a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Coding Standards

### Python Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and single-purpose

### API Design

- Follow RESTful conventions
- Use appropriate HTTP status codes
- Include proper error handling and logging
- Validate input data with Pydantic models

### Testing

- Write tests for new features
- Ensure existing tests pass
- Include both unit and integration tests
- Test error conditions and edge cases

## Project Structure

```
app/
├── main.py              # FastAPI app setup and configuration
├── routers/             # API route handlers
│   ├── __init__.py
│   └── ner.py          # NER-specific endpoints
└── utils/               # Utility functions
    ├── __init__.py
    └── hide.py         # Text preprocessing utilities
```

## Types of Contributions

### 🐛 Bug Reports

- Use GitHub Issues with the "bug" label
- Include steps to reproduce
- Provide environment details (Python version, OS, etc.)
- Include relevant logs or error messages

### 💡 Feature Requests

- Use GitHub Issues with the "enhancement" label
- Describe the problem the feature would solve
- Provide examples of how it would be used
- Consider implementation complexity

### 🔧 Code Contributions

- **Bug fixes**: Focus on minimal changes that fix the issue
- **New features**: Discuss in an issue first for larger features
- **Performance improvements**: Include benchmarks showing improvement
- **Documentation**: Improve README, add code comments, etc.

### 📚 Documentation

- Improve API documentation
- Add usage examples
- Fix typos or unclear explanations
- Translate documentation (if applicable)

## Specific Areas We'd Love Help With

1. **Testing Framework**: Setting up comprehensive test suite
2. **Performance Optimization**: Model caching, request batching
3. **Additional Privacy Features**: More text preprocessing options
4. **API Extensions**: Bulk processing, streaming responses
5. **Documentation**: More usage examples, tutorials
6. **Monitoring**: Health checks, metrics endpoints

## Code Review Process

1. All submissions require review before merging
2. We aim to review PRs within 48 hours
3. Address reviewer feedback promptly
4. Maintain a clean git history (squash commits if needed)

## Release Process

- We use semantic versioning (MAJOR.MINOR.PATCH)
- Releases are tagged and published to GitHub
- Docker images are automatically built and published

## Getting Help

- 💬 [GitHub Discussions](https://github.com/hopkins385/ragna-transformer-server/discussions) for questions
- 🐛 [GitHub Issues](https://github.com/hopkins385/ragna-transformer-server/issues) for bugs
- 📧 Contact maintainers for security issues

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🚀
