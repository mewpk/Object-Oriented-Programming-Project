from typing import Dict

class Settings:
    def __init__(self, config: Dict):
        self.config = config

    def __getitem__(self, key):
        return self.config[key]

    def __getattr__(self, key):
        return self.config[key]

config = {
    "app_name": "My App",
    "log_level": "debug",
    "api_key": "1234567890",
    "api_host" : "0.0.0.0",
    "api_port" : 8000
}

settings = Settings(config)
