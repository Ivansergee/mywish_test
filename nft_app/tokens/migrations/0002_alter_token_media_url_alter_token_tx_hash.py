# Generated by Django 4.0.4 on 2022-04-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='media_url',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='token',
            name='tx_hash',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
