# Generated by Django 3.2.5 on 2021-07-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_beer_venues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='outdoor',
        ),
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='venue',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='venue',
            name='state',
            field=models.CharField(default='', max_length=15),
        ),
    ]
