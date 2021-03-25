import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
from word2number import w2n

def parseRepeatedItems(sentence):
  # Process the text a
  nlp=spacy.load('en_core_web_sm')
  temp_text=sentence.split()
  doc = nlp(sentence)

  #pattern matcing using nlp
  matcher=Matcher(nlp.vocab)
  single_pattern=[{'LOWER':'single',"POS":'ADJ'},{'POS':{'NOT_IN':['VERB','AUX','ADJ','PRON','ADV']}}]
  double_pattern=[{'LOWER':'double',"POS":'ADJ'},{'POS':{'NOT_IN':['VERB','AUX','ADJ','PRON','ADV']}}]
  triple_pattern=[{'LOWER':'triple',"POS":'ADJ'},{'POS':{'NOT_IN':['VERB','AUX','ADJ','PRON','ADV']}}]


  matcher.add("PatternMatching",[single_pattern,double_pattern,triple_pattern])  
  
  

  #adding the matcher to the document
  matches=matcher(doc)                

  temp_list_with_matcher=[]
  for string_hash_id,start_pos,end_pos in matches:
    string_id=nlp.vocab.strings[string_hash_id]
    #print("string hash_id",string_id)
    span=doc[start_pos:end_pos]
    #taking the token and its next token to repeat those many number of times.
    temp_list_with_matcher.append([start_pos,end_pos,span.text])
  #print(temp_list_with_matcher)
  temp_list_with_matcher_end=[]
  for i in range(len(temp_list_with_matcher)):
    start=temp_list_with_matcher[i][0]
    end=temp_list_with_matcher[i][1]
    string=str(temp_list_with_matcher[i][2]).split()
    if string[0]=="double":
      temp_text[end-1]=2*temp_text[end-1]
    elif string[0]=="triple":
      temp_text[end-1]=3*temp_text[end-1]
    else:
      temp_text=temp_text
  temp_text=' '.join(temp_text) 
  return temp_text


def parseMoneyWeights(sentence):
  nlp=spacy.load("en_core_web_sm")
  doc=nlp(sentence)
  currency=("dollars","dollar","euro","euros","rupee","rupees")
  quantity=("pounds","kilograms","grams")
  money,number,quantity=[],[],[]
  for i in doc.ents:
    if i.label_ =="MONEY":
      money.append(str(i))
    elif i.label=="CARDINAL": #check for number
      number.append(str(i))
    elif i.label=="QUANTIYY":
      quantity.append(str(i))
  temp_money,temp_number,temp_quantity=[],[],[]
  for i in money:
    i=i.lower().split()
    j=' '.join([k for k in i if k in currency])
    if j in 'dollar' or j in "dollars": 
      currency_symbol="$"
    elif j in "euro" or j in "euros":
      currency_symbol=u"\u20ac35"
    elif j in 'rupee' or j in "rupees":
      currency_symbol=u"\u20B9"
    else:
      currency_symbol=""
    i=[a for a in i if a not in currency]
    i=' '.join(i)
    temp_money.append(currency_symbol+str(w2n.word_to_num(i)))
  #parsing number
  for i in number:
        temp_number.append(str(w2n.word_to_num(i)))
  #parsing  quantity
  for i in  quantity:
    i=i.lower()
    i=i.split()
    j=[k for k in i if k in quantity]
    j=' '.join(j)
    if j in "pound" or j in "pounds":
       quantity_symbol=" lbs"
    elif j in "kilogram" or j in "kilograms":
       quantity_symbol="kgs"
    elif j in "gram" or j in "grams":
       quantity_symbol="gms"
    else:
       quantity_symbol=""
    i=[a for a in i if a not in quantity]
    i=' '.join(i)
    temp_quantity.append(str(str(w2n.word_to_num(a))+quantity_symbol))
  
  
  j=0
  temp_str= []
  for token in doc:
    if token.ent_iob_ =='B' and token.ent_type_ =='QUANTITY':
          temp_str.append(str(temp_quantity[j]))
          j=j+1
    elif token.ent_iob_ =='I' and token.ent_type_ =='QUANTITY':
          temp_str=temp_str
    else:
          temp_str.append(str(token))
        
  res=' '.join(temp_str)

    
  doc=nlp(res)

  k=0
  result=[]
  for token in doc:
    if token.ent_iob_ =='B' and token.ent_type_ =='MONEY':
        result.append(str(temp_money[k]))
        k=k+1
    elif token.ent_iob_ =='I' and token.ent_type_ =='MONEY':
        result=result
    else:
        result.append(str(token))
        
  result=' '.join(result)
  return result

if __name__=="__main__":
  text="C M has spent hundred thousand dollars."
  text2="This is triple A and this is double B try to repeat it "
  parsedRepeatedSentence=parseRepeatedItems(text2)
  final_result=parseMoneyWeights(parsedRepeatedSentence)
  print(final_result)
