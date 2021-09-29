# Name-Anonymizer for data protection (beta)

## What is Name-Anonymizer ?


Name Anonymizer is a simple tool that uses OOV to detect and hide foreign words (could be names, locations...) in text.<br/>
***Best use: French text with non-French names.***

<div style="text-align:center"><img src="image1.jpg"  width="700" height="300"/></div>

## Deployment

This app is deployed in Heroku, you can use it from [here](https://name-anonymizer.herokuapp.com/)

## Local use

Clone the repository and run the following command:

<code>python main.py input_directory output_directory</code> 

<code>input_directory</code> : path to the directory containing text files to anonymize (make sure it contains only readable files)

<code>output_directory</code> : path to the directory of anonymized text files.</code>

## Supported languages

Currently, the only supported language is French, check supported languages using:

<code> NameIdentifier().get_supported_languages()</code>

## Add a custom VOCABULARY

If you have any custom words you don't want to anonymize, create you own vocabulary of words in a .txt file (each word in a line) and add it to /resources/LANGUAGE/
