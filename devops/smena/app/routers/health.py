# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
def healthcheck():
    """healthcheck для проверки работоспособности сервиса"""
    return {"success": True}
