from utils.utils import preprocess_text


class Text:
    def __init__(self, path, content):
        self.path: str = path
        self.original_content: str = content
        self.content: str = preprocess_text(content)
        self.anonymized_content: str = ''
        self.entities = []

    def set_anonymized_content(self, a):
        self.anonymized_content = a

    def get_original_content(self):
        return self.original_content

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entities(self):
        return self.entities

    def get_file_name(self) -> str:
        return self.path.split('\\')[-1]

    def set_original_content(self, a):
        self.original_content = a

    def get_content(self):
        return self.content
