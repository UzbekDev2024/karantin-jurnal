# Generated by Django 4.2.7 on 2024-05-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tahririyat_talablar'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnallar',
            name='korishlarSoni',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jurnallar',
            name='yuklashlarSoni',
            field=models.IntegerField(default=1),
        ),
    ]
