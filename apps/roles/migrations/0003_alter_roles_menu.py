# Generated by Django 4.2 on 2024-04-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_optionmenu_options_alter_optionmenu_link_url'),
        ('roles', '0002_roles_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='menu',
            field=models.ManyToManyField(to='menu.menu'),
        ),
    ]