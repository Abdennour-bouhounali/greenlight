# Generated by Django 4.2.6 on 2023-10-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.AddField(
            model_name='user',
            name='is_volunteer',
            field=models.BooleanField(default=False),
        ),
    ]
