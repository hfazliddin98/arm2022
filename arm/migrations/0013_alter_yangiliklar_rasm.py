# Generated by Django 4.2 on 2023-04-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0012_alter_yangiliklar_rasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yangiliklar',
            name='rasm',
            field=models.FileField(upload_to='yangiliklar/'),
        ),
    ]
