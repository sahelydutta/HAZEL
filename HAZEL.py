import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import random
import requests
import sys

# pyttsx3 use to convert text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # Speak function
    engine.say(audio)
    engine.runAndWait()

#this function use for wish me
def wishMe():
    # Greet the user based on the time of day
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hey sweety, good morning!")
    elif 12 <= hour < 18:
        speak("Lazy wazy, good noon to you dear!")
    else:
        speak("Good evening sahely!")
    speak("I am Hazel. Tell me, how can I help you?")


# Listen to user's voice command and convert it to text sr recognizer
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing you...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("try hearing you...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print("Could you say that one more time, please?")
        return "None"

#can be send mail any internet machine with an SMTP
def sendEmail(to, content):
    # Set up your email credentials and server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your email like mine abcd2@gmail.com"
    sender_password = "your pw like 12345"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
    except Exception as e:
        print(e)
        speak("Sorry, I was unable to send the email.")

# Its make calls using appropriate libraries or APIs
def callPerson():
    
    speak("Whom do you want to call?")


def calculate(expression):
    try:
        # Replace words with operators
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("multiply", "*")
        expression = expression.replace("divide", "/")

        result = eval(expression)
        speak(f"The result of {expression} is {result}")
        print(f"The result of {expression} is {result}")
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")

#get you a weather report
def getWeatherReport():
    api_key = "2200990002888966000222"  #weather api key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query

        except Exception as e:
            print("Could you say that one more time, please?")
            return "None"

    speak("Please provide your location.")
    location = takeCommand()

    url = f"{base_url}q={location}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        temperature = temperature - 273.15

        speak(f"The weather in {location} is {weather}. The temperature is {temperature:.2f} degrees Celsius with {humidity}% humidity.")
    else:
        speak("Sorry, I couldn't fetch the weather report for your location.")

#suggest recipes in the list
def suggestRecipe():
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query

        except Exception as e:
            print("Could you say that one more time, please?")
            return "None"

    recipes = [
        "Butter Chicken",
        "Chicken Tikka Masala",
        "Palak Paneer",
        "Mushroom Roast",
        "Gulab Jamun",
        "Rosogolla",
        "Homemade Pizza",
        "Biriyani",
        "Red Velvet Cake",
        "Apple Oats"
    ]

    recipe = random.choice(recipes)
    speak("Here is a recipe suggestion for you:")
    speak(recipe)

#suggest spiritual quotes from bhagavad gita
def getSpiritualQuote():
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query

        except Exception as e:
            print("Could you say that one more time, please?")
            return "None"

    quotes = [
        "whatever happened, happened for the good - Bhagavad Gita."
        "change is the laws of the universe. you can be a millionire, or a pauper in an instant - Bhagavad Gita ."
        "man is made by his belief, as he belives , so he is - Bhagavad Gita."
        "even the wise are confused about what is action and what is in action - Bhagavad Gita."
        "you are what you belive in. you become that which you belive you can become - Bhagavad Gita."
    ]
    
        

    quote = random.choice(quotes)
    speak("Here is a spiritual quote for you:")
    speak(quote)

#daily health tips
def getDailyHealthTips():
    tips = [
        "Stay hydrated: Drink an adequate amount of water throughout the day to keep your body hydrated.",
        "Eat a balanced diet: Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your meals.",
        "Engage in regular physical activity: Incorporate exercise into your daily routine, whether it's walking, jogging, yoga, or any other activity you enjoy.",
        "Get enough sleep: Prioritize quality sleep by maintaining a consistent sleep schedule. Aim for 7-8 hours of sleep each night to allow your body to rest and recover.",
        "Practice stress management: Find healthy ways to manage stress, such as meditation, deep breathing exercises, or engaging in activities you find relaxing."
    ]

    tip = random.choice(tips)
    speak("Here is your daily health tip:")
    speak(tip)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #for query the time
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
         
        #for query wikipedia
        elif'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #for open application in your laptop
        elif 'hazel open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'hazel open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'hazel open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'hazel open threads' in query:
            webbrowser.open("https://www.threads.com")

        elif 'hazel play music' in query:
            music_dir = 'C:\\Users\\SAHELY\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'start' in query:
            pyautogui.hotkey('win', 's')

        elif 'open vs code' in query:
            codePath = "C:\\Users\\SAHELY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to sahely' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sahelydutta2@gmail.com"
                sendEmail(to, content)
                speak("Okay, email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was unable to send the email.")

        elif 'daily health tips' in query:
            getDailyHealthTips()

        elif 'spiritual quote' in query:
            getSpiritualQuote()

        elif 'suggest recipe' in query:
            suggestRecipe()

        elif 'call' in query:
            callPerson()

        elif 'calculate' in query:
            expression = query.replace("calculate", "")
            calculate(expression)

        elif 'weather report' in query:
            getWeatherReport()
# for turn it off
        elif 'turn off' in query or 'exit' in query:
            speak("Goodbye! Have a nice day, Sahely!")
            sys.exit()
