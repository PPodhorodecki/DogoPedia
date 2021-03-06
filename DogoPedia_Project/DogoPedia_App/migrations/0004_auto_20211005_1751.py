# Generated by Django 3.2.8 on 2021-10-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogoPedia_App', '0003_alter_users_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameField(
            model_name='dogs',
            old_name='name',
            new_name='dog_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='shalter_name',
        ),
        migrations.AlterField(
            model_name='dogs',
            name='race',
            field=models.CharField(max_length=64),
        ),
    ]
