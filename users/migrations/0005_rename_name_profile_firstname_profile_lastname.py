# Generated by Django 4.0.3 on 2022-03-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_address_alter_profile_address2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
    ]