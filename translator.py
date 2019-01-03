import epitran
import cgi

def word_return(c):
  #I'm adding asterisks after a word corresponding to how 'different' the English-language sound is from the actual authentic French phoneme
  #Should we have just a standard word return, with all the IPA? That way we just call the method once for each different language? 
	dict = {'a':'Pat', 'ɑ': 'raw', 'e':'stay**', 'ɛ':'best', 'aj':'eye', 'ə': 'duck', 'i': 'tea', 'y' : 'few****', 'œ': 'girl***', 'ɔ' : 'awe', 
          'ø': 'ugly', 'u' : 'too', 'o' : 'soak', 'ɑ̃': 'croissant', 'ɛ̃':'pan', 'œ̃' : 'uh-huh','ɔ̃':'bone***','ễ':'?????','b':'bear', 'd':'do',
          'f':'feast','ɡ':'gain','k':'keen', 'l':'lay', 'm':'moon', 'n':'noon','ɲ':'canyon','p':'pale','r':'rolled r? Like the roar of a lion????****',
          's':'sail','ʃ':'shoe', 't':'team', 'v':'veal', 'z':'zeal', 'ʒ':'measure','dʒ':'jam', 'ŋ':'camping', 'tʃ':'chair','j':'yes', 'w':'we',
          'ɥ':'wheat'}
	if (c in dict):
		print(c + ": " + dict[c])			#Note: check how to output result onto a site
    print "Content-type:text/html\r\n\r\n"
		print "<html>"
		print "<body>"
		print "<%s>" % (c + ":" + dict[c])
		print "</body>"
		print "</html>"

def frenchTranslation(inputWord):
	epi = epitran.Epitran('fra-Latn')
	newWord = (epi.transliterate(inputWord))
	print(newWord)
	#first_symbol = newWord[0]
	#print("The first symbol is:" + first_symbol)
  for ch in newWord:
  	word_return(ch)
  
  	#print ch

def germanTranslation(inputWord):
  epi = epitran.Epitran('deu-Latn')
  newWord = (epi.transliterate(inputWord))
  print(newWord)
  for ch in newWord:
  	word_return(ch)
    
if __name__ == "__main__":
	print "Content-type: text/html\n"
  form = cgi.FieldStorage()
	inputWord =  form.getvalue('word')
  language = form.getvalue('language')
  if language = 'french':
  	frenchTranslation(inputWord)
  if language = 'german':
  	germanTranslation(inputWord)
                      
              