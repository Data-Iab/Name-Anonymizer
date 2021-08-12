# Name-Anonymizer for data protection (beta)

##What is Name-Anonymizer ?

Name Anonymizer is a simple tool that detects and hides foreign words (could be names, locations...) in text.<br/>
***Best use: French text with non-French names.***

![plot](image1.jpg)

## How to use it ?

Clone the repository and run the following command:

<code>python main.py input_directory output_directory</code> 

<code>input_directory</code> : path to the directory containing text files to anonymize (make sure it contains only readable files)

<code>output_directory</code> : path to the directory of anonymized text files.

## Open it in your local machine using Streamlit

Explore Names Anonymizer with a GUI by running the command:

<code>streamlit run runGUI.py</code> 

<ol>
<li>Browse readable files</li>
<li>Click Anonymize button</li>
<li>Download files</li>
</ol>

![plot](image2.jpg)
