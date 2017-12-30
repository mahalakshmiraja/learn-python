def censor(word,rpl):
    word = word.split()
    result=[]
    for i in word:
        if i==rpl:
            result.append("*****")
        else:
            result.append(i)
    print(" ".join(map(str,result)))


censor("this hack is wack hack", "hack")