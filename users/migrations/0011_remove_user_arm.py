# Generated by Django 4.2 on 2023-04-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_arm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='arm',
        ),
    ]