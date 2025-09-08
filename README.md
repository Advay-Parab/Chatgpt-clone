# ChatGPT Clone Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)

A conversational AI application built with modern web technologies, featuring intelligent chat responses and weather information services.

## Overview

This project implements a full-stack chatbot application that leverages OpenAI's language models to provide human-like conversations. The system includes user management, persistent chat storage, and integrated weather services.

## Core Capabilities

The application provides several key functionalities:
- User authentication system with secure registration and login
- Intelligent conversation handling using OpenAI's GPT models
- Weather information retrieval for global cities
- Conversation history persistence across user sessions
- Real-time chat interface with responsive design

## Technology Implementation

**Backend Architecture**
- FastAPI framework for REST API development
- SQLAlchemy ORM for database operations
- PostgreSQL for data persistence
- Alembic for database schema management

**Frontend Development**  
- Streamlit framework for user interface
- Interactive chat components
- Real-time response handling

**External Services**
- OpenAI API for natural language processing
- OpenWeatherMap API for meteorological data

## System Requirements

Before installation, ensure your development environment includes:
- Python version 3.8 or newer
- PostgreSQL database server (version 13 recommended)
- Active internet connection for API services
- Git version control system

## API Credentials Setup

You will need to obtain API keys from the following services:
1. OpenAI Platform - Register at https://platform.openai.com for GPT access
2. OpenWeatherMap - Create account at https://openweathermap.org for weather data

## Installation Process

### Repository Setup
```bash
git clone <your-repository-url>
cd <project-directory>
```

### Python Environment Configuration
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate  # Linux/Mac
chatbot_env\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Database Initialization
Access your PostgreSQL instance and execute:
```sql
CREATE DATABASE chatbot_db;
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT ALL ON DATABASE chatbot_db TO app_user;
```

### Environment Configuration
Create `.env` file with your credentials:
```
OPENAI_API_KEY=<your-openai-key>
WEATHER_API_KEY=<your-weather-key>
DATABASE_URL=postgresql://app_user:secure_password@localhost:5432/chatbot_db
```

### Database Schema Setup
```bash
alembic upgrade head
```

## Running the Application

### Start Backend Service
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Launch Frontend Interface  
```bash
streamlit run streamlit_app.py --server.port 8501
```

Access the application at http://localhost:8501

## Application Usage

### Getting Started
1. Navigate to the application URL
2. Create a new user account or sign in
3. Begin conversation by typing in the message field
4. Select conversation topics using the dropdown menu

### Weather Queries
For weather information:
- Set topic to "weather" 
- Enter city name in message field
- Receive current weather conditions

### Conversation Management
- All conversations are automatically saved
- Previous chats can be continued in new sessions
- Context is maintained across message exchanges

## Development Guidelines

### Adding New Features
When extending functionality:
```bash
alembic revision --autogenerate -m "feature description"
alembic upgrade head
```

### Code Organization
- Models: Database table definitions
- Routes: API endpoint implementations  
- Services: External API integrations
- Schemas: Data validation structures

## Troubleshooting Guide

**Database Issues**
- Verify PostgreSQL service is running
- Check connection string format
- Confirm user permissions are correct

**API Problems**
- Validate API key formats and activation
- Monitor usage quotas and limits
- Check network connectivity

**Port Conflicts**
- Modify FastAPI port: `uvicorn main:app --port 8001`
- Change Streamlit port: `streamlit run app.py --server.port 8502`

## Project Architecture

The application follows a layered architecture pattern:
- Presentation Layer: Streamlit UI components
- API Layer: FastAPI route handlers
- Business Logic: Service implementations
- Data Layer: SQLAlchemy models and PostgreSQL

## Contributing

To contribute to this project:
1. Fork the repository
2. Create feature branch from main
3. Implement changes with tests
4. Submit pull request with description

## Support and Contact

For technical support or questions:
- Review troubleshooting section
- Check existing issues in repository
- Create new issue with detailed problem description

---

**Project maintained by Advay Parab**  
Last updated: $(date +%Y-%m-%d)
