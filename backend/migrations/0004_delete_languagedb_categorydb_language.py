# Generated by Django 4.2.2 on 2023-07-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_categorydb_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='languagedb',
        ),
        migrations.AddField(
            model_name='categorydb',
            name='Language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]