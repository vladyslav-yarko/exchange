from abc import ABC, abstractmethod
from typing import Union, Optional
import uuid
from functools import wraps

from sqlalchemy import func, select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base import Base
from src.utils.logger import logger


class Repository(ABC):
    
    @abstractmethod
    async def get():
        raise NotImplementedError
    
    @abstractmethod
    async def get_one():
        raise NotImplementedError
    
    @abstractmethod
    async def get_count():
        raise NotImplementedError
    
    @abstractmethod
    async def create_one():
        raise NotImplementedError
    
    @abstractmethod
    async def update_one():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one():
        raise NotImplementedError
