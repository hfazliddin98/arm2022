# Generated by Django 4.2 on 2023-05-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talaba', '0003_talaba'),
    ]

    operations = [
        migrations.CreateModel(
            name='sinov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
            ],
        ),
    ]