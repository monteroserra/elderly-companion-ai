# Utility functions for file operations

def read_file(file_path):
    """Reads the contents of a file."""
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)
