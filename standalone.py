NotYetUwUed=input("What word do youwu want towo uwu-ize? ")
UwUed=""

def UwUizer(uwu):
    uwu = uwu.replace("man.", "boyfriend.")
    uwu = uwu.replace(" man", " boyfriend") #... uwu
    uwu = uwu.replace("iend", "end")
    uwu = uwu.replace(".", ". uwu") # an UwU after every sentence
    uwu = uwu.replace("?", "? >~<") # a hiding cute >~< after every question
    uwu = uwu.replace("!", "! ÒwÓ")
    uwu = uwu.replace("r", "w") # Replace hard r's with weak w's!(๑•̀ㅁ•́๑)
    uwu = uwu.replace("v", "w")
    uwu = uwu.replace("awe", "awwe") # Replace are with awwe UwU
    uwu = uwu.replace("na", "nya") # Replace na with nya
    uwu = uwu.replace("l", "w")
    uwu = uwu.replace("think", "thinky-winky")
    uwu = uwu.replace("sly", "swy") # Obviouswy!
    uwu = uwu.replace("am ", "iz ") # I iz UwU
    uwu = uwu.replace("gay", "gei")
    uwu = uwu.replace("howd", "hold") # Hold may stay
    if (uwu[-1] == 'Ó'):
        uwu += ''
    elif (uwu[-1] == '<'):
        uwu += ''
    else:
        uwu += ' uwu~'
    return uwu
    

if __name__ == '__main__':
    UwUed = UwUizer(NotYetUwUed)
    print(UwUed)