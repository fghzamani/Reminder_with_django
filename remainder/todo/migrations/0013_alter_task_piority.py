# Generated by Django 3.2.5 on 2021-07-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_rename_completed_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='piority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=10),
        ),
    ]
