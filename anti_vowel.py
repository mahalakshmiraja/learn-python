def anti_vowel(text):
    lst = []
    text = text.lower()
    length = len(text)
    for i in range(length):
        if text[i]!="a" and text[i]!="e" and text[i]!="i" and text[i]!="o" and text[i]!="u":
            lst.append(text[i])
    print ("".join(map(str,lst)))
            
        
 
anti_vowel("welcome DAY")