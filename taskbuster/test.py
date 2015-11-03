# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils.translation import activate
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):

    def setUp(self):
        activate('en')

    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "taskbuster/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")

    def test_internationalization(self):
        for lang, h1_text in [('en', 'Welcome to TaskBuster!'),
                              ('ca', 'Benvingut a TaskBuster!')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)
