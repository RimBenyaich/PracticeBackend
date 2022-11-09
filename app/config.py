from pydantic import BaseSettings


class _Settings(BaseSettings):
    SERVICE_ENDPOINT: str = "/repositories"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = _Settings()
