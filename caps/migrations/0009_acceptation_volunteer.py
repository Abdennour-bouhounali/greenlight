# Generated by Django 4.2.6 on 2023-10-14 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caps', '0008_acceptation_donation_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptation',
            name='volunteer',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
