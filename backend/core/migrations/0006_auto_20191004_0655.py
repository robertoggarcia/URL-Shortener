# Generated by Django 2.2.6 on 2019-10-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191004_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.CharField(default='t', editable=False, max_length=2000, primary_key=True, serialize=False),
        ),
    ]
