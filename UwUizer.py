#!/usr/bin/env python3

# UwUizer.py
#
# Tuwn nowmie tekst intu teh gay shit nyaaa~
#
# Wwitten by TEH lgbt queen!!! uwu

NotYetUwUed="Placeholder text?"
UwUed=""

def UwUizer(uwu):
    uwu = uwu.replace("prettier", ";prettier")
    uwu = uwu.replace("your", ";your")
    uwu = uwu.replace("you", "chu")
    uwu = uwu.replace(";chur", "your")
    uwu = uwu.replace("very", ";very")
    uwu = uwu.replace("idiot", "Baka! >~<")
    uwu = uwu.replace("say", "sej")
    uwu = uwu.replace("ing", "in")
    uwu = uwu.replace("man.", "boyfriend.")
    uwu = uwu.replace(" man", " boyfriend") #... uwu
    uwu = uwu.replace("iend", "end")
    uwu = uwu.replace("v", "w")
    uwu = uwu.replace("lowe", "wuv")
    uwu = uwu.replace(".", ". uwu") # an UwU after every sentence
    uwu = uwu.replace("!;", ";! >~<") # Emotions
    uwu = uwu.replace("!a", ";! ÒwÓ")
    uwu = uwu.replace("!e", ";! (Ò﹏Ó ╬)")
    uwu = uwu.replace("!h", ";! ^_^")
    if(uwu.find(";!") == -1):
        uwu = uwu.replace("!", "! OWO")
    uwu = uwu.replace(";!", "!")
    uwu = uwu.replace("?", "? ówò")
    uwu = uwu.replace("r", "w") # Replace hard r's with weak w's!(๑•̀ㅁ•́๑)
    uwu = uwu.replace("awe", "awwe") # Replace are with awwe UwU
    uwu = uwu.replace("na", "nya") # Replace na with nya
    uwu = uwu.replace("l", "w")
    uwu = uwu.replace("think", "thinky-winky")
    uwu = uwu.replace("sly", "swy") # Obviouswy!
    uwu = uwu.replace(" am ", " iz ") # I iz UwU
    uwu = uwu.replace("gay", "gei")
    uwu = uwu.replace("howd", "hold") # Hold may stay
    uwu = uwu.replace("oo", "owo")
    uwu = uwu.replace("the", "teh")
    uwu = uwu.replace("nice", "nais")
    uwu = uwu.replace(";wewy", "vewwy")
    uwu = uwu.replace(";pwettiew", "pwettier")
    if (uwu[-1].upper() == 'Ó'):
        uwu += ''
    elif (uwu[-1].upper() == 'O'):
        uwu += ''
    elif (uwu[-1].upper() == 'Ò'):
        uwu += ''
    elif (uwu[-1] == '<'):
        uwu += ''
    elif (uwu[-1] == ')'):
        uwu += ''
    elif (uwu[-1] == 'u'):
        uwu += ''
    elif (uwu[-1] == '^'):
        uwu += ''
    else:
        uwu += ' uwu~'
    return uwu
    

if __name__ == '__main__':
    UwUed = UwUizer(NotYetUwUed.lower())
    print(UwUed)
