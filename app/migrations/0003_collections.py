# Generated by Django 5.0 on 2024-01-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image_hover'),
    ]

    operations = [
        migrations.CreateModel(
            name='collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners')),
            ],
        ),
    ]
