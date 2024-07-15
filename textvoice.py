import pyttsx3 as pyxt

def textvoice(text):
    txt_speech=pyxt.init()

    txt_speech.say(text)

    txt_speech.runAndWait()


if __name__==textvoice:
    textvoice()

textvoice('Quackkkkkkkkkkkk')
