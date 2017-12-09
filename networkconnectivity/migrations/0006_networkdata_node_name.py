# Generated by Django 2.0 on 2017-12-09 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('networkconnectivity', '0005_remove_networkdata_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdata',
            name='node_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networkconnectivity.NetworkNode'),
            preserve_default=False,
        ),
    ]