# encoding=utf-8


from celery import Celery


broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('xxx', broker=broker, backend=backend, include=[
    'celery_.tasks'
])
app.conf.timezone = 'Asia/Shanghai'
# 导入指定的任务模块
# 启动worker    celery worker -A celery_app -l info -P=solo


# app.config_from_object('celery_app.celery_config')