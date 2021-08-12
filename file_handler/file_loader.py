from name_identifier.text import Text
import glob
from typing import List
import warnings


class Loader:
    def __init__(self, input_dir=None, paths=None, encoding='utf-8'):
        """

        :param input_dir: directory path of readable files
        :param paths: readable files paths. Pass either input_dir
                      or list of paths, if both are passed priority goes to paths
        :param encoding: text encoding
        """
        self.encoding: str = encoding
        self.input_dir: str = input_dir
        self.text_list: List[str] = []
        self.paths = paths
        if paths is None:
            try:
                self.paths: List[str] = sorted(glob.glob(input_dir + '/*'))
            except:
                print()

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


class STLoader(Loader):
    def __init__(self, uploaded, **kwargs):
        super().__init__(uploaded, **kwargs)
        self.uploaded = uploaded

    def load_files(self):
        """Loads files to self.text_list as Text objects"""
        for file in self.uploaded:
            content = file.read().decode(self.encoding)
            txt = Text(path=file.name, content=content)
            self.add_txt(txt)
        return self.text_list
