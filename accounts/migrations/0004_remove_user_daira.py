# Generated by Django 4.2.6 on 2023-10-13 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_active_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='daira',
        ),
    ]
