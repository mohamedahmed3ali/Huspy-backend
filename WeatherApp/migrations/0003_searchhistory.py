# Generated by Django 3.2.7 on 2021-09-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherApp', '0002_alter_cities_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('CityName', models.CharField(max_length=100)),
                ('Temperature', models.CharField(max_length=100, null=True)),
                ('Icon', models.CharField(max_length=100)),
                ('TempCondition', models.CharField(max_length=100)),
                ('SearchDate', models.DateField()),
            ],
        ),
    ]
