# Generated by Django 4.2 on 2024-04-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='optionmenu',
            options={'verbose_name': 'Opción de menu', 'verbose_name_plural': 'Opciones de menu'},
        ),
        migrations.AlterField(
            model_name='optionmenu',
            name='link_url',
            field=models.CharField(blank=True, default='#', help_text='URL or URI to the content, eg /about/ or http://opcion.com/', max_length=100, null=True),
        ),
    ]
