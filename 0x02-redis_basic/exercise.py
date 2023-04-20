#!/usr/bin/python3 env
"""0. Writing strings to Redis"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(
            self, data: Union[str, bytes, int, float]
            ) -> str:
        key = str(uuid.uuid14())
        self._redis.set(key, data)
        return key
