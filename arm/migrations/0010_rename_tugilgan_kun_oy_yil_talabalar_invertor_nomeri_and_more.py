# Generated by Django 4.1.7 on 2023-04-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0009_rename_munddarija_kitoblar_mundarija'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talabalar',
            old_name='tugilgan_kun_oy_yil',
            new_name='invertor_nomeri',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='darajasi',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='familya',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='guruh',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='ism',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='kocha_uy',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='kurs',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='sharifi',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='tuman',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='viloyat',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='yonalish',
        ),
        migrations.AddField(
            model_name='talabalar',
            name='talaba_id',
            field=models.CharField(default=21, max_length=100),
            preserve_default=False,
        ),
    ]