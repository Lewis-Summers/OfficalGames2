# Generated by Django 4.2.4 on 2023-09-11 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='leagues',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sport'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='company.teams'),
        ),
        migrations.AddField(
            model_name='game',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.field'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='company.teams'),
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.leagues'),
        ),
        migrations.AddField(
            model_name='game',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sport'),
        ),
        migrations.AddField(
            model_name='field',
            name='complex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.complex'),
        ),
        migrations.AddField(
            model_name='complex',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='company',
            name='leadAdmin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.game'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.role'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='age',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sport'),
        ),
    ]
