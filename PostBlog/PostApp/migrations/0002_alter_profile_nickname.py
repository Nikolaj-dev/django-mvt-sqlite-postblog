# Generated by Django 4.2 on 2023-04-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]