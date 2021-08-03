from name_identifier.entity import Entity
from utils.utils import preprocess_dict, insensitive_replace
import glob
import numpy as np
import os.path
from nltk.stem.snowball import FrenchStemmer


class NameIdentifier:
    def __init__(self, language='french', preprocess_dic=True, min_length=2):
        self.min_length: int = min_length
        self.language: str = language
        self.preprocess_dic: bool = preprocess_dic
        self.dict_path = glob.glob(os.path.abspath('resources') + f'\\{self.language}\\*')
        self.vocab: dict = {}
        self.stemmer = FrenchStemmer()

    def _load_dict(self):
        words_list = []
        for path in self.dict_path:
            with open(path, encoding='utf-8') as f:
                doc = f.readlines()
                doc = list(map(lambda x: x[:-1], doc))
                if self.preprocess_dic:
                    doc = list(map(lambda x: preprocess_dict(x), doc))
                words_list += doc
        words_list = list(np.unique(words_list))
        for i, word in enumerate(words_list):
            self.vocab[word] = i

    def word_in_vocab(self, word):
        try:
            _ = self.vocab[word]
            return True
        except:
            return False

    def find_entities(self, text_list):
        self._load_dict()
        for text in text_list:
            content = text.get_content()
            original_content = text.get_original_content()
            for word in content.split():
                length = len(word)
                if length <= self.min_length:
                    continue

                if not self.word_in_vocab(word):
                    stemmed_word = self.stemmer.stem(word)
                    if not self.word_in_vocab(stemmed_word):
                        start = content.find(word)
                        entity = Entity(word, start, len(word))
                        text.add_entity(entity)
        return text_list
