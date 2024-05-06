# Generated by Django 5.0.1 on 2024-02-09 19:56

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
                ('title', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to='image', verbose_name='photo')),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=None)),
                ('in_shopping_cart', models.BooleanField(default=False)),
                ('order', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to='image', verbose_name='photo')),
            ],
        ),
    ]
