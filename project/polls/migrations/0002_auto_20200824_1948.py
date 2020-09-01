# Generated by Django 3.1 on 2020-08-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=None, verbose_name='time published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
