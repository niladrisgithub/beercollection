# Generated by Django 3.2.5 on 2021-07-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20210714_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='venues',
            field=models.ManyToManyField(to='main_app.Venue'),
        ),
    ]
