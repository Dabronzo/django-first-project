from django.test import TestCase
from .models import Itens

class TestViews(TestCase):
    """Class test for views"""

    def test_get_todo_list(self):
        """To test it we will get a response of the home page ('/')
        and test if we get a ok reponse (200) and the correct template is being
        loaded """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_add_item_page(self):
        """To test it we will get a response of the page (/add)
        and test if we get a ok reponse (200) and the correct template is being
        loaded """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_edit_item_page(self):
        """ this test need along the edit an number of item id to be passed
        to solve this we gonna create an item for test to have an id (auto generated by python) """
        item = Itens.objects.create(name='Test edit item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        """here we create a response as a item 
        to simulate if the view will be redirect"""
        response = self.client.post('/add', {'name': 'Test add Item'})
        self.assertRedirects(response, '/')

    def test_can_toggle_item(self):
        """ Here also we need to create an item to see if will be toggled"""
        item = Itens.objects.create(name='Test edit item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Itens.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    
    def test_can_delete_item(self):
        """ Create an item and then see if the delete was sucess"""
        item = Itens.objects.create(name='Test delete item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_itens = Itens.objects.filter(id=item.id)
        self.assertEqual(len(existing_itens), 0)
    

    def test_can_edit_item(self):
        """ create an item, edit it on response and check"""
        item = Itens.objects.create(name='Test can edit item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Itens.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')