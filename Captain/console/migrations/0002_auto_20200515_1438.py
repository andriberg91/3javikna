# Generated by Django 3.0.6 on 2020-05-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='console',
            name='detailed_description',
            field=models.CharField(blank=True, max_length=3999),
        ),
        migrations.AlterField(
            model_name='console',
            name='description',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
