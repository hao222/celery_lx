import time

from celery.task import Task

from course.models import Book
from celery_.celery import app

# class CourseTask(Task):
#
#     name = 'course-task'
#
#     def run(self, *args, **kwargs):
#         print('start task .......')
#         time.sleep(2)
#         Book.objects.create(name='woxiao')
#         print('args={}, kwargs={}'.format(args, kwargs))
#         print('end task .....')

@app.task
def run(*args, **kwargs):
    print('start task .......')
    time.sleep(2)
    Book.objects.create(name='xiaoming')
    print('args={}, kwargs={}'.format(args, kwargs))
    print('end task .....')