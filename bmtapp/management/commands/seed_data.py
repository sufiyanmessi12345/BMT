# bmtapp/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from bmtapp.models import Section, SectionUser

class Command(BaseCommand):
    help = 'Seeds the database with initial sections and users.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        sections_data = [
            {'id': 'received-orders', 'title': 'Received Orders'},
            {'id': 'design-engineering', 'title': 'Design & Engineering'},
            {'id': 'procurement', 'title': 'Procurement / Purchasing'},
            {'id': 'production-planning', 'title': 'Production Planning'},
            {'id': 'quality-control', 'title': 'Quality Control'},
            {'id': 'packaging-dispatch', 'title': 'Packaging & Dispatch'},
            {'id': 'warehouse', 'title': 'Warehouse'},
            {'id': 'pending-orders', 'title': 'Pending Orders'},
        ]

        users_data = {
            "received-orders": {"username": "received", "password": "1234"},
            "design-engineering": {"username": "design", "password": "1234"},
            "procurement": {"username": "procurement", "password": "1234"},
            "production-planning": {"username": "production", "password": "1234"},
            "quality-control": {"username": "quality", "password": "1234"},
            "packaging-dispatch": {"username": "packaging", "password": "1234"},
            "warehouse": {"username": "warehouse", "password": "1234"},
            "pending-orders": {"username": "pending", "password": "1234"}
        }

        for sec_data in sections_data:
            section, created = Section.objects.get_or_create(
                id=sec_data['id'], 
                defaults={'title': sec_data['title']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created section: {section.title}'))
            
            user_info = users_data.get(section.id)
            if user_info:
                # Hash the password before creating the user
                hashed_password = make_password(user_info['password'])
                
                SectionUser.objects.get_or_create(
                    section=section,
                    defaults={
                        'username': user_info['username'],
                        'password': hashed_password
                    }
                )
                self.stdout.write(f'Created/updated user for {section.title}')
                
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))