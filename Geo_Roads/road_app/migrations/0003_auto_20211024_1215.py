# Generated by Django 2.2.4 on 2021-10-24 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('road_app', '0002_auto_20211023_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='distance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='road',
            name='road_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='road_app.RoadType'),
        ),
    ]
