# Generated by Django 3.0.8 on 2020-07-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200713_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_text',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='TEXT'),
        ),
    ]
