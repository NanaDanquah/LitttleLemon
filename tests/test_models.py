from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Fufu', price=45, inventory=5)
        self.assertEqual(str(item), "Fufu : 45")
