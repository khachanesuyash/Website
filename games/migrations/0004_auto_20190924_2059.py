# Generated by Django 2.2.5 on 2019-09-24 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190924_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='game',
        ),
        migrations.AddField(
            model_name='sales',
            name='games',
            field=models.ForeignKey(default=1, max_length=150, on_delete=django.db.models.deletion.CASCADE, to='games.Games'),
        ),
        migrations.AlterField(
            model_name='games',
            name='year',
            field=models.IntegerField(),
        ),
    ]
