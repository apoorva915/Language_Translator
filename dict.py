class LegalJargonTranslator:
    def _init_(self):
        # Example legal jargon dictionary
        self.jargon_dictionary = {
            'plaintiff': 'demandeur',
            'defendant': 'défendeur',
            'witness': 'témoin',
            'testimony': 'témoignage',
            # Add more terms to the dictionary
        }
    input_text=input("Enter input: ")

    def translate_text(self, input_text):
        # Split the input text into words
        words = input_text.split()

        # Translate each word using the legal jargon dictionary
        translated_words = [self.jargon_dictionary.get(word, word) for word in words]

        # Join the translated words back into a sentence
        translated_text = ' '.join(translated_words)
        print("Translated Text:", translated_text)
        return translated_text
