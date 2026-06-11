from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'

    def __str__(self):
        return self.name



class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, related_name='tasks',)
    type = models.ForeignKey(TaskType, on_delete=models.PROTECT, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created']

    def __str__(self):
        return self.summary
