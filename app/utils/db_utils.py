# Utility functions for database operations

def get_user_by_id(db_session, user_id):
    """Fetches a user from the database by their ID."""
    return db_session.query(User).filter(User.id == user_id).first()

def add_user(db_session, user):
    """Adds a new user to the database."""
    db_session.add(user)
    db_session.commit()
