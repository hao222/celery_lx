
from django.http import JsonResponse
from django.shortcuts import render
from celery_.tasks import run
# Create your views here.
from course.models import Book
# from course.tasks import CourseTask
from celery_.celery import app


def do(request):

    print('start request')
    # 第一种
    # CourseTask.delay()
    # 第二种
    # CourseTask.apply_async(args=('hello',), queue='work_queue')
    # run.delay()
    # 第三种调用
    app.send_task("tasks.run", args=[1,2])
    print('end reuqest...')
    # Book.objects.create(name='xxx')
    return JsonResponse({'result':'ok'})