# Generated by Django 2.2.13 on 2020-08-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app26', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='features',
            field=models.TextField(blank=True),
        ),
    ]
