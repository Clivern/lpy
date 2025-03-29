# 372. pydantic-settings
#
# BaseSettings reads env vars. model_config can set env_prefix. Nested env uses __ in v2.
# Keep secrets out of git and in the environment.
#
# Run: python 372_pydantic_settings/main.py

from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LEARN_")
    debug: bool = False
s = Settings(_env_file=None)
print(s.debug, Settings(debug=True).debug)
