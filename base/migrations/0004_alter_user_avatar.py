# Generated by Django 4.1.3 on 2022-11-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/avatar.svg', null=True, upload_to=''),
        ),
    ]
