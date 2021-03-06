# Generated by Django 2.2.5 on 2019-09-15 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_optiongroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiongroup',
            name='machine_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Машинное имя'),
        ),
        migrations.AlterField(
            model_name='optiongroup',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('value', models.CharField(max_length=32, verbose_name='Значение')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.OptionGroup')),
            ],
        ),
    ]
