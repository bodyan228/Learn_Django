# Generated by Django 4.1.2 on 2022-11-04 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
