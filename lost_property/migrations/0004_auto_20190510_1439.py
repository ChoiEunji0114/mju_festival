# Generated by Django 2.2.1 on 2019-05-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost_property', '0003_auto_20190510_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
