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
    list_display = ['id', 'summary', 'status', 'type', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    ordering = ['-created']
    fieldsets = (
        ('Основная информация', {
            'fields': ('summary', 'description')
        }),
        ('Категоризация', {
            'fields': ('status', 'type')
        }),
        ('Даты', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )