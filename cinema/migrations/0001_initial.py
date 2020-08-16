# Generated by Django 3.1 on 2020-08-15 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceNor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceSch', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceStud', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceChild', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('number', models.IntegerField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.hall')),
            ],
        ),
    ]
