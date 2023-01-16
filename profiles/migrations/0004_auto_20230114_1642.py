# Generated by Django 3.2.16 on 2023-01-14 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_first_name',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]