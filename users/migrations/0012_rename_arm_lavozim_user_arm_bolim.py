# Generated by Django 4.2 on 2023-04-09 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_arm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='arm_lavozim',
            new_name='arm_bolim',
        ),
    ]
