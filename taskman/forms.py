from django import forms
from taskman.models import Task, TaskType, TaskStatus


class TaskForm(forms.ModelForm):
    summary = forms.CharField(max_length=200, required=True, label='Краткое описание')
    description = forms.CharField(widget=forms.Textarea, required=False, label='Полное описание')
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), required=True, label='Статус')
    type = forms.ModelChoiceField(queryset=TaskType.objects.all(), required=True, label='Тип')

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
