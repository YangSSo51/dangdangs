# Generated by Django 2.2.3 on 2019-08-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190730_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]