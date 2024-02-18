# Generated by Django 4.2.10 on 2024-02-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='store/media/uploads/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]