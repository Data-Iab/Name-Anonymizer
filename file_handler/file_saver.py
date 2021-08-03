from pathlib import Path


class Saver:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save(self, text_list):
        base_path = self.output_dir + '\\Anonymized'
        Path(base_path).mkdir(parents=True, exist_ok=True)

        for text in text_list:
            name = text.get_file_name()
            content = text.get_anonymized_content()
            save_path = base_path + '\\' + name
            with open(save_path, 'w') as f:
                f.write(content)
