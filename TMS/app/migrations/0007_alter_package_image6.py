# Generated by Django 5.0 on 2024-01-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_package_image6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='Image6',
            field=models.ImageField(upload_to='image'),
        ),
    ]
