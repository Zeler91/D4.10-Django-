# Generated by Django 2.2.6 on 2019-12-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('book', models.ManyToManyField(to='p_library.Book')),
            ],
        ),
    ]
