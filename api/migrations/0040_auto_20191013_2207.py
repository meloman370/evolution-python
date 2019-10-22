# Generated by Django 2.2.5 on 2019-10-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20191001_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optiongroup',
            name='categories',
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='CategoryOptionGroup',
        ),
    ]