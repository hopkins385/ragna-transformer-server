---
name: Bug Report
about: Create a report to help us improve
title: "[BUG] "
labels: bug
assignees: ""
---

## Bug Description

A clear and concise description of what the bug is.

## Steps to Reproduce

1. Send request to '...'
2. With payload '....'
3. See error

## Expected Behavior

A clear and concise description of what you expected to happen.

## Actual Behavior

A clear and concise description of what actually happened.

## Environment

- OS: [e.g. macOS, Ubuntu 20.04]
- Python version: [e.g. 3.13.0]
- Server version: [e.g. 0.1.0]
- Deployment method: [e.g. Docker, local development]

## Request/Response Examples

```bash
# Request
curl -X POST "http://localhost:3030/ner/extract" \
     -H "Content-Type: application/json" \
     -d '{"text": "example text"}'

# Response (if any)
```

## Logs

```
Paste relevant log output here
```

## Additional Context

Add any other context about the problem here, such as:

- Does this happen consistently or intermittently?
- Any recent changes to your setup?
- Screenshots (if applicable)
