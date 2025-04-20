from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_HOST: str

    GOQ_API_KEY: str = Field(default="your_groq_api_key")
    GROQ_MODEL: str = Field(default="llama3-8b-8192")
    GROQ_API_URL: str = Field(default="https://api.groq.com/openai/v1/chat/completions")

    class Config:
        env_file = ".env"

settings = Settings()

