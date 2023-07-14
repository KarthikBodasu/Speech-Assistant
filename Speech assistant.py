from speech_recognition import Microphone, Recognizer, RequestError, UnknownValueError
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import webbrowser  # module that allows access to web based documents

r = Recognizer()


def record_audio():
    with Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except UnknownValueError:  # unknownvalue error occurs if speech is not able to understand
            print('sorry,i did not get you')
        except RequestError:  # request error occurs when there is problem speechrecognition module
            print('speech service is not good')
        return voice_data


def speak(command,destl):
    say=gTTS(text=command,lang=destl,slow=False)
    say.save('say.mp3')
    playsound.playsound('say.mp3')
    os.remove('say.mp3')

def respond(voice_data):
    if 'print' in voice_data:
        print('say what you want to print')
        stat = record_audio()
        print('you said  ' + stat)
        speak('you spoke','en')
        speak(stat,'en')
    if 'search' in voice_data:
        print('what u want to search for')
        query = record_audio()
        url = 'https://google.com/search?q=' + query
        webbrowser.open(url)  # open makes the url  open in webrowser
        print('Here is what I found for ' + query)
        speak('here is what i found for u about','en')
        speak(query,'en')
    if 'tab' in voice_data:
        print('what u want to search for')
        query = record_audio()
        url = 'https://google.com/search?q=' + query
        webbrowser.open_new(url)  # open makes the url  open in webrowser
        print('Here is what I found for u in new google chrome tab about' + query)
        speak('here is what i found for u about in new google chrome tab','en')
        speak(query,'en')
    if 'location' in voice_data:
        print('which location you want to search for')
        location = record_audio()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is what I found for ' + location)
        speak('here is location you want','en')
        speak(location,'en')
    if 'translate' in voice_data:
        from textblob import TextBlob
        translator = Translator()
        print('say something to translate')
        voice_data = record_audio()
        word = TextBlob(voice_data)
        try:
            lang = word.detect_language()
            print('say destination language')
            destlang = record_audio()
            print('you want in ' + destlang)
            if 'Telugu' in destlang:
                print('1')
                destl = 'te'
            elif 'Tamil' in destlang:
                print('2')
                destl = 'ta'
            elif 'Hindi' in destlang:
                print('3')
                destl = 'hi'
            print(destl)
            translated = translator.translate(word, src=lang, dest=destl)
            print(destlang + 'translation of what you said is')
            print(translated.text)
            speak(translated.text,destl)
        except:
            print('error: please speak fluently')
    if 'backup' in voice_data:

        print('if u want to overwrite the file say write')  # write makes data to overwrite
        print('if u want to read the file say read')  # read  makes data to print only
        print('if u want to rewrite or add something to the file say append')  # append makes new data to add at end
        print('if u want to exit')
        # speak('if u want to overwrite the file say write if u want to read the file say read if u want to rewrite or add something to the file say append if u want to exit')
        voice_data = record_audio()
        print('you said' + voice_data)
        if 'read' in voice_data:
            file1 = open(r"C:\Users\karthik\Documents\money", "r")
            print('u have this in file')
            print(file1.read())
        if 'write' in voice_data:
            file1 = open(r"C:\Users\karthik\Documents\money", "w+")
            print('previously u have this in ur file')
            print(file1.read())
            print('say what u want to overwrite in this file')
            file1.write(record_audio)
            print('u now have this in file')
            print(file1.read())
        if 'append' in voice_data:
            file1 = open(r"C:\Users\karthik\Documents\money", "a+")
            print('previously u have this in ur file')
            print(file1.read())
            print('say what u want to overwrite in this file')
            file1.write(record_audio)
            print('u now have this in file')
            print(file1.read())

    if 'exit' in voice_data:
        print('exit')
        exit()


a = 1
while a:
    a = 0
    print('what you want to do ')
    print('if print what you said say print')
    print('if you want to search say search')
    print('if you want to search in new tab say tab')
    print('if you want to translate say translate')
    print('if u want to search location say location')
    print('if u want to implement in file say backup')
    print('if you want to exit say exit')
    voice_data = record_audio()
    respond(voice_data)
    a = int(input('if you want to try again enter 1/0 : '))
