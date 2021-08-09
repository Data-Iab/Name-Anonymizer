from utils.utils import preprocess_text
from typing import List
from name_identifier.entity import Entity


class Text:
    def __init__(self, path, content):
        """

        :param path: text file path
        :param content: file content
        """
        self.path: str = path
        self._original_content: str = content
        self._content: str = preprocess_text(content)
        self.anonymized_content: str = ''
        self.entities: List[Entity] = []

    def get_file_name(self) -> str:
        return self.path.split('\\')[-1]

    def add_entity(self, entity):
        self.entities.append(entity)

    def set_anonymized_content(self, a):
        self.anonymized_content = a

    def get_anonymized_content(self):
        return self.anonymized_content

    def get_original_content(self):
        return self._original_content

    def get_entities(self):
        return self.entities

    def get_content(self):
        return self._content
