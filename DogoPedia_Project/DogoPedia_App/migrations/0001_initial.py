# Generated by Django 3.2.8 on 2021-10-05 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('telephone', models.BigIntegerField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, null=True)),
                ('race', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField(null=True)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('description', models.CharField(max_length=1024)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DogoPedia_App.users')),
            ],
        ),
    ]
