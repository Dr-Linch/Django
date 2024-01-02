from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='dr.linch19@gmail.com',
            first_name='admin',
            last_name='admins',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('SkyPro123')
        user.save()