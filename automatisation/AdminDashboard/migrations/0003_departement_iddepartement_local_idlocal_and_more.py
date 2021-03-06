# Generated by Django 4.0.5 on 2022-06-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0002_fournisseur_mail_fournisseur_numerotéléphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='IdDepartement',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='local',
            name='IdLocal',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='TYPE',
            field=models.CharField(choices=[('R', 'Routeur'), ('S', 'Switch'), ('F', 'Fédérateur'), ('MP', 'Machinepysique')], max_length=5),
        ),
    ]
