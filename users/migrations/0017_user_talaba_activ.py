# Generated by Django 4.2 on 2023-05-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_delete_activ'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='talaba_activ',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
    ]
