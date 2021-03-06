# Generated by Django 4.0.4 on 2022-04-14 09:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
                ('condition', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('asking_price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('make', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.company')),
            ],
        ),
    ]
