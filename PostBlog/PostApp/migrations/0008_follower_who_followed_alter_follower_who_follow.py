# Generated by Django 4.2 on 2023-04-12 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0007_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='who_followed',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='who_followed', to='PostApp.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='who_follow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_follow', to='PostApp.profile'),
        ),
    ]
