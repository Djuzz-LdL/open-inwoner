import io
import logging

from django.core.management import call_command

from zgw_consumers.api_models.base import factory

from open_inwoner.celery import app
from open_inwoner.openzaak.api_models import Notification
from open_inwoner.openzaak.notifications import handle_zaken_notification

logger = logging.getLogger(__name__)


@app.task
def import_zgw_data():
    logger.info("starting import_zgw_data() task")

    out = io.StringIO()

    call_command("zgw_import_data", stdout=out)

    logger.info("finished import_zgw_data() task")

    return out.getvalue()


@app.task
def process_zaken_notification(notification_data: dict):
    logger.info("Started process_zaken_notification() task")
    notification = factory(Notification, notification_data)
    handle_zaken_notification(notification)
