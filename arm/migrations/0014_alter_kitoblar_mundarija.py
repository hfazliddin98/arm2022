# Generated by Django 4.2 on 2023-05-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0013_alter_yangiliklar_rasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitoblar',
            name='mundarija',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
