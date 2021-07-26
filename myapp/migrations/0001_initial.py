# Generated by Django 3.2.5 on 2021-07-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=1000)),
                ('short_url', models.CharField(max_length=70, unique=True)),
            ],
        ),
    ]