# Generated by Django 2.1.7 on 2019-03-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True)),
            ],
            options={
                'db_table': 'contributors',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('iswc', models.CharField(max_length=255,
                                          primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=255)),
                ('contributors', models.ManyToManyField(
                    to='works_single_view.Contributors')),
            ],
            options={
                'db_table': 'works',
            },
        ),
    ]
