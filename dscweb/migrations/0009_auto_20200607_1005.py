# Generated by Django 3.0.5 on 2020-06-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscweb', '0008_auto_20200607_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(upload_to='staticfiles/images/members/'),
        ),
    ]
