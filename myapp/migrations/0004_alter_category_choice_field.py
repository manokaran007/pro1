# Generated by Django 5.0.2 on 2024-03-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='choice_field',
            field=models.CharField(choices=[('Blind', 'Blind'), ('Deaf', 'Deaf')], max_length=10),
        ),
    ]