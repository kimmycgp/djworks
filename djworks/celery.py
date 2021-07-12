from celery import Celery


app = Celery('tasks', broker="redis://localhost:16379", backend="redis://localhost:16379")


@app.task
def add(x, y):
    return x + y
