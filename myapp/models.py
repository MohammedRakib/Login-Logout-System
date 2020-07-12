from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name

