from datetime import timedelta
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Booking, MenuItem

User = get_user_model()

class LittleLemonAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="TestPass123!")
        self.client.force_authenticate(user=self.user)

    def test_menu_list_returns_items(self):
        MenuItem.objects.create(title="Greek Salad", price=Decimal("12.50"), inventory=20)
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Greek Salad")

    def test_menu_create_requires_authentication_for_write(self):
        self.client.force_authenticate(user=None)
        response = self.client.post("/api/menu/", {
            "title": "Bruschetta", "price": "8.50", "inventory": 12
        }, format="json")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_menu_item(self):
        response = self.client.post("/api/menu/", {
            "title": "Bruschetta", "price": "8.50", "inventory": 12
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_user_can_create_and_list_own_booking(self):
        response = self.client.post("/api/bookings/", {
            "name": "Alex",
            "no_of_guests": 2,
            "booking_date": (timezone.now() + timedelta(days=1)).isoformat(),
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        list_response = self.client.get("/api/bookings/")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)

    def test_booking_endpoint_requires_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 401)

    def test_registration_endpoint(self):
        self.client.force_authenticate(user=None)
        response = self.client.post("/api/register/", {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "NewUserPass123!",
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username="newuser").exists())
