# Generated by Django 4.2 on 2023-04-09 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0003_alter_postcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment',
            field=models.TextField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(5000)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=5000, null=True, validators=[django.core.validators.MaxLengthValidator(5000)]),
        ),
    ]
