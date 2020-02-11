# Generated by Django 2.1.10 on 2019-07-07 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terrain', '0003_auto_20180518_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='TerrainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('terrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terrain.Terrain')),
            ],
        ),
    ]