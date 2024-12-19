import os

def create_utils_structure(base_path="app/utils"):
    # Define the utils files and their example content
    utils_files = {
        "file_utils.py": '''# Utility functions for file operations

def read_file(file_path):
    """Reads the contents of a file."""
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)
''',

        "api_utils.py": '''# Utility functions for API-related tasks

def validate_api_key(api_key):
    """Validates that an API key is present."""
    if not api_key:
        raise ValueError("API key is missing")
    return True
''',

        "db_utils.py": '''# Utility functions for database operations

def get_user_by_id(db_session, user_id):
    """Fetches a user from the database by their ID."""
    return db_session.query(User).filter(User.id == user_id).first()

def add_user(db_session, user):
    """Adds a new user to the database."""
    db_session.add(user)
    db_session.commit()
''',

        "string_utils.py": '''# Utility functions for string manipulation

def capitalize_words(text):
    """Capitalizes the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())

def is_palindrome(text):
    """Checks if a string is a palindrome."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
''',

        "general_utils.py": '''# General-purpose utility functions

import datetime

def get_current_timestamp():
    """Returns the current timestamp."""
    return datetime.datetime.now().isoformat()

def calculate_percentage(part, whole):
    """Calculates the percentage of a part out of a whole."""
    return (part / whole) * 100 if whole != 0 else 0
'''
    }

    # Create the utils directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    # Create each file with its content
    for file_name, content in utils_files.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'w') as f:
            f.write(content)

    print(f"Utils structure created under {base_path}")

if __name__ == "__main__":
    create_utils_structure()
