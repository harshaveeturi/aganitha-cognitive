# aganitha-cognitive


This code is taken from https://github.com/HerambVD/spoken2written link.

# Usage


First you have to import the module using the below code.

import spoken2written

If it shows error during importing then spacy english dependency package is not installed in your device. In this case, install en_core_web_sm library using the command mentioned above.

After importing the package use TextTraslator method to translate spoken English to written form.

Example script:

>>>from spoken2written import TextTranslator

test= "My life is triple B . European authorities fined Google a record sixty five thousand dollars on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices . Furthermore , My T - Shirt size is double X in 2019 and it costs six dollars . My weight is fifty kilograms ."

result=TextTranslator(test)


print(result)


Output:
My life is BBB . European authorities fined Google a record $65000 on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices . Furthermore , My T - Shirt size is XX in 2019 and it costs $6 . My weight is 50 kg .

