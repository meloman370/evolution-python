# Generated by Django 2.2.5 on 2019-09-17 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20190917_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SliderBlock')),
            ],
        ),
        migrations.AddField(
            model_name='sliderblock',
            name='products',
            field=models.ManyToManyField(through='api.SliderProduct', to='api.Product'),
        ),
    ]
