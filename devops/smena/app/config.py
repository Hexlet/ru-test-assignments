# -*- coding: utf-8 -*-
from starlette.config import Config


config = Config(".env")

# Environment
ENVIRONMENT = config("ENVIRONMENT")

# Secret
ENVIRONMENT_FROM_SECRET = config("ENVIRONMENT_FROM_SECRET")
