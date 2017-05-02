from unittest import TestCase
from VigenereCipher import VigenereCipher

class TestVigenereCipher(TestCase):
    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"

    def test_combine_character(self):
        cipher = VigenereCipher("TRAIN")
        assert cipher.combine_character("E", "T") == "X"
        assert cipher.combine_character("N", "R") == "E"

    def test_encode_character(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        assert encoded == "X"

    def test_separate_character(self):
        cipher = VigenereCipher("TRAIN")
        assert cipher.separate_character("X", "T") == "E"
        assert cipher.separate_character("E", "R") == "N"

    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encoded("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_lowercase(self):
        cipher = VigenereCipher("TRain")
        encoded = cipher.encoded("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"