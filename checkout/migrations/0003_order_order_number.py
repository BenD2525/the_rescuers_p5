# Generated by Django 3.2.16 on 2023-01-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='', editable=False, max_length=32),
        ),
    ]
