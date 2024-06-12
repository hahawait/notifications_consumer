from dataclasses import dataclass
from functools import lru_cache

from pydantic_settings import BaseSettings as PydanticSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


class BotSettings(BaseSettings):
    NAME: str
    BOT_TOKEN: str


class ConsumerSettings(BaseSettings):
    CONSUMER_HOST: str
    CONSUMER_PORT: int
    VIRTUAL_HOST: str = '/'
    CONSUMER_USERNAME: str
    CONSUMER_PASSWORD: str
    QUEUE_NAME: str


@dataclass
class Config:
    consumer_settings: ConsumerSettings
    bot_settings: BotSettings


@lru_cache
def get_config():
    return Config(
        consumer_settings=ConsumerSettings(),
        bot_settings=BotSettings()
    )
