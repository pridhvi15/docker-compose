# Generated by Django 5.2.3 on 2025-06-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
