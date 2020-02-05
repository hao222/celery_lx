from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(default='xxxx', max_length=12)


    class Meta:
        db_table = "course_book"