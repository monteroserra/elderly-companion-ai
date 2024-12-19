# General-purpose utility functions

import datetime

def get_current_timestamp():
    """Returns the current timestamp."""
    return datetime.datetime.now().isoformat()

def calculate_percentage(part, whole):
    """Calculates the percentage of a part out of a whole."""
    return (part / whole) * 100 if whole != 0 else 0
