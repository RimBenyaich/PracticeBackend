from pydantic import BaseSettings


class _Settings(BaseSettings):
    SERVICE_ENDPOINT: str = "/repositories"


settings = _Settings()
