# Generated by Django 4.2.6 on 2023-10-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0007_donation_donated_acceptation'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptation',
            name='donation_rejected',
            field=models.BooleanField(default=False),
        ),
    ]