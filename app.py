from flask import Flask, render_template, request, send_from_directory, flash
from name_identifier.name_identifier import NameIdentifier
from anonymizers.anonymizer import Anonymizer
from name_identifier.text import Text
from werkzeug.utils import secure_filename
from typing import List
import tempfile
from zipfile import ZipFile
import os
from uuid import uuid4


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    supported_languages = NameIdentifier().get_supported_languages()
    no_files_message = ''
    anonymized = ''
    if request.method == 'GET':
        return render_template('main.html', supported_languages=supported_languages)
    else:
        files = request.files.getlist("file[]")
        if files[0].filename == '':
            no_files_message = 'please upload files'
        if files and allowed_files(files):
            file_list = []
            # upload
            for file in files:
                file_name = secure_filename(file.filename)
                content = file.read().decode('utf-8')
                text_file = Text(content=content, path=file_name)
                file_list.append(text_file)

            language = request.form.to_dict()['language']
            anonymized = anonymize(file_list, language=language)
            # zip and send
            temporary_dir = tempfile.mkdtemp()
            zip_name = str(uuid4()) + '.zip'
            temp_zip_path = os.path.join(temporary_dir, zip_name)
            zip_file = ZipFile(temp_zip_path, 'w')
            for file in anonymized:
                file_path = os.path.join(temporary_dir, file.get_file_name())
                with open(file_path, 'w') as f:
                    f.write(file.get_anonymized_content())
                f.close()
                zip_file.write(file_path, file.get_file_name())
            zip_file.close()
            return send_from_directory(temporary_dir, filename=zip_name)

        return render_template('main.html',
                               supported_languages=supported_languages,
                               anonymized=anonymized,
                               no_files_message=no_files_message)


def anonymize(file_text: List[Text], language: str) -> List[Text]:
    name_identifier = NameIdentifier(language=language)
    anonymizer = Anonymizer()
    identified = name_identifier.find_entities(file_text)
    anonymized = anonymizer.anonymize(identified)
    return anonymized


def allowed_file(file_name: str) -> bool:
    return '.txt' == ('.' + file_name.split('.')[-1].lower())


def allowed_files(files_list) -> bool:
    for file in files_list:
        if not allowed_file(file.filename):
            return False
    return True


if __name__ == '__main__':
    app.run(debug=True)
