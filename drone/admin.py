from django.contrib import admin
from .models import Drone,AuditLog
# Register your models here.

admin.site.register(Drone)
admin.site.register(AuditLog)
