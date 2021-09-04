# Generated by Django 3.2.6 on 2021-08-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=600)),
                ('date', models.DateField(auto_now=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]