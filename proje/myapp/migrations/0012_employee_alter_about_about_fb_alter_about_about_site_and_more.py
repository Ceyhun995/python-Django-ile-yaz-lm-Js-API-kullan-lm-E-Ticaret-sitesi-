# Generated by Django 4.2.3 on 2023-08-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_about_about_linkedin_alter_about_about_site_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_image', models.FileField(upload_to='Photos', verbose_name='image')),
                ('employee_about', models.CharField(max_length=50, verbose_name='hakkında')),
                ('employee_fb', models.URLField(verbose_name='https://www.facebook.com/')),
                ('employee_x', models.URLField(verbose_name=' https://x.com/')),
                ('employee_linkedin', models.URLField(verbose_name='linkedin')),
                ('employee_site', models.URLField(verbose_name='http://127.0.0.1:8000/')),
                ('employee_name', models.CharField(max_length=50, verbose_name='isim')),
                ('employee_duty', models.CharField(max_length=50, verbose_name='görevi')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='about_fb',
            field=models.URLField(verbose_name='https://www.facebook.com/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_site',
            field=models.URLField(verbose_name='http://127.0.0.1:8000/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_x',
            field=models.URLField(verbose_name=' https://x.com/'),
        ),
    ]