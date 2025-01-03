from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert
from slugify import slugify


router = APIRouter(prefix='/', tags=['stocks'])


@router.get('')
async def get_all_coins():
    pass