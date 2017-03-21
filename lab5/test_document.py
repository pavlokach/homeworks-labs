from unittest import TestCase
from document import *


class TestDocument(TestCase):
    def __init__(self):
        doc = Document()
        doc.insert('h')
        doc.insert('e')
        doc.insert('l')
        doc.insert('l')
        doc.insert('o')
        self.assertEquals(doc.string, "hello")
        doc.cursor.back()
        doc.cursor.back()
        doc.delete()
        doc.insert('p')
        doc.delete()
        self.assertEquals(doc.string, "help")