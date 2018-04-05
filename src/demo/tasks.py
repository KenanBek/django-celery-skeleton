from __future__ import absolute_import, unicode_literals
from dcs.celeryconf import app


@app.task(bind=True, ignore_result=False, max_retries=3)
def demo_task1(self):
    result = {
        'val1': 1,
        'val2': 2,
        'val3': 3,
    }
    return result


@app.task(bind=True, ignore_result=False, max_retries=3)
def demo_task2(self):
    result = {
        'val1': 'a',
        'val2': 'b',
        'val3': 'c',
    }
    return result
