# Generated by Django 2.0 on 2017-12-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0012_spirit_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
