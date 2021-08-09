from name_identifier.text import Text
import glob


class Loader:
    def __init__(self, input_dir, encoding='utf-8'):
        """

        :param input_dir: directory path of readable files
        :param encoding: text encoding
        """
        self.encoding: str = encoding
        self.input_dir: str = input_dir
        self.text_list = []
        self.paths = sorted(glob.glob(input_dir + '/*'))

    def add_txt(self, txt):
        self.text_list.append(txt)

    def load_files(self):
        """Loads files to self.text_list as Text objects"""
        for path in self.paths:
            with open(path, encoding=self.encoding) as f:
                content = f.read()
                txt = Text(path=path, content=content)
                self.add_txt(txt)
        return self.text_list
