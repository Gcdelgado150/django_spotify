# Generated by Django 5.1.4 on 2024-12-05 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
