# Generated by Django 4.2.6 on 2023-10-14 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0011_donation_collected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
