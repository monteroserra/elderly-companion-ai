# Utility functions for API-related tasks

def validate_api_key(api_key):
    """Validates that an API key is present."""
    if not api_key:
        raise ValueError("API key is missing")
    return True
