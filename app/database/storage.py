from config import STORAGE_API_TOKEN
import requests
import time


class Storage:
    basic_headers = {"Authorization": f"Bearer {STORAGE_API_TOKEN}"}
    cache = {}
    timeout = time()

    @classmethod
    async def _manage_timeout(cls):
        # Если таймер закончился - True
        # Если время до обновления осталось - False

        if time() - cls.timeout > 600:
            cls.cache = {}
            cls.timeout = time()
            return True
        return False
    
    @classmethod
    async def get_categories(cls):
        if "categories" in cls.cache and not cls._manage_timeout():
            return cls.cache["categories"]
        
        data = requests.get(f"https://api.moysklad.ru/api/remap/1.2/entity/productfolder", headers=cls.basic_headers).json()
        cls.cache["categories"] = data

        return data

    @classmethod
    async def get_parent_categories(cls):
        if "parent_categories" in cls.cache and not cls._manage_timeout():
            return cls.cache["parent_categories"]
        
        data = cls.get_categories()

        parent_categories = [category for category in data if not category["pathName"]]

        cls.cache["parent_categories"] = parent_categories

        return parent_categories