# Generated by Django 3.2.5 on 2021-07-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='venue',
            name='outdoor',
            field=models.BooleanField(default=True),
        ),
    ]
