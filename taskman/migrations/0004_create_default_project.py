from django.db import migrations


def create_default_project(apps, schema_editor):
    Project = apps.get_model('taskman', 'Project')
    Task = apps.get_model('taskman', 'Task')

    project = Project.objects.create(
        start_date='2026-06-11',
        end_date=None,
        title='Тестовый проект',
        description='Проект для старых задач'
    )
    Task.objects.filter(project__isnull=True).update(project=project)


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0003_project_task_project'),
    ]

    operations = [
        migrations.RunPython(create_default_project, migrations.RunPython.noop),
    ]
