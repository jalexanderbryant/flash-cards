# Generated by Django 2.1 on 2018-08-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
