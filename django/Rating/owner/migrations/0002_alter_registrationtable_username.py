# Generated by Django 4.2.7 on 2023-11-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationtable',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
