from unittest import TestCase
from all_prefixes import *


class TestLine_intersect(TestCase):
    def test_prefixes(self):
        self.assertEquals(all_prefixes('агора'), {'а', 'аг', 'аго', 'агор', 'агора'})
        self.assertEquals(all_prefixes('lead'), {'lea', 'l', 'lead', 'le'})
        self.assertEquals(all_prefixes('lealyd'), {'l', 'leal', 'ly', 'lea', 'lyd', 'le', 'lealyd', 'lealy'})
        self.assertEquals(all_prefixes('авангард'),
                          {'аван', 'ан', 'ар', 'авангард', 'аванг', 'анга', 'авангар', 'а', 'ангар', 'ард', 'ангард',
                           'аванга', 'анг', 'ава', 'ав'})
