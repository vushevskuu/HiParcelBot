import unittest
from aiogram import types
from handlers.advert_handler import create_advert

class TestAdvertHandlers(unittest.TestCase):
    async def test_create_advert(self):
        message = types.Message(text="/create_advert")
        response = await create_advert(message)
        self.assertIn("Создание объявления", response.text)

if __name__ == '__main__':
    unittest.main()