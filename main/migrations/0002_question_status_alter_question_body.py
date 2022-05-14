# Generated by Django 4.0.4 on 2022-05-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('n', 'Named'), ('a', 'Anonymous')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
