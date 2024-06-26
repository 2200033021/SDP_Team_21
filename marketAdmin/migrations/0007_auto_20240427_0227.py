# Generated by Django 3.2.15 on 2024-04-26 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketAdmin', '0006_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='link',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='price',
        ),
        migrations.CreateModel(
            name='VegetablePlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField(blank=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketAdmin.platform')),
                ('vegetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketAdmin.vegitables')),
            ],
        ),
        migrations.CreateModel(
            name='GroceryPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField(blank=True)),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketAdmin.grocrey')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketAdmin.platform')),
            ],
        ),
    ]
