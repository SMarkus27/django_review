from django.contrib import admin
from .models import Author, Employee, Status, Todo

admin.site.register(Author)
admin.site.register(Employee)
admin.site.register(Status)
admin.site.register(Todo)
