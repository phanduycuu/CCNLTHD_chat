# Generated by Django 5.0.12 on 2025-04-24 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
        ('message', '0004_remove_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='file.file'),
        ),
    ]
