# Generated by Django 3.1.5 on 2021-01-06 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Растение', 'verbose_name_plural': 'Растения'},
        ),
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.IntegerField(verbose_name='Нома воды')),
                ('date', models.DateField(verbose_name='Дата и время полива')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.articles')),
            ],
            options={
                'verbose_name': 'Полив растений',
                'verbose_name_plural': 'Полив растений',
            },
        ),
    ]
