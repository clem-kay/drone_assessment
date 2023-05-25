from celery.utils.log import get_task_logger
from drone_assessment.celery import app
from drone.models import Drone,AuditLog

logger = get_task_logger(__name__)

@app.task
def task_one():
    drones = Drone.objects.all()
    for drone in drones:
        audit_log = AuditLog(drone,drone.battery_capacity)
        audit_log.save()
