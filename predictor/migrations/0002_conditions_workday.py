# Generated by Django 2.1 on 2019-01-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditions',
            name='workday',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
