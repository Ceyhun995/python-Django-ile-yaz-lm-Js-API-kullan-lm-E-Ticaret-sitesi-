# Generated by Django 4.2.3 on 2023-08-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_product_stok'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=50, verbose_name='title')),
                ('about_image', models.FileField(upload_to='Photos', verbose_name='resim')),
                ('about_content', models.TextField(verbose_name='content start')),
                ('about_content1', models.TextField(blank=True, null=True, verbose_name='content center')),
                ('about_content2', models.TextField(blank=True, null=True, verbose_name='content end')),
                ('about_fb', models.URLField(verbose_name='fb')),
                ('about_x', models.URLField(verbose_name='fb')),
                ('about_linkedin', models.URLField(verbose_name='fb')),
                ('about_site', models.URLField(verbose_name='fb')),
            ],
        ),
    ]
