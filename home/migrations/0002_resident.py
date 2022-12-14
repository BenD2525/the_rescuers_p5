# Generated by Django 3.2.16 on 2022-12-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('updated', models.DateField(auto_now=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('favourite_toy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
