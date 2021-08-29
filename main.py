from name_identifier.name_identifier import NameIdentifier
from file_handler.file_loader import Loader
from file_handler.file_saver import Saver
from anonymizers.anonymizer import Anonymizer
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir',
                        metavar='path',
                        type=str,
                        help='directory globing text files to anonymize')
    parser.add_argument('output_dir',
                        metavar='path',
                        type=str,
                        help='output directory')

    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir

    start = time.time()
    name_identifier = NameIdentifier()
    loader = Loader(input_dir)
    saver = Saver(output_dir)
    anonymizer = Anonymizer()

    text_list = loader.load_files()
    text_list = name_identifier.find_entities(text_list)
    text_list = anonymizer.anonymize(text_list)

    saver.save(text_list)
    end = time.time()
    print(f'Executed in {end-start}s')


if __name__ == '__main__':
    main()
