# Generated by Django 2.0 on 2017-12-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0015_usercocktail'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='spirit1',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='spirit2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='spirit3',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='spirit4',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='spirit5',
            field=models.CharField(default='', max_length=30),
        ),
    ]
