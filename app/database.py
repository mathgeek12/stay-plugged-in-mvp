from tortoise import Tortoise

from app.config import PostgresConfig

from aerich import Command

MODELS_MODULES = ["app.models", "aerich.models"]
TORTOISE_ORM = {
    "connections": {"default": PostgresConfig.get_url(PostgresConfig.db_name)},
    "apps": {
        "models": {
            "models": MODELS_MODULES,
            "default_connection": "default",
        },
    },
}


# Create Database Tables
async def init(_create_db: bool = False, generate_schemas: bool = False):
    await Tortoise.init(
        config=TORTOISE_ORM,
        _create_db=_create_db,
    )
    if generate_schemas:
        await Tortoise.generate_schemas(safe=True)


async def shutdown() -> None:
    await Tortoise.close_connections()


async def migrate():
    command = Command(tortoise_config=TORTOISE_ORM, app="models")
    await command.init()
    await command.migrate()
    await command.upgrade()
