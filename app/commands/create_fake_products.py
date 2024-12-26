from django.core.management.base import BaseCommand
from app.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'create_fake_products'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Tạo 10 sản phẩm giả
            Product.objects.create(
                name=fake.word(),
                price=round(random.uniform(10.0, 100.0), 2),
                description=fake.text(),
                created_at=fake.date_time_this_year()
            )
        self.stdout.write(self.style.SUCCESS('Successfully created fake products'))