# Generated by Django 2.1 on 2019-01-21 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.FloatField()),
                ('timestamp', models.DateTimeField(verbose_name='время')),
                ('temp', models.FloatField()),
                ('felt_temp', models.FloatField()),
                ('wind', models.FloatField()),
                ('holiday', models.BooleanField()),
                ('season', models.IntegerField()),
                ('weather', models.IntegerField()),
            ],
        ),
    ]
