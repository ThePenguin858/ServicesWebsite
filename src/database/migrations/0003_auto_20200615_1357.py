# Generated by Django 3.0.7 on 2020-06-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200615_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatura',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fatura',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]