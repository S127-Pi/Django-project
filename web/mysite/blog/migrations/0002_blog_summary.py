# Generated by Django 3.2.3 on 2021-05-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='This is the summary'),
        ),
    ]
