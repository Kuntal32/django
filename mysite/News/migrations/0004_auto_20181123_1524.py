# Generated by Django 2.0.5 on 2018-11-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_sportsnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sportsnews',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
