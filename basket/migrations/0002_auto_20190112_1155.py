# Generated by Django 2.1.5 on 2019-01-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Продукты', 'Продукты'), ('Бытовая химия', 'Бытовая химия'), ('Одежда', 'Одежда')], max_length=100, verbose_name='Название категории'),
        ),
    ]
