# Generated by Django 3.0.6 on 2020-05-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0003_console_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='console',
            name='quantity',
        ),
    ]
