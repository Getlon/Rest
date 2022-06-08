# Generated by Django 4.0.5 on 2022-06-08 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField()),
                ('beauty_title', models.TextField()),
                ('title', models.TextField()),
                ('other_titles', models.TextField()),
                ('connect', models.CharField(blank=True, max_length=1)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('level_winter', models.TextField(blank=True, max_length=3)),
                ('level_summer', models.TextField(blank=True, max_length=3)),
                ('level_autumn', models.TextField(blank=True, max_length=3)),
                ('level_spring', models.TextField(blank=True, max_length=3)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.BinaryField()),
                ('title_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmitData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.TextField()),
                ('title', models.TextField()),
                ('other_titles', models.TextField()),
                ('connect', models.CharField(blank=True, max_length=1)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('fam', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('otc', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
                ('level_winter', models.TextField(blank=True, max_length=3)),
                ('level_summer', models.TextField(blank=True, max_length=3)),
                ('level_autumn', models.TextField(blank=True, max_length=3)),
                ('level_spring', models.TextField(blank=True, max_length=3)),
                ('data', models.BinaryField()),
                ('title_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('fam', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('otc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pereval.perevaladded')),
                ('title', models.TextField()),
                ('status', models.TextField(choices=[('new', 'new'), ('pending', 'pending'), ('rejected', 'rejected'), ('accepted', 'accepted')], default='new')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAddedPerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pereval_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.perevaladded')),
                ('pereval_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.perevalimages')),
            ],
        ),
    ]
