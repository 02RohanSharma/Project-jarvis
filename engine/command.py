import pyttsx3
import speech_recognition as sr
import eel
import time


# Convert Text to Speech using Pyttsx3
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)    # It is used to change voice {0,1}
    engine.setProperty('rate',150)              # speach speed
    eel.DisplayMessage(text)   
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait() 


# Taking commands from user using speech_recognition
def takecommand():
    r = sr.Recognizer()

    # Voice Listening
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,10,6)
    
    # voice recognition(voice to text)
    try:
        print('Recognizing..') 
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return ""
    
    return query.lower()


# Take all commands from user
@eel.expose
def allCommands(message=1):

    if message==1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)


    try:
      

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query :
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        flag = takecommand()    
                        sendMessage(flag, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    flag = ""
                    if "send message" in query:
                        flag = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                                        
                    whatsApp(contact_no, query, flag, name)

        else:
            from engine.features import chatBot
            chatBot(query)

    except:
        print("error!!")

    eel.ShowHood()
