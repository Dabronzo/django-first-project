from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):
    """Test class for the form"""

    def test_item_name_is_required(self):
        """we will instantiate an form with no name value to check if the sys
        catch it"""
        form = ItemForm({'name': ' '})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertAlmostEqual(form.errors['name'][0], 'This field is required.')
    
    def test_if_done_field_not_required(self):
        """the done checkbox should not be required"""
        form = ItemForm({'name': 'Test name item'})
        self.assertTrue(form.is_valid())

    def test_if_the_explicity_metadata_is_displayed(self):
        """Test to ensure just the data that is meant to be displayed
        will be dispayed"""
        form = ItemForm()
        self.assertAlmostEqual(form.Meta.fields, ['name', 'done'])
    