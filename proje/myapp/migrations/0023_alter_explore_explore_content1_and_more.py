# Generated by Django 4.2.3 on 2023-09-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_explore_alter_comment_comment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore',
            name='explore_content1',
            field=models.TextField(max_length=50, verbose_name='content1'),
        ),
        migrations.AlterField(
            model_name='explore',
            name='explore_content2',
            field=models.TextField(max_length=50, verbose_name='content2'),
        ),
        migrations.AlterField(
            model_name='explore',
            name='explore_content3',
            field=models.TextField(max_length=50, verbose_name='content3'),
        ),
        migrations.AlterField(
            model_name='explore',
            name='explore_content4',
            field=models.TextField(max_length=50, verbose_name='content4'),
        ),
    ]
