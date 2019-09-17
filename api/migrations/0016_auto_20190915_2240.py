# Generated by Django 2.2.5 on 2019-09-15 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190915_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('option_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OptionGroup')),
            ],
        ),
        migrations.AddField(
            model_name='optiongroup',
            name='categories',
            field=models.ManyToManyField(related_name='groups', through='api.CategoryOptionGroup', to='api.Category'),
        ),
    ]
