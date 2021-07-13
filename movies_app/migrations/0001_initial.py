# Generated by Django 3.2.5 on 2021-07-13 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(default='2010-01-01')),
                ('photo', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('year_of_production', models.DateField(default='2010-01-01')),
                ('image', models.URLField(max_length=300)),
                ('description', models.TextField()),
                ('director', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies_app.director')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(default='2010-01-01')),
                ('photo', models.URLField(max_length=300)),
                ('movies', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies_app.movie')),
            ],
        ),
    ]