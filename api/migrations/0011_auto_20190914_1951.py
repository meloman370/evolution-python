# Generated by Django 2.2.5 on 2019-09-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190914_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='inner_image',
            new_name='origin_inner',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='thumb_image',
            new_name='origin_thumb',
        ),
        migrations.AddField(
            model_name='image',
            name='compressed_inner',
            field=models.ImageField(blank=True, upload_to='./catalog/inner', verbose_name='Сжатое изображение'),
        ),
        migrations.AddField(
            model_name='image',
            name='compressed_thumb',
            field=models.ImageField(blank=True, upload_to='./catalog/thumb', verbose_name='Сжатое изображение тизер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(max_length=32, verbose_name='Alt'),
        ),
    ]