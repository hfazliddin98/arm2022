# Generated by Django 4.2 on 2023-04-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_arm_lavozim_user_arm_bolim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lavozim',
            field=models.CharField(blank=True, default='talaba', max_length=100),
        ),
    ]
