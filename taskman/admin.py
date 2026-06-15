from django.contrib import admin
from .models import Task, TaskType, TaskStatus


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('summary', 'status', 'created', 'updated')
    filter_horizontal = ('type',)