# Generated by Django 4.2 on 2023-04-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('category_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('cat_img', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
