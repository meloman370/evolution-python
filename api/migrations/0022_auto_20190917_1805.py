# Generated by Django 2.2.5 on 2019-09-17 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderblock',
            name='weight',
        ),
        migrations.AddField(
            model_name='block',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='sliderblock',
            name='block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='block', to='api.Block'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sliderblock',
            name='title',
            field=models.CharField(max_length=32, verbose_name='Заголовок'),
        ),
    ]
