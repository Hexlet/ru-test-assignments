# -*- coding: utf-8 -*-
from fastapi import APIRouter
from . import health


api_router = APIRouter()

api_router.include_router(health.router)
