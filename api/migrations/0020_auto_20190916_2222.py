# Generated by Django 2.2.5 on 2019-09-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('weight', models.IntegerField(default=0, verbose_name='Вес')),
                ('type', models.CharField(default='slider', max_length=20, verbose_name='Тип')),
            ],
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='HomepageBlock',
        ),
    ]