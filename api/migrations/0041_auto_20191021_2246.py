# Generated by Django 2.2.5 on 2019-10-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20191013_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(default='', max_length=32, verbose_name='Alt'),
        ),
    ]
