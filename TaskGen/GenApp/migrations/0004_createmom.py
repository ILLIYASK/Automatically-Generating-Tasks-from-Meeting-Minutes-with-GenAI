# Generated by Django 4.2.1 on 2023-09-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenApp', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateMoM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.TextField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('attendees', models.TextField()),
                ('agenda', models.TextField()),
                ('discussion', models.TextField()),
            ],
        ),
    ]
