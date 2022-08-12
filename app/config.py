import os

from dynaconf import Dynaconf

abs_directory = os.path.dirname(os.path.realpath(__file__))

_ENV_PREFIX = "STAYPLUGGED"
settings = Dynaconf(
    envvar_prefix=_ENV_PREFIX,
    settings_files=[f"{abs_directory}/settings.yaml", f"{abs_directory}/.secrets.yaml"],
    env_switcher=f"{_ENV_PREFIX}_ENV",
    environments=True,
)


# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
class PostgresConfig:
    db_name = settings.POSTGRES_DB_NAME
    host = settings.POSTGRES_HOST
    port = settings.POSTGRES_PORT
    user_name = settings.POSTGRES_USERNAME
    user_password = settings.POSTGRES_PASSWORD

    url = f"postgres://{user_name}:{user_password}@{host}:{port}"

    @classmethod
    def get_url(cls, database_name: str) -> str:
        return f"{cls.url}/{database_name}"
