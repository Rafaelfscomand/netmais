# Generated by Django 2.1.7 on 2019-03-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipaments', '0007_auto_20190322_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='date',
            field=models.DateField(default='2019-05-05', verbose_name='Data'),
            preserve_default=False,
        ),
    ]
