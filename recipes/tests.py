from django.test import TestCase
from django.urls import reverse, resolve

class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id':1})
        self.assertEqual(url, '/receitas/1/')
        