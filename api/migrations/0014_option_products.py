# Generated by Django 2.2.5 on 2019-09-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190915_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='products',
            field=models.ManyToManyField(related_name='options', to='api.Product'),
        ),
    ]