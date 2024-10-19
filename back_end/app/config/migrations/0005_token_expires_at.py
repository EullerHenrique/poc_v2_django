# Generated by Django 5.1 on 2024-09-13 02:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_token_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='expires_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
