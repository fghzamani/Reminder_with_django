# Generated by Django 3.2.5 on 2021-07-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20210730_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='piority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='L', max_length=10),
        ),
    ]
