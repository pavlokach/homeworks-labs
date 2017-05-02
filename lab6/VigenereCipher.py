class VigenereCipher:
    # Class for encrypting/decrypting
    def __init__(self, keyword):
        # Initializing
        self.keyword = keyword

    def extend_keyword(self, number):
        # Counting
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        #
        text = text.replace(" ", "").upper()

        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    @staticmethod
    def combine_character(plain, keyword):
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    @staticmethod
    def separate_character(cypher, keyword):
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    def encode(self, plaintext):
        return self._code(plaintext, VigenereCipher.combine_character)

    def decode(self, ciphertext):
        return self._code(ciphertext, VigenereCipher.separate_character)