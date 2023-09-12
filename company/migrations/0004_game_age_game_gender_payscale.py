# Generated by Django 4.2.4 on 2023-09-12 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='age',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.age'),
        ),
        migrations.AddField(
            model_name='game',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coed')], max_length=2),
        ),
        migrations.CreateModel(
            name='PayScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numRef', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coed')], max_length=2)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.age')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.leagues')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.role')),
            ],
        ),
    ]
