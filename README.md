
# speech to text

This python module converts speech to text.

e.g. It will convert:   "I watched movie triple H ." to "I watched movie named HHH"
                        "My weight is fifty five kilograms ." to "My weight is 55 kg"
                        
<h1>Installation guide</h1>

Run this command in terminal:
```
pip install speech-text
```
The dependencies spaCy,word2number will also be installed after installing the package.
It is better to have english language dependency requirement of spacy which is en_core_web_sm

To install this en_core_web_sm, run following command in terminal
```
python -m spacy download en_core_web_sm
```
<h1>Usage</h1>

First you have to import the module using the below code.
```
import speech_text
```

After importing the package use speech_2_text method to translate spoken to written form.

Example script:
```
>>>from speech_text import speech2text
...sentence="This is triple A and this is double B try to repeat it "
...result=speech2text(sentence)
...print(result)
```
Output:
```
This is triple AAA and this is double BB try to repeat it
```

<h1>Features Used to Develop this package</h1>

1. Name Entity Recognition technique is used to detect entities from given input. Name Entity Recognition is done using the library named 'spaCy'. Entities such as QUANTITY (E.g weight: fifty kilograms), MONEY(e.g. amount: thousand dollars), PROPER NOUNS are detected using this technique.

2. The package word2number is used to convert numbers written as 'two thousand' to '2000'. Furthermore, few lines of logical code adds suffix/prefix as $/kg,etc. depending upon type of entity.

3. In some texts entity such as"double X" may occur. In this case, the word double acts as adjective followed by X as noun. To detect such texts along with their corresponding parts of speech spacy Token Matcher is used. Again, after detection of entity few lines of logical code will translate "double X" to "XX".

