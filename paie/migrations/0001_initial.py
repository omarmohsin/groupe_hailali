# Generated by Django 3.2.7 on 2021-09-19 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aouloz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desg', models.CharField(max_length=100)),
                ('Qté', models.CharField(max_length=100)),
                ('pu', models.CharField(max_length=100)),
                ('pt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engrais_Aoulouz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, choices=[('Ammonitrate', 'Ammonitrate'), ('Sulfat_potasse', 'Sulfat_potasse'), ('MAP', 'MAP'), ('Nitrat_potasse', 'Nitrat_potasse'), ('Calcium', 'Calcium'), ('Complet', 'Complet'), ('Acide', 'Acide'), ('Sequestrine', 'Sequestrine'), ('Uree_46', 'Uree_46'), ('Kimia', 'Kimia')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engrais_berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, choices=[('Ammonitrate', 'Ammonitrate'), ('Sulfat_potasse', 'Sulfat_potasse'), ('MAP', 'MAP'), ('Nitrat_potasse', 'Nitrat_potasse'), ('Calcium', 'Calcium'), ('Complet', 'Complet'), ('Acide', 'Acide'), ('Sequestrine', 'Sequestrine'), ('Uree_46', 'Uree_46'), ('Kimia', 'Kimia')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engrais_drisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, choices=[('Ammonitrate', 'Ammonitrate'), ('Sulfat_potasse', 'Sulfat_potasse'), ('MAP', 'MAP'), ('Nitrat_potasse', 'Nitrat_potasse'), ('Calcium', 'Calcium'), ('Complet', 'Complet'), ('Acide', 'Acide'), ('Sequestrine', 'Sequestrine'), ('Uree_46', 'Uree_46'), ('Kimia', 'Kimia')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engrais_Mariem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, choices=[('Ammonitrate', 'Ammonitrate'), ('Sulfat_potasse', 'Sulfat_potasse'), ('MAP', 'MAP'), ('Nitrat_potasse', 'Nitrat_potasse'), ('Calcium', 'Calcium'), ('Complet', 'Complet'), ('Acide', 'Acide'), ('Sequestrine', 'Sequestrine'), ('Uree_46', 'Uree_46'), ('Kimia', 'Kimia')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engrais_Rgaigue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(blank=True, choices=[('Ammonitrate', 'Ammonitrate'), ('Sulfat_potasse', 'Sulfat_potasse'), ('MAP', 'MAP'), ('Nitrat_potasse', 'Nitrat_potasse'), ('Calcium', 'Calcium'), ('Complet', 'Complet'), ('Acide', 'Acide'), ('Sequestrine', 'Sequestrine'), ('Uree_46', 'Uree_46'), ('Kimia', 'Kimia')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mariemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desg', models.CharField(max_length=100)),
                ('Qté', models.CharField(max_length=100)),
                ('pu', models.CharField(max_length=100)),
                ('pt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Od_berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desg', models.CharField(max_length=100)),
                ('Qté', models.CharField(max_length=100)),
                ('pu', models.CharField(max_length=100)),
                ('pt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Od_drisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desg', models.CharField(max_length=100)),
                ('Qté', models.CharField(max_length=100)),
                ('pu', models.CharField(max_length=100)),
                ('pt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pesticide_Aoulouz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Karaté', 'Karaté'), ('Blouz', 'Blouz'), ('AG3', 'AG3'), ('Agrale', 'Agrale'), ('Coperniko', 'Coperniko'), ('Confidor', 'Confidor'), ('Valmec', 'Valmec'), ('Joker', 'Joker'), ('Pixel', 'Pixel'), ('Coperide', 'Coperide'), ('Mospelan', 'Mospelan'), ('Rondo', 'Rondo'), ('Fozika', 'Fozika'), ('Movinto', 'Movinto'), ('enfidor-speed', 'enfidor-speed'), ('Magnome', 'Magnome'), ('Mamba', 'Mamba'), ('Fozika_ca', 'Fozika_ca'), ('Soufre', 'Soufre')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pesticide_berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Karaté', 'Karaté'), ('Blouz', 'Blouz'), ('AG3', 'AG3'), ('Agrale', 'Agrale'), ('Coperniko', 'Coperniko'), ('Confidor', 'Confidor'), ('Valmec', 'Valmec'), ('Joker', 'Joker'), ('Pixel', 'Pixel'), ('Coperide', 'Coperide'), ('Mospelan', 'Mospelan'), ('Rondo', 'Rondo'), ('Fozika', 'Fozika'), ('Movinto', 'Movinto'), ('enfidor-speed', 'enfidor-speed'), ('Magnome', 'Magnome'), ('Mamba', 'Mamba'), ('Fozika_ca', 'Fozika_ca'), ('Soufre', 'Soufre')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pesticide_drisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Karaté', 'Karaté'), ('Blouz', 'Blouz'), ('AG3', 'AG3'), ('Agrale', 'Agrale'), ('Coperniko', 'Coperniko'), ('Confidor', 'Confidor'), ('Valmec', 'Valmec'), ('Joker', 'Joker'), ('Pixel', 'Pixel'), ('Coperide', 'Coperide'), ('Mospelan', 'Mospelan'), ('Rondo', 'Rondo'), ('Fozika', 'Fozika'), ('Movinto', 'Movinto'), ('enfidor-speed', 'enfidor-speed'), ('Magnome', 'Magnome'), ('Mamba', 'Mamba'), ('Fozika_ca', 'Fozika_ca'), ('Soufre', 'Soufre')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pesticide_Mariem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Karaté', 'Karaté'), ('Blouz', 'Blouz'), ('AG3', 'AG3'), ('Agrale', 'Agrale'), ('Coperniko', 'Coperniko'), ('Confidor', 'Confidor'), ('Valmec', 'Valmec'), ('Joker', 'Joker'), ('Pixel', 'Pixel'), ('Coperide', 'Coperide'), ('Mospelan', 'Mospelan'), ('Rondo', 'Rondo'), ('Fozika', 'Fozika'), ('Movinto', 'Movinto'), ('enfidor-speed', 'enfidor-speed'), ('Magnome', 'Magnome'), ('Mamba', 'Mamba'), ('Fozika_ca', 'Fozika_ca'), ('Soufre', 'Soufre')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pesticide_Rgaigue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Karaté', 'Karaté'), ('Blouz', 'Blouz'), ('AG3', 'AG3'), ('Agrale', 'Agrale'), ('Coperniko', 'Coperniko'), ('Confidor', 'Confidor'), ('Valmec', 'Valmec'), ('Joker', 'Joker'), ('Pixel', 'Pixel'), ('Coperide', 'Coperide'), ('Mospelan', 'Mospelan'), ('Rondo', 'Rondo'), ('Fozika', 'Fozika'), ('Movinto', 'Movinto'), ('enfidor-speed', 'enfidor-speed'), ('Magnome', 'Magnome'), ('Mamba', 'Mamba'), ('Fozika_ca', 'Fozika_ca'), ('Soufre', 'Soufre')], max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('entree', models.CharField(max_length=100)),
                ('cumul_entree', models.CharField(max_length=100)),
                ('sortie', models.CharField(max_length=100)),
                ('cumul_sortie', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='rgaigueo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desg', models.CharField(max_length=100)),
                ('Qté', models.CharField(max_length=100)),
                ('pu', models.CharField(max_length=100)),
                ('pt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rgaigue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('np', models.CharField(blank=True, max_length=100)),
                ('sdb', models.CharField(max_length=100)),
                ('j1', models.CharField(max_length=100)),
                ('j2', models.CharField(max_length=100)),
                ('j3', models.CharField(max_length=100)),
                ('j4', models.CharField(max_length=100)),
                ('j5', models.CharField(max_length=100)),
                ('j6', models.CharField(max_length=100)),
                ('j7', models.CharField(max_length=100)),
                ('nb_j', models.FloatField(max_length=100)),
                ('base', models.FloatField(max_length=100)),
                ('ancienneté', models.FloatField(max_length=100)),
                ('pf', models.FloatField(max_length=100)),
                ('sb', models.FloatField(max_length=100)),
                ('cnss', models.FloatField(max_length=100)),
                ('amo', models.FloatField(max_length=100)),
                ('net_p', models.FloatField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ouled_drisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('np', models.CharField(blank=True, max_length=100)),
                ('sdb', models.CharField(max_length=100)),
                ('j1', models.CharField(max_length=100)),
                ('j2', models.CharField(max_length=100)),
                ('j3', models.CharField(max_length=100)),
                ('j4', models.CharField(max_length=100)),
                ('j5', models.CharField(max_length=100)),
                ('j6', models.CharField(max_length=100)),
                ('j7', models.CharField(max_length=100)),
                ('nb_j', models.FloatField(max_length=100)),
                ('base', models.FloatField(max_length=100)),
                ('ancienneté', models.FloatField(max_length=100)),
                ('pf', models.FloatField(max_length=100)),
                ('sb', models.FloatField(max_length=100)),
                ('cnss', models.FloatField(max_length=100)),
                ('amo', models.FloatField(max_length=100)),
                ('net_p', models.FloatField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ouled_berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('np', models.CharField(blank=True, max_length=100)),
                ('sdb', models.CharField(max_length=100)),
                ('j1', models.CharField(max_length=100)),
                ('j2', models.CharField(max_length=100)),
                ('j3', models.CharField(max_length=100)),
                ('j4', models.CharField(max_length=100)),
                ('j5', models.CharField(max_length=100)),
                ('j6', models.CharField(max_length=100)),
                ('j7', models.CharField(max_length=100)),
                ('nb_j', models.FloatField(max_length=100)),
                ('base', models.FloatField(max_length=100)),
                ('ancienneté', models.FloatField(max_length=100)),
                ('pf', models.FloatField(max_length=100)),
                ('sb', models.FloatField(max_length=100)),
                ('cnss', models.FloatField(max_length=100)),
                ('amo', models.FloatField(max_length=100)),
                ('net_p', models.FloatField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mariem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('np', models.CharField(blank=True, max_length=100)),
                ('sdb', models.CharField(max_length=100)),
                ('j1', models.CharField(max_length=100)),
                ('j2', models.CharField(max_length=100)),
                ('j3', models.CharField(max_length=100)),
                ('j4', models.CharField(max_length=100)),
                ('j5', models.CharField(max_length=100)),
                ('j6', models.CharField(max_length=100)),
                ('j7', models.CharField(max_length=100)),
                ('nb_j', models.FloatField(max_length=100)),
                ('base', models.FloatField(max_length=100)),
                ('ancienneté', models.FloatField(max_length=100)),
                ('pf', models.FloatField(max_length=100)),
                ('sb', models.FloatField(max_length=100)),
                ('cnss', models.FloatField(max_length=100)),
                ('amo', models.FloatField(max_length=100)),
                ('net_p', models.FloatField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='caisse_Rgaigue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100)),
                ('recette', models.CharField(blank=True, max_length=100)),
                ('cumul_recette', models.CharField(blank=True, max_length=100)),
                ('depense', models.CharField(blank=True, max_length=100)),
                ('cumul_depense', models.CharField(blank=True, max_length=100)),
                ('solde', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='caisse_Mariem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100)),
                ('recette', models.CharField(blank=True, max_length=100)),
                ('cumul_recette', models.CharField(blank=True, max_length=100)),
                ('depense', models.CharField(blank=True, max_length=100)),
                ('cumul_depense', models.CharField(blank=True, max_length=100)),
                ('solde', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='caisse_drisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100)),
                ('recette', models.CharField(blank=True, max_length=100)),
                ('cumul_recette', models.CharField(blank=True, max_length=100)),
                ('depense', models.CharField(blank=True, max_length=100)),
                ('cumul_depense', models.CharField(blank=True, max_length=100)),
                ('solde', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='caisse_berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100)),
                ('recette', models.CharField(blank=True, max_length=100)),
                ('cumul_recette', models.CharField(blank=True, max_length=100)),
                ('depense', models.CharField(blank=True, max_length=100)),
                ('cumul_depense', models.CharField(blank=True, max_length=100)),
                ('solde', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='caisse_Aoulouz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100)),
                ('recette', models.CharField(blank=True, max_length=100)),
                ('cumul_recette', models.CharField(blank=True, max_length=100)),
                ('depense', models.CharField(blank=True, max_length=100)),
                ('cumul_depense', models.CharField(blank=True, max_length=100)),
                ('solde', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=100)),
                ('titre', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('times', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aoulouz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('np', models.CharField(blank=True, max_length=100)),
                ('sdb', models.CharField(max_length=100)),
                ('j1', models.CharField(max_length=100)),
                ('j2', models.CharField(max_length=100)),
                ('j3', models.CharField(max_length=100)),
                ('j4', models.CharField(max_length=100)),
                ('j5', models.CharField(max_length=100)),
                ('j6', models.CharField(max_length=100)),
                ('j7', models.CharField(max_length=100)),
                ('nb_j', models.FloatField(max_length=100)),
                ('base', models.FloatField(max_length=100)),
                ('ancienneté', models.FloatField(max_length=100)),
                ('pf', models.FloatField(max_length=100)),
                ('sb', models.FloatField(max_length=100)),
                ('cnss', models.FloatField(max_length=100)),
                ('amo', models.FloatField(max_length=100)),
                ('net_p', models.FloatField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
