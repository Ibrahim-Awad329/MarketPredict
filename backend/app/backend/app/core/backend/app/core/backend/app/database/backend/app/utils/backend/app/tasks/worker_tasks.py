from celery import shared_task
import structlog

log = structlog.get_logger()

@shared_task
def test_task(name: str):
    log.info("Task started", name=name)
    return f"Hello {name}, task completed"
