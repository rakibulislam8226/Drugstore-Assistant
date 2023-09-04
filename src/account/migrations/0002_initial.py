# Generated by Django 4.2.4 on 2023-09-04 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='organizationuser',
            constraint=models.UniqueConstraint(condition=models.Q(('is_default', True)), fields=('user',), name='user_have_one_default_organization', violation_error_message='A merchant can have only one default organization.'),
        ),
        migrations.AlterUniqueTogether(
            name='organizationuser',
            unique_together={('organization', 'user')},
        ),
    ]
