from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    # Replace these with your desired superuser credentials
    username = "Admin"
    email = "Admin@gmail.com"
    password = "12345"

    User = get_user_model()  # Support for custom user models

    # Check if the superuser already exists
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

class Migration(migrations.Migration):

    dependencies = [
        # Add the latest migration file for auth (if not using a custom user model)
        ('auth', '0012_alter_user_first_name_max_length'),
        # Replace 'your_app_name' with your app's name and the previous migration
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
