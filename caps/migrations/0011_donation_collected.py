# Generated by Django 4.2.6 on 2023-10-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0010_acceptation_deposit_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='collected',
            field=models.BooleanField(default=False),
        ),
    ]
