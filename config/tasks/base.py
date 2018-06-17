import logging
from celery import Task
from flask_mail import Message

from config.settings import mail
from config.static_config import current_config

logger = logging.getLogger(__name__)


class BaseTask(Task):
    abstract = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.exception(str(einfo))
        logger.debug("Task_id {} failed, Arguments are {}".format(task_id, args))

        if current_config.IS_ERROR_MAIL_ENABLED:
            # send error mail
            mail_subject = "[App Celery] for task_id {}, {}".format(task_id, str(exc))

            mail_body = "\nargs: {} \nkwargs: {}\n\n\n {}".format(args, kwargs, (str(einfo)))
            msg = Message(subject=mail_subject, body=mail_body, sender=current_config.DEFAULT_MAIL_SENDER, recipients=current_config.ADMINS)
            mail.send(msg)
