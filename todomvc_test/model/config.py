from typing import Optional

import pydantic


class Settings(pydantic.BaseSettings):
    browser_name: str = 'chrome'
    browser_quit_after_each_test: bool = False
    headless: bool = True
    remote_url: Optional[pydantic.AnyHttpUrl] = None
    remote_enableVNC: bool = False


settings = Settings(_env_file='config.env')

