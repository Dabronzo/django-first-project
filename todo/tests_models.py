from django.test import TestCase
from .models import Itens

class TestModel(TestCase):

    def test_done_default_to_false(self):
        item = Itens.objects.create(name='Test for model')
        self.assertFalse(item.done)

    def test_string_model(self):
        item = Itens.objects.create(name='Test for model')
        self.assertEqual(str(item), 'Test for model')
