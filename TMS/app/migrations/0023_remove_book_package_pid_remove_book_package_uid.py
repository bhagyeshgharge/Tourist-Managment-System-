# Generated by Django 5.0 on 2024-01-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_book_package_pid_book_package_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_package',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='book_package',
            name='uid',
        ),
    ]
