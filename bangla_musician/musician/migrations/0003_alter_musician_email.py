# Generated by Django 5.0.4 on 2024-08-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musician_email_alter_musician_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
