# Generated by Django 4.0.2 on 2022-02-08 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bootstraptemplatepage_alter_homepage_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bootstraptemplatepage',
            options={'verbose_name': 'Bootstrap template page', 'verbose_name_plural': 'bootstrap templates '},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home page site demo', 'verbose_name_plural': 'Accueil Bakery'},
        ),
    ]