from utils.utils import insensitive_replace


class Anonymizer:
    def __init__(self, replace_names='<Confidential>'):
        self.replace = replace_names

    def anonymize(self, text_list):
        for txt in text_list:
            content = txt.get_original_content()

            entities = txt.get_entities()
            for entity in entities:
                word = entity.to_dict()['entity']
                content = insensitive_replace(txt=content,
                                              sub_text=word,
                                              replace=self.replace)

            txt.set_anonymized_content(content)
        return text_list
