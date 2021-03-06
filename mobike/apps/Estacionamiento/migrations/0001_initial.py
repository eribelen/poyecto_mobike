# Generated by Django 3.1.2 on 2020-10-27 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bicicleta', '0005_auto_20201024_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(choices=[('Sin Comuna', 'Seleccione Comuna'), ('La Reina', 'La Reina'), ('Ñuñoa', 'Ñuñoa'), ('Providencia', 'Providencia')], default='Sin Comuna', max_length=15)),
                ('direccion', models.TextField()),
                ('bicicletasDisponibles', models.IntegerField()),
                ('bicicleta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bicicleta.bicicleta')),
            ],
        ),
    ]
