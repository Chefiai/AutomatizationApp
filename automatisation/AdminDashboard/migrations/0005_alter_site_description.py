# Generated by Django 4.0.5 on 2022-06-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0004_alter_equipement_ip_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='Description',
            field=models.TextField(),
        ),
    ]