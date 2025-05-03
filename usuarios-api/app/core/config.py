from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
print("DATABASE_URL:", settings.database_url)  # Adicione isso temporariamente