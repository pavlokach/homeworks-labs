class CursorAfterFile(Exception):
    pass


class CursorBeforeFile(Exception):
    pass


class InvalidDelete(Exception):
    pass


class NoNameSave(Exception):
    pass


class TooLongCharacter(Exception):
    pass


class Cursor:
    def __init__(self, document):
        """Initializing variables"""
        self.document = document
        self.position = 0

    def forward(self):
        """changing cursor position forward"""
        if self.position > len(self.document.string) - 1:
            raise CursorAfterFile("Cursor is after file")
        self.position += 1

    def back(self):
        """changing cursor position backward"""
        if self.position == 0:
            raise CursorBeforeFile("Cursor is before file")
        self.position -= 1

    def home(self):
        """moving cursor forward to the closest newline"""
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """moving cursor backward to the closest newline"""
        while self.position < len(
                self.document.characters) and \
                self.document.characters[self.position].character != '\n':
            self.position += 1


class Document:
    def __init__(self):
        """Initializing variables"""
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def set_name(self, message=''):
        """Changing variable filename"""
        self.filename = input(message)

    def insert(self, character):
        """Type only 1 character to the cursor position"""
        if len(character) - 1:
            raise TooLongCharacter("Can't add more than 1 character")
        self.characters.insert(self.cursor.position,
                               character)
        self.cursor.forward()

    def delete(self):
        """delete only 1 character after cursor"""
        if self.cursor.position > len(self.string) - 1:
            raise InvalidDelete("Can't delete non-existent character")
        del self.characters[self.cursor.position]

    def save(self):
        """writing to document"""
        if not self.filename:
            raise NoNameSave("Can't save unnamed file")
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        """returning document as string"""
        return "".join((str(c) for c in self.characters))


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        """Initializing variables"""
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """adding '*', '/' or '_' depending on style"""
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

    def insert(self, character):
        """adding character if it's not there"""
        if not hasattr(character, 'character'):
            self.character = Character(character)
doc = Document()
doc.filename = "test_document"
doc.insert('h')
doc.insert('e')
doc.insert('l')
doc.insert('l')
doc.insert('o')
print(doc.string)
doc.cursor.back()
doc.cursor.back()
doc.delete()
doc.insert('p')
doc.delete()

print("".join(doc.characters))
