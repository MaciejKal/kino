# Generated by Django 3.0.8 on 2020-08-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
