# Generated by Django 3.2.6 on 2021-09-13 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-datetime',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
