# Generated by Django 3.2.8 on 2021-10-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='filmname',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='scripts_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='scriptstep',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='username',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
    ]
