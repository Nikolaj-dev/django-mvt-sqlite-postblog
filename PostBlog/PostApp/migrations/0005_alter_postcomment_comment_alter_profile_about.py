# Generated by Django 4.2 on 2023-04-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0004_alter_postcomment_comment_alter_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
