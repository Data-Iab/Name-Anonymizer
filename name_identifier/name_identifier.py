from typing import List
from name_identifier.entity import Entity
from name_identifier.text import Text
from utils.utils import preprocess_dic
import glob
import numpy as np
import os.path
import warnings


class NameIdentifier:
    def __init__(self, language='french', preprocess_dictionary=True, min_length=2):
        """Identifies foreign names in text

        :param language: one of supported languages (french only now)
        :param preprocess_dictionary: either to apply the preprocess_dic function or not
        :param min_length: minimum word length to be identified
        """
        self.min_length: int = min_length
        self.language: str = language
        self.preprocess_dictionary: bool = preprocess_dictionary
        relative_path = os.path.join(self.language, '*')
        self.dict_path = glob.glob(os.path.join(os.path.abspath('resources'), relative_path))
        self.vocab: dict = {}
        self.supported_languages = ['french']
        if language.lower() not in self.supported_languages:
            warnings.warn(f'Unsupported language, here is a list of supported languages: \n {self.supported_languages}')

    def get_supported_languages(self):
        return self.supported_languages

    def load_dict(self):
        """Loads dictionaries' words in /resources to self.vocab"""
        words_list = []
        for path in self.dict_path:
            with open(path, encoding='utf-8') as f:
                doc = f.readlines()
                doc = list(map(lambda x: x[:-1], doc))
                if self.preprocess_dictionary:
                    doc = list(map(lambda x: preprocess_dic(x), doc))
                words_list += doc
        words_list = list(np.unique(words_list))
        for i, word in enumerate(words_list):
            self.vocab[word] = i

    def word_in_vocab(self, word) -> bool:
        """Checks if the word is in self.vocab or not -> bool"""
        try:
            _ = self.vocab[word]
            return True
        except KeyError:
            return False

    def find_entities(self, text_list) -> List[Text]:
        """Fills list of Text object with found entities

        :param text_list: list of Text objects
        :return: List of [Text] with entities filled
        """
        self.load_dict()
        for text in text_list:
            content = text.get_content()
            for word in content.split():
                length = len(word)
                if length <= self.min_length:
                    continue

                if not self.word_in_vocab(word):
                    start = content.find(word)
                    entity = Entity(word, start, len(word))
                    text.add_entity(entity)
        return text_list
