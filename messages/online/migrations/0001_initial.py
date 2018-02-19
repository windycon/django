# Generated by Django 2.0.1 on 2018-02-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
    ]
