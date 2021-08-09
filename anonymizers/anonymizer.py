from utils.utils import insensitive_replace


class Anonymizer:
    def __init__(self, replace_entities='<Confidential>'):
        """

        :param replace_entities: string to replace entities with
        """
        self.replace_entities: str = replace_entities

    def anonymize(self, text_list):
        """Sets Text anonymized content after replacing entities with self.replace_entities"""
        for txt in text_list:
            content = txt.get_original_content()
            entities = txt.get_entities()
            for entity in entities:
                word = entity.to_dict()['entity']
                content = insensitive_replace(text=content,
                                              sub_text=word,
                                              replace=self.replace_entities)

            txt.set_anonymized_content(content)
        return text_list
