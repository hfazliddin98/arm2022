# Generated by Django 4.2 on 2023-04-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talaba', '0008_alter_tuman_viloyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kafedra',
            name='fakultet',
            field=models.CharField(max_length=100),
        ),
    ]