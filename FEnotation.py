def get_fen(prev, curx):


    novih_praznih_mest = []
    pieces = []
    cur = ""
    p=0
    x=0
    counter = 1   

    for i in range(71):
        if prev[i].isalpha() == True and prev[i]!="/":
            p+=1
        if (curx[i] == "b" and curx[i]!="/") or (curx[i] == "w" and curx[i]!="/"):
            x+=1
        if prev[i]!="0" and curx[i]=="0":
            pieces.append(prev[i])
        if (prev[i] != "0" and curx[i]=="0"):
            novih_praznih_mest.append(i)




    if len(novih_praznih_mest)==1 and len(pieces) == 1 and p == x:
        for i in range(71):
            if prev[i] != "0" and curx[i] != "0":
                cur += prev[i]
            elif prev[i] != "0" and curx[i] == "0":
                cur+="0"
            elif prev[i] == "0" and curx[i] != "0":
                cur += pieces[0]
            elif prev[i] == "0" and curx[i] == "0":
                cur += prev[i]
            elif prev[i] == "/":
                cur+="/"


    elif len(novih_praznih_mest)==2:

        for i in range(71):
            if prev[i] != "0" and curx[i] != "0":
                cur += prev[i]
            elif prev[i] != "0" and curx[i] == "0":
                cur+="0"
            elif prev[i] == "0" and curx[i] != "0" and curx[0]=="0":
                
                cur += pieces[counter]
                counter-=1
            
            elif prev[i] == "0" and curx[i] != "0":
                
                cur += pieces[counter]
                counter-=1


            elif prev[i] == "0" and curx[i] == "0":
                cur += prev[i]
            elif prev[i] == "/":
                cur+="/"

    elif len(novih_praznih_mest) == 1 and p!=x:

        for i in range(71):
            if (prev[i].islower() ==  True and curx[i] == "b") or (prev[i].isupper() ==  True and curx[i] == "w"):
                cur += prev[i]
            elif prev[i] != "0" and curx[i] == "0":
                cur+="0"
            elif (prev[i].islower() ==  True and curx[i] == "w") or (prev[i].isupper() ==  True and curx[i] == "b"):
                cur += pieces[0]
            elif prev[i] == "0" and curx[i] == "0":
                cur += prev[i]
            elif prev[i] == "/":
                cur+="/"

    return cur