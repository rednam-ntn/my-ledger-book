from pathlib import Path
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, DirectoryPath, validator


class Settings(BaseSettings):
    DATA_DIR: DirectoryPath

    PORT: str

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


INPUT_PATH = Path(settings.DATA_DIR / "input")
OUTPUT_PATH = Path(settings.DATA_DIR / "output")
FACTORY_DATA_PATH = Path(settings.DATA_DIR / "factory_api")
BULK_PATH = Path(settings.DATA_DIR / "bulk")

for _path in (INPUT_PATH, OUTPUT_PATH, FACTORY_DATA_PATH, BULK_PATH):
    _path.mkdir(parents=True, exist_ok=True)
