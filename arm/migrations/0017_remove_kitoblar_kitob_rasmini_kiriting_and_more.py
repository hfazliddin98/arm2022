# Generated by Django 4.2 on 2023-05-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0016_alter_kitoblar_anatatsiya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitoblar',
            name='kitob_rasmini_kiriting',
        ),
        migrations.AddField(
            model_name='kitoblar',
            name='kitob_rasmi',
            field=models.FileField(blank=True, upload_to='rasm/'),
        ),
    ]
