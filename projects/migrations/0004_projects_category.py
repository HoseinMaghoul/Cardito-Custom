# Generated by Django 2.2.12 on 2022-05-14 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='projects.Category'),
        ),
    ]
