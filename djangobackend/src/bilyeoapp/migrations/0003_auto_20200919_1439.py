# Generated by Django 3.1.1 on 2020-09-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilyeoapp', '0002_auto_20200919_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rev_star',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=11),
        ),
    ]