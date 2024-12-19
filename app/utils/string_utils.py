# Utility functions for string manipulation

def capitalize_words(text):
    """Capitalizes the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())

