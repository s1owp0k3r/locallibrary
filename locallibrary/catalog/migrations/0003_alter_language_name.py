# Generated by Django 4.1.7 on 2023-03-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Enter a book language', max_length=200),
        ),
    ]
