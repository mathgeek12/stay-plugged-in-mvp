from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from app.database import MODELS_MODULES, TORTOISE_ORM
from app import models
from app.config import settings

Tortoise.init_models(MODELS_MODULES, "models")

app = FastAPI(
    title="Stay Plugged In API",
    description=("This service offers data for stay plugged" "in orders."),
    version="1.0",
    docs_url="/docs" if settings.DOCS_ENABLED else None,
    redoc_url="/redoc" if settings.DOCS_ENABLED else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=TORTOISE_ORM)

employee_pydantic = pydantic_model_creator(models.Employee)
device_types_pydantic = pydantic_model_creator(models.DeviceType)
repair_type_pydantic = pydantic_model_creator(models.RepairType)
orders_pydantic = pydantic_model_creator(models.Orders)


@app.get("/employees/")
async def get_employee():
    return await employee_pydantic.from_queryset(models.Employee.all())


@app.get("/device-types/")
async def get_device_type():
    return await device_types_pydantic.from_queryset(models.DeviceType.all())


@app.get("/repair-type/")
async def get_repair_type():
    return await repair_type_pydantic.from_queryset(models.RepairType.all())


@app.get("/orders/")
async def get_orders():
    return await orders_pydantic.from_queryset(models.Orders.all())
