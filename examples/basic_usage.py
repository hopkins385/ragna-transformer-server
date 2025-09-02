#!/usr/bin/env python3
"""
Example usage of the Ragna Transformer Server NER API.

This script demonstrates how to interact with the NER service
to extract and mask sensitive information from text.
"""

import requests
import json
import sys
from typing import Dict, Any

# Default server URL
SERVER_URL = "http://localhost:3030"


def extract_entities(text: str, labels: list = None, server_url: str = SERVER_URL) -> Dict[str, Any]:
    """
    Extract named entities from text using the NER API.
    
    Args:
        text: The input text to process
        labels: Optional list of entity labels to extract
        server_url: The server URL (default: localhost:3030)
    
    Returns:
        Dictionary containing masked_text and entities
    """
    endpoint = f"{server_url}/ner/extract"
    
    payload = {"text": text}
    if labels:
        payload["labels"] = labels
    
    try:
        response = requests.post(
            endpoint,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error calling NER API: {e}")
        return None


def main():
    """Run example NER extractions."""
    
    # Example 1: Basic usage with default labels
    print("🔍 Example 1: Basic NER with default labels")
    print("=" * 50)
    
    sample_text = """
    John Doe works at Acme Corporation in New York. 
    His email is john.doe@acme.com and his phone number is +1-555-123-4567.
    His birth date is 1985-03-15 and his IBAN is GB29 NWBK 6016 1331 9268 19.
    """
    
    result = extract_entities(sample_text)
    if result:
        print(f"Original text: {sample_text.strip()}")
        print(f"\nMasked text: {result['masked_text']}")
        print(f"\nFound {len(result['entities'])} entities:")
        for entity in result['entities']:
            print(f"  - {entity['text']} → {entity['label']} (confidence: {entity['score']:.2f})")
    
    print("\n" + "=" * 70 + "\n")
    
    # Example 2: Custom labels
    print("🎯 Example 2: Custom entity labels")
    print("=" * 50)
    
    custom_text = "Apple Inc. was founded by Steve Jobs in Cupertino, California."
    custom_labels = ["person", "organization", "location"]
    
    result = extract_entities(custom_text, labels=custom_labels)
    if result:
        print(f"Original text: {custom_text}")
        print(f"Custom labels: {custom_labels}")
        print(f"\nMasked text: {result['masked_text']}")
        print(f"\nFound {len(result['entities'])} entities:")
        for entity in result['entities']:
            print(f"  - {entity['text']} → {entity['label']} (confidence: {entity['score']:.2f})")
    
    print("\n" + "=" * 70 + "\n")
    
    # Example 3: Privacy-focused text
    print("🔒 Example 3: Privacy-sensitive content")
    print("=" * 50)
    
    privacy_text = """
    Contact Sarah Williams at sarah@company.com or visit https://company.com.
    Her office address is 123 Main Street, Boston, MA 02101.
    Customer ID: CU-2024-001, Phone: (555) 987-6543
    """
    
    result = extract_entities(privacy_text)
    if result:
        print(f"Original text: {privacy_text.strip()}")
        print(f"\nMasked text: {result['masked_text']}")
        print(f"\nEntities that would be masked:")
        for entity in result['entities']:
            print(f"  - {entity['text']} → {entity['label']} (confidence: {entity['score']:.2f})")


def test_server_connection(server_url: str = SERVER_URL) -> bool:
    """Test if the server is running and accessible."""
    try:
        response = requests.get(f"{server_url}/docs", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


if __name__ == "__main__":
    print("🚀 Ragna Transformer Server - NER API Examples")
    print("=" * 60)
    
    # Check if server is running
    if not test_server_connection():
        print("❌ Server not accessible at http://localhost:3030")
        print("\nTo start the server:")
        print("  Docker: docker run -p 3030:3030 ghcr.io/hopkins385/ragna-transformer-server:latest")
        print("  Local:  uv run app/main.py")
        sys.exit(1)
    
    print("✅ Server is running at http://localhost:3030")
    print()
    
    try:
        main()
        print("🎉 Examples completed successfully!")
        print("\nTry modifying the text samples above or create your own!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        sys.exit(1)