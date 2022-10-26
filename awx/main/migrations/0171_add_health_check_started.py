# Generated by Django 3.2.13 on 2022-09-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0170_node_and_link_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='health_check_started',
            field=models.DateTimeField(editable=False, help_text='The last time a health check was initiated on this instance.', null=True),
        ),
    ]