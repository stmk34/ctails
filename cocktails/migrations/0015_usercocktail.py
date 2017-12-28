# Generated by Django 2.0 on 2017-12-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0014_auto_20171228_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCocktail',
            fields=[
                ('taste', models.CharField(max_length=20)),
                ('cocktail_name', models.CharField(max_length=50, primary_key='true', serialize=False)),
                ('difficulty', models.CharField(max_length=20)),
                ('cocktail_pic', models.FileField(upload_to='')),
                ('strength', models.CharField(max_length=20)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
