# 🤖 ChatGPT Clone

> An intelligent AI-powered chatbot with persistent memory, weather intelligence, and seamless user experience.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)

## ✨ Features

🔐 **Secure Authentication** - User registration and login system  
🧠 **Contextual Memory** - Remembers conversation history across sessions  
💬 **Real-time Chat** - Powered by OpenAI's GPT-3.5-Turbo  
🌦️ **Weather Intelligence** - Get weather updates for any city  
📊 **Persistent Storage** - Chat history stored in PostgreSQL  
🎨 **Modern UI** - Clean, responsive Streamlit interface  

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **AI Engine** | OpenAI GPT-3.5-Turbo |
| **Database** | PostgreSQL + SQLAlchemy ORM |
| **Authentication** | Custom token-based auth |
| **Weather API** | OpenWeatherMap |

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:
- 🐍 Python 3.8 or higher
- 🐘 PostgreSQL (13+)
- 🔑 OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- 🌤️ OpenWeatherMap API key ([Get one here](https://openweathermap.org/api))

### 1️⃣ Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/chatgpt-clone.git
cd chatgpt-clone

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Database Configuration

```sql
-- Connect to PostgreSQL and create database
CREATE DATABASE Chatgpt;

-- Optional: Create dedicated user
CREATE USER [your_name] WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE Chatgpt TO [your_name];
```

### 3️⃣ Environment Setup

Create a `.env` file in the root directory:

```env
# API Keys
OPENAI_API_KEY=sk-your-openai-api-key-here
WEATHER_API_KEY=your-openweather-api-key-here

# Database
DATABASE_URL=postgresql://username:password@localhost:5432/Chatgpt

# Optional: App Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### 4️⃣ Initialize Database

```bash
# Run database migrations
alembic upgrade head
```

### 5️⃣ Launch Application

**Terminal 1 - Backend:**
```bash
cd app
uvicorn main:app --reload
```
🌐 Backend API: http://127.0.0.1:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
streamlit run streamlit_app.py
```
🎨 Frontend UI: http://localhost:8501

## 📖 Usage

1. **Register/Login** - Create your account or sign in
2. **Start Chatting** - Ask questions, get AI responses
3. **Weather Queries** - Type "weather in [city]" for weather info
4. **View History** - Access your previous conversations
5. **Continue Sessions** - Pick up where you left off

## 🔧 Development

### Database Migrations

When you modify database models:

```bash
# Generate new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migration
alembic upgrade head
```

## 🆘 Troubleshooting

**Database Connection Issues:**
- Ensure PostgreSQL is running
- Check DATABASE_URL format
- Verify user permissions

**API Key Errors:**
- Validate OpenAI API key format
- Check API usage limits
- Ensure .env file is properly loaded

**Port Conflicts:**
- FastAPI: Change port with `--port 8001`
- Streamlit: Change port with `--server.port 8502`

## 📧 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Create a new issue with detailed information

---

<div align="center">
  Made by Advay Parab
</div>
