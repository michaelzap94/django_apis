# Generated by Django 2.2.6 on 2020-04-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(max_length=12),
        ),
    ]