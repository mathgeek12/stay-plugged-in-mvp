import asyncio

from app.database import init

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init(True, True))
