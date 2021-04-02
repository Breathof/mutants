from celery import Celery
from celery.utils.log import get_task_logger

import time

logger = get_task_logger(__name__)

app = Celery('works',
                    broker='amqp://admin:mypass@localhost:5672',
                    backend='rpc://')

@app.task
def save_message(message):
    time.sleep(5)
    return True
