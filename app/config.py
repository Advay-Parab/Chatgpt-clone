from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str
    OPENWEATHER_API_KEY: str

    class Config:
        env_file = ".env"

# 🔥 Create the instance so it can be imported across the project
settings = Settings()






