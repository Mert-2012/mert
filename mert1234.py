meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            'sigma': 'iyi bir lider',
            'ker':'eşşek'
            }
            
kelime= input('kelimeyi girin') 
if kelime in meme_dict.keys():
    print(meme_dict[kelime])
    
else:
   print('başka kelimeleri deneyin yok')
