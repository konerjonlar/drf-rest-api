# Generated by Django 3.2.9 on 2021-11-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muni_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]