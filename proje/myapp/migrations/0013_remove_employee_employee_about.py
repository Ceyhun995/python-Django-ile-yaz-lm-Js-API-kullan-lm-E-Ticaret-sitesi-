# Generated by Django 4.2.3 on 2023-08-29 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_employee_alter_about_about_fb_alter_about_about_site_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_about',
        ),
    ]