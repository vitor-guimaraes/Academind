# Generated by Django 5.0.6 on 2024-06-03 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookoutlet', '0003_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookoutlet.author'),
        ),
    ]
