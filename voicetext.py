import speech_recognition as sr
import pyttsx3

# Initialize the recognizer class
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # Call and prepare recognizer class method to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                # listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                
                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print('Unknown error occured')

        
    return
    
def write_to_file(text):

    # Writes to the given file and if its not present creates the file with that name
    f=open('output_text.txt','a')
    f.write(text)
    f.write('\n')
    f.close()
    return

def voicetext():
    while(1):
        text=record_text()
        write_to_file(text)

        print('test')


if __name__==voicetext:
    voicetext()

voicetext()