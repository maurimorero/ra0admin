# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import Chasis

# Create your tests here.

class ChasisTests(TestCase):

    def test_chasis_valido(self):
        todos = Chasis.objects.all()
        c1= Chasis()
        c1.name="C1"
        c1.description="asdasds"
        self.assertEqual(c1.name, "C10")