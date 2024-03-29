# Generated by Django 4.2.4 on 2024-02-05 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dgc_app', '0002_metadata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='view',
            new_name='page_name',
        ),
        migrations.AddField(
            model_name='institution',
            name='requirements',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
