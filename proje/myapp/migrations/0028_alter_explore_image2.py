# Generated by Django 4.2.3 on 2023-09-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_explore_explore_title3_explore_explore_title4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore',
            name='image2',
            field=models.FileField(blank=True, upload_to='Explore', verbose_name='image2'),
        ),
    ]
