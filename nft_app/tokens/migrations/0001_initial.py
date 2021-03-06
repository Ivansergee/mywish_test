# Generated by Django 4.0.4 on 2022-04-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(max_length=20, unique=True)),
                ('tx_hash', models.CharField(blank=True, max_length=255, unique=True)),
                ('media_url', models.URLField()),
                ('owner', models.CharField(max_length=255)),
            ],
        ),
    ]
