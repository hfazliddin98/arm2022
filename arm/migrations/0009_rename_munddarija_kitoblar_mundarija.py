# Generated by Django 4.2 on 2023-04-11 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0008_alter_kitoblar_anatatsiya'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitoblar',
            old_name='munddarija',
            new_name='mundarija',
        ),
    ]
