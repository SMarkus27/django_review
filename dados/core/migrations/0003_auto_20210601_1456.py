# Generated by Django 3.2.3 on 2021-06-01 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20210601_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
