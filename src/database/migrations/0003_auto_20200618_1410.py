# Generated by Django 3.0.7 on 2020-06-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200618_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nif',
            field=models.CharField(max_length=9),
        ),
    ]