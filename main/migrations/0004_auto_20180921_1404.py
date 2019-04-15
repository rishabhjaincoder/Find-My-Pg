# Generated by Django 2.1a1 on 2018-09-21 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180903_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactowner',
            name='userid',
        ),
        migrations.AddField(
            model_name='contactowner',
            name='email',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactowner',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactowner',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
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