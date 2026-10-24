from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str = "OrderHubAPI"
    debug: bool = False

    database_url: str = ""
    celery_broker_url: str = ""
    celery_result_backend: str = ""

    model_config = {
        "env_file":str(BASE_DIR / ".env"),
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

settings = Settings()
