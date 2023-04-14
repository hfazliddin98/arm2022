# Generated by Django 4.1.6 on 2023-03-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0005_rename_talaba_talabalar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitoblar',
            old_name='mundarija',
            new_name='munddarija',
        ),
        migrations.AlterField(
            model_name='kitoblar',
            name='alfabit',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='kitoblar',
            name='darslik_turi',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='kitoblar',
            name='kitob_turi',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='kitoblar',
            name='tili',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='yangiliklar',
            name='rasm',
            field=models.ImageField(upload_to='yangiliklar/'),
        ),
    ]