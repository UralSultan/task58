from django.contrib import admin
from .models import Task, TaskType, TaskStatus, Project


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
    list_display = ('summary', 'project', 'status', 'created', 'updated')
    filter_horizontal = ('type',)
    exclude = ('is_deleted',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    ordering = ['-start_date']
