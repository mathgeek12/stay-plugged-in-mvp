from tortoise import Model, fields


class PluggedBaseModel(Model):
    id = fields.IntField(pk=True)
    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Employee(PluggedBaseModel):
    name = fields.TextField()


class DeviceType(PluggedBaseModel):
    name = fields.TextField()


class RepairType(PluggedBaseModel):
    name = fields.TextField()


class Orders(PluggedBaseModel):
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    employee = fields.ForeignKeyField("models.Employee")
    device_type = fields.ForeignKeyField("models.DeviceType")
    repair_type = fields.ForeignKeyField("models.RepairType")
