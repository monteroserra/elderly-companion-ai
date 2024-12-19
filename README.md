# Elderly Companion AI

Elderly Companion AI is a proof-of-concept (PoC) application designed to support and provide companionship to elderly individuals. It leverages AI-powered conversations, reminders, and activity recommendations to create an intelligent, user-friendly system tailored to individual preferences.

---

## Features

### 1. **Morning and Evening Check-ins**
   - AI-powered friendly conversations to start and end the day positively.
   - Text-to-Speech (TTS) capabilities to deliver messages in a soothing voice.

### 2. **Reminders System**
   - Manage and notify users of important appointments, medication schedules, and general activities.

### 3. **Activity Recommender**
   - Suggests nearby activities and events based on user preferences.
   - Utilizes Google Maps API and web scraping for localized recommendations.

### 4. **Avatar Integration**
   - Simple avatar interface to provide a friendly, interactive user experience.

---

## Technologies Used

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/): For building a lightweight, high-performance API.
  - [SQLAlchemy](https://www.sqlalchemy.org/): Database management with SQLite.
- **AI and APIs**:
  - [OpenAI API](https://openai.com/): For natural language processing and LLM-based conversations.
  - [Google Maps API](https://developers.google.com/maps): For location-based activity recommendations.
  - [gTTS](https://pypi.org/project/gTTS/): For converting text to speech.
- **Frontend**:
  - Static files and basic templates (HTML/CSS) integrated with FastAPI.
- **Deployment**:
  - [Heroku](https://www.heroku.com/): To host the application.

---
## Project Structure

```plaintext
elderly-companion-ai/
├── notebooks/                  # Jupyter notebooks for experimentation
├── app/
│   ├── main.py                 # Entry point of the app
│   ├── api/                    # API routes (e.g., reminders, checks)
│   │   ├── endpoints.py        # Define API endpoints
│   │   └── utils.py            # API helper functions
│   ├── core/                   # App configurations and dependencies
│   │   ├── config.py           # Configuration settings
│   │   └── dependencies.py     # Dependency injection setup
│   ├── models/                 # Database models
│   │   └── user.py             # User database model
│   ├── services/               # Functional services (TTS, reminders, etc.)
│   │   ├── tts.py              # Text-to-Speech service
│   │   ├── reminders.py        # Reminder logic
│   │   └── recommender.py      # Activity recommender logic
│   ├── static/                 # Static files (avatars, etc.)
│   └── templates/              # HTML templates (if needed)
├── database/                   # Database initialization and files
│   ├── db.sqlite               # SQLite database
│   └── init_db.py              # Initialize the database
├── tests/                      # Unit and integration tests
├── pyproject.toml              # Poetry configuration
├── requirements.txt            # Dependencies (optional for Heroku)
├── Procfile                    # Heroku deployment file
├── runtime.txt                 # Python version for Heroku
├── README.md                   # Project overview
├── .gitignore                  # Ignored files

```

## Installation and Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/elderly-companion-ai.git
cd elderly-companion-ai

