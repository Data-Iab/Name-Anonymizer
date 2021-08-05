import os


class Saver:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save(self, text_list):
        """Saves list of Text objects' anonymized content in output_dir in .txt format"""
        base_path = self.output_dir + '\\Anonymized'
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        for text in text_list:
            name = text.get_file_name()
            content = text.get_anonymized_content()
            save_path = base_path + '\\' + name
            with open(save_path, 'w') as f:
                f.write(content)
