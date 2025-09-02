# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Ragna Transformer Server seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please send an email to: **[your-email@domain.com]** (replace with your actual contact)

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

### What to Include

Please include the following information along with your report:

- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

### Security Considerations for NER Service

This service processes text that may contain sensitive information. Key security areas include:

1. **Input Validation**: Maliciously crafted text inputs
2. **Model Security**: Attacks against the GLiNER model
3. **Data Exposure**: Logs or errors that might leak sensitive data
4. **Resource Exhaustion**: Large inputs causing DoS
5. **Container Security**: Docker container vulnerabilities

### Preferred Languages

We prefer all communications to be in English.

## Policy

We follow the principle of responsible disclosure and will work with security researchers to:

1. Acknowledge receipt of your vulnerability report
2. Provide an estimated timeline for addressing the vulnerability
3. Notify you when the vulnerability has been fixed
4. Credit you for the discovery (if desired)

## Bug Bounty

Currently, we do not have a bug bounty program, but we deeply appreciate security research and responsible disclosure.

## Security Updates

Security updates will be released as patch versions and announced through:

- GitHub Security Advisories
- Release notes
- This repository's README.md

## Safe Harbor

We support safe harbor for security researchers who:

- Make a good faith effort to avoid privacy violations and data destruction
- Only interact with accounts you own or with explicit permission
- Do not access or modify others' data
- Contact us before sharing vulnerability details with others
