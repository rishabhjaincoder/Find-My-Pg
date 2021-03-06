# Generated by Django 2.1.1 on 2018-09-21 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180921_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ameneties',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PG'),
        ),
        migrations.AlterField(
            model_name='contactowner',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PG'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PG'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AlterField(
            model_name='pg',
            name='ownerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Owner'),
        ),
        migrations.AlterField(
            model_name='pgimages',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PG'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PG'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
