# Generated by Django 4.2.3 on 2023-09-01 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_rename_comment_user_comment_comment_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productdetail', to='myapp.about', verbose_name='nereye'),
        ),
    ]
