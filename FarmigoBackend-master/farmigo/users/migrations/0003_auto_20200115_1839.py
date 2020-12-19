# Generated by Django 3.0.2 on 2020-01-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200115_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='address',
            field=models.CharField(default='Address', max_length=64),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='district',
            field=models.CharField(default='District', max_length=64),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='mobnumber',
            field=models.CharField(default='Mobile Number', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='state',
            field=models.CharField(default='State', max_length=32),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='username',
            field=models.CharField(default='Mobile Number', max_length=10, unique=True),
        ),
    ]
