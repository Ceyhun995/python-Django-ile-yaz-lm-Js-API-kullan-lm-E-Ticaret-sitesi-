# Generated by Django 4.2.3 on 2023-09-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_sosial_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sosial_media',
            name='sosial_link',
            field=models.URLField(verbose_name='Link'),
        ),
    ]
