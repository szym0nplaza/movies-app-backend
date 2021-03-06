# Generated by Django 3.2.5 on 2021-07-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_alter_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='director',
            name='photo',
        ),
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.ImageField(default='directors/default.jpg', upload_to='actors/'),
        ),
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.ImageField(default='directors/default.jpg', upload_to='directors/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='directors/default.jpg', upload_to='movies/'),
        ),
    ]
