# Generated by Django 3.2 on 2023-06-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
