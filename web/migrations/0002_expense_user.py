from django.db import migrations, models
import django.db.models.deletion
from web.models import DEFAULT_USER_ID
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=DEFAULT_USER_ID, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
