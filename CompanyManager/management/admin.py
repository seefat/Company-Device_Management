from django.contrib import admin
from .models import (
    Company,
    Employee,
    Device,
    CheckIn,
    CheckOut,
    DeviceLog
)
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(DeviceLog)