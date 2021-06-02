from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.username


class Status(models.Model):
    status = models.CharField(max_length=9)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Status'


class Todo(models.Model):
    task = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    overview = models.TextField()
    employee = models.ManyToManyField(Employee)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.ManyToManyField(Status)

    def __str__(self):
        return self.task
