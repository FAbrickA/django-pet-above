# Generated by Django 4.1.6 on 2023-02-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(db_index=True, default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
