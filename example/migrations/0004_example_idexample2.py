# Generated by Django 2.2.1 on 2019-06-30 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_example2'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='idExample2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='example.Example2'),
            preserve_default=False,
        ),
    ]
