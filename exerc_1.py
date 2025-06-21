#Here we are importing text to speech converter in python --pip install pyttsx3
#A text-to-speech conversion library in Python that allows the program to speak text out loud.
import pyttsx3
#Here we are importing datetime library in python --predifined library
#Provides classes for manipulating dates and times. Used here to get the current date and time.
import datetime
#Here we are importing speech recognition library in python --pip install SpeechRecognition
#Recognizes and converts spoken language into text using various speech recognition services.
import speech_recognition as sr
# Description: This file contains the code to interact with the Eden AI API to get the response from the chatbot.
#Parses JSON data, which is used for handling responses from API
import json
# Description: This file contain requests sent in to server --pip install requests
# Sends HTTP requests to web services and APIs to fetch data, such as weather or news information.
import requests
#Parses HTML and XML documents, often used for web scraping, like extracting weather data from a web page.
#from bs4 import BeautifulSoup
#import os
from bs4 import BeautifulSoup
import pyjokes
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

# API keys and URLs
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZDgxZTA0NzAtNTBiMC00MWUyLWIzYWEtZGI4NDU5OGJhYmU5IiwidHlwZSI6ImFwaV90b2tlbiJ9.Am910GByB1wASU1Wx2zapWyP13cWUs9NxotB9UlHUsQ"
}
url = "https://api.edenai.run/v2/audio/text_to_speech_async"

# Payload for API requests
payload = {
    "providers": "openai",
    "text": "Hello, I need your help!",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "vasu"
}

responses = {
    "hello": ["Hi there!", "Hello! How can I assist you today?", "Greetings!"],
    "how are you": ["I'm just a bot, but I'm doing great! How can I help you?", "I'm fine, thank you! How about you?"],
    "what is your name": ["I'm a friendly chatbot created to assist you.", "You can call me alexa!"],
    "thank you": ["You're welcome!, Happy to help!", "No problem!"], # type: ignore
    "what can you do": ["I can chat with you, provide news updates, weather forecasts, and more! Just ask me anything."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "I told my wife she was drawing her eyebrows too high. She looked surprised!"],
    "capital of india":["the capital of india is new delhi"],
    "technology":[" technology is the application of scientific knowledge for practical purposes or applications. Technology uses scientific principles, and applies them to change the environment in which humans live. Technology can also use scientific principles to advance industry or other human constructions."],
    "world war 1":["World War I or the First World War, also known as the Great War, was a global conflict between two coalitions: the Allies and the Central Powers.",],
    "world war 2":["World War II or the Second World War was a global conflict between two coalitions: the Allies and the Axis powers"],
    "cold war":["The Cold War was a period of geopolitical tension between the United States and the Soviet Union and their respective allies, the Western Bloc and the Eastern Bloc, that started in 1947, two years after the end of World War II, and lasted until the fall of the Soviet Union in 1991."],
    "independent india":["The Indian Independence Movement was a series of historic events in South Asia with the ultimate aim of ending British colonial rule. It lasted until 1947, when the Indian Independence Act 1947 was passed. The first nationalistic movement for Indian independence emerged in the Province of Bengal."],
    "life":["the period between birth and death, or the experience or state of being alive: Life's too short to worry about money!"],
    "artificial intelligence":["Artificial intelligence is the science of making machines that can think like humans. It can do things that are considered , AI technology can process large amounts of data in ways, unlike humans. The goal for AI is to be able to do things such as recognize patterns, make decisions and judge like humans."],
    "robotics":["Robotics is the intersection of science, engineering and technology that produces machines, called robots, that replicate or substitute for human actions."],
    "cyber security":["Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information; extorting money from users through ransomware; or interrupting normal business processes."],
    "ml":[" ml is nothing but machine learning.Machine learning (ML) is a field of artificial intelligence (AI) that enables machines to learn and improve from data without explicit instructions. ML uses algorithms to analyze large amounts of data, identify patterns, and make decisions. "],
    "cloud computing":["Cloud computing is the on-demand availability of computing resources (such as storage and infrastructure), as services over the internet. It eliminates the need for individuals and businesses to self-manage physical resources themselves, and only pay for what they use."],
    
    "flu":["The first symptom is a fever between 102°F (39°C) and 106°F (41°C). An adult often has a lower fever than a child. Other common symptoms include: Body aches."],
    "healthy diet":["Healthy movement may include walking, sports, dancing, yoga, running or other activities you enjoy. Eat a well-balanced, low-fat diet with lots of fruits, vegetables and whole grains. Choose a diet that's low in saturated fat and cholesterol, and moderate in sugar, salt and total fat."],
    "cold":["a stuffy, runny nose, scratchy, tickly throat, sneezing, watery eyes and a low-grade fever. Treatment to reduce symptoms includes getting rest and drinking plenty of fluids. Because colds are caused by viruses, treatment with antibiotics won't work."],
    "fever":["Fever is a rise in body temperature above the normal temperature, usually caused by infection. Normal body temperature is around 37°C (give or take a degree, but this can vary from person to person). There may also be minor fluctuations over the course of the day and night."],
    "chess":["Good chess strategy is playing each piece one time to its best square, developing them all in turn, and getting your chess pieces off the starting squares. You want to get your pieces into the game rapidly, and posted where they can accomplish something - either aiding your attack or defense of the center."],
    "cricket":["Cricket is a bat-and-ball game played between two teams of 11 players on an oval field. The goal is to score more runs than the opposing team by hitting a ball bowled by the other team with a bat. The game has been played for centuries, with the first international match taking place in 1844. Cricket is similar to baseball and uses some of the same terms, such as innings, umpire, and pitch"],
    "kho kho":["Kho kho is a traditional South Asian sport that dates to ancient India.[1][2] It is the second-most popular traditional tag game in the Indian subcontinent after kabaddi.[3] Kho kho is played on a rectangular court with a central lane connecting two poles which are at either end of the court. During the game, nine players from the chasing team (attacking team) are on the field, with eight of them sitting (crouched) in the central lane, while three runners from the defending team run around the court and try to avoid being touched."],
    "kabaddi":["Kabaddi is basically a combative sport, with seven players on each side; played for a period of 40 minutes with a 5 minutes break (20-5-20). The core idea of the game is to score points by raiding into the opponent's court and touching as many defense players as possible without getting caught on a single breath."],
    ""
    "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def talktoai(query):
    payload["text"] = query
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = json.loads(response.text)
        generated_text = result.get('openai', {}).get('generated_text', 'Sorry, I did not get that.')
        speak(generated_text)
    except Exception as e:
        print("Say that again please.")
        speak("Say that again please.")
        return "None"

def wishme():
    speak("Hello, I am Vasu. How can I assist you today?")

def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak("Current time is " + t)
    print(t)
    
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_response(user_input):
    """Get a response based on user input."""
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that. Can you ask something else?"

def start_chatbot():
    """Start the chatbot interaction."""
    speak("Welcome to the ChatBot! Type 'bye' to exit.")
    print("ChatBot: Welcome to the ChatBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            speak("Goodbye! Have a great day!")
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")
        speak(response)



def date():
    now = datetime.datetime.now()
    speak("Today's date is " + now.strftime("%d %B %Y"))
    print(now)

def present_news():
    news_api_key = "7d062bd8dae34b70b2c8cbcd632d9281"
    base_url = f"http://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
    response = requests.get(base_url)
    news_data = response.json()
    headlines = [article['title'] for article in news_data['articles'][:5]]
    speak("Here are the top headlines from India:")
    for headline in headlines:
        speak(headline)
    print(headlines)

def present_temperature(city):
    weather_api_key = "b5d5226b574d4a1bafd163814241908"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    return temperature

def present_weather(tadepalligudem):
    url = f"https://www.google.com/search?q=weather+in+{tadepalligudem}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            location = soup.select('#wob_loc')[0].getText().strip()
            temperature = soup.select('#wob_tm')[0].getText().strip()
            weather_conditions = soup.select('#wob_dc')[0].getText().strip()
            return f"The temperature in {location} is {temperature}°C with {weather_conditions}."
            print(weather_conditions)
        except IndexError:
            return f"Sorry, I couldn't retrieve weather information for {city}."
    else:
        return "Sorry, there was a problem retrieving weather information."

def present_health():
    health_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.healthinfo.com/v1/{query}?apikey={health_api_key}"  # Replace with actual API endpoint
    
    response = requests.get(base_url)
    if response.status_code == 200:
        health_data = response.json()
        # Assume the response has a key 'info' that contains the health information
        info = health_data.get('info', 'Sorry, I couldn\'t retrieve health information.')
        speak(info)
        print(info)
    else:
        speak("Sorry, there was a problem retrieving health information.")
        print("Sorry, there was a problem retrieving health information.")

def present_history():
    history_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.history.com/v1/{query}?apikey={history_api_key}"  # Replace with actual API endpoint
    
    response = requests.get(base_url)
    if response.status_code == 200:
        history_data = response.json()
        # Assume the response has a key 'fact' that contains the historical information
        fact = history_data.get('fact', 'Sorry, I couldn\'t retrieve historical information.')
        speak(fact)
        print(fact)
    else:
        speak("Sorry, there was a problem retrieving historical information.")
        print("Sorry, there was a problem retrieving historical information.")
        
def present_education():
    education_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.example.com/v1/education?apiKey={education_api_key}&query={query}"  # Replace with actual API URL

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        education_data = response.json()
        topics = education_data.get('topics', [])

        if topics:
            speak(f"Here is some information on {query}:")
            for topic in topics[:3]:  # Limit to top 3 topics
                title = topic.get('title', 'No title')
                description = topic.get('description', 'No description available')
                speak(f"{title}: {description}")
        else:
            speak(f"No information found for {query}.")
        
        print(topics)
    except Exception as e:
        speak("Sorry, I couldn't retrieve educational information.")
        print("Sorry, I couldn't retrieve educational information.", e)
        
def travel(query):
    travel_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.example.com/v1/travel?apiKey={travel_api_key}&query={query}"  # Replace with actual API URL

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        travel_data = response.json()
        destinations = travel_data.get('destinations', [])
        
        if destinations:
            speak(f"Here are some travel suggestions for {query}:")
            for destination in destinations[:3]:  # Limit to top 3 destinations
                name = destination.get('name', 'No name')
                description = destination.get('description', 'No description available')
                speak(f"{name}: {description}")
        else:
            speak(f"No travel suggestions found for {query}.")
        
        print(destinations)
    except Exception as e:
        speak("Sorry, I couldn't retrieve travel information.")
        print("Sorry, I couldn't retrieve travel information.", e)

def present_food_info(query):
    food_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.example.com/v1/recipes/search?apiKey={food_api_key}&query={query}"  # Replace with actual API URL

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        food_data = response.json()
        recipes = food_data.get('recipes', [])
        
        if recipes:
            speak(f"Here are some recipes for {query}:")
            for recipe in recipes[:3]:  # Limit to top 3 recipes
                title = recipe.get('title', 'No title')
                description = recipe.get('description', 'No description available')
                speak(f"{title}: {description}")
        else:
            speak(f"No recipes found for {query}.")
        
        print(recipes)
    except Exception as e:
        speak("Sorry, I couldn't retrieve food information.")
        print("Sorry, I couldn't retrieve food information.", e)

def present_sports_info():
    sports_api_key = "04136562ffmsh745d6cb15dcdac6p10d84ajsn290019aff283"  # Replace with your actual API key
    base_url = f"https://api.example.com/v1/sports?apiKe{sports_api_key}"  # Replace with actual API URL

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        sports_data = response.json()
        sports_updates = [update['title'] for update in sports_data['updates'][:5]]  # Limit to top 5 updates
        speak("Here are the latest sports updates:")
        for update in sports_updates:
            speak(update)
        print(sports_updates)
    except Exception as e:
        speak("Sorry, I couldn't retrieve sports information.")
        print("Sorry, I couldn't retrieve sports information.", e)






def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-te')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not hear that.")
        speak("Sorry, I did not hear that.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        speak("Sorry, there was an issue with the speech recognition service.")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wishme()
    while True:
        query = take_command()

        if 'time' in query:
            time()
        elif 'chatbot' in query:
            start_chatbot()
        elif 'chat' in query:
            speak()
        elif 'date' in query:
            date()
        elif 'news' in query:
            present_news()
        elif 'music' in query:
            # You need to specify a file path for play_music()
            print("Play music function is not implemented yet.")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif 'sports' in query:
            present_sports_info()
        elif 'health' in query:
            present_health()
        elif 'travel' in query:
            travel()
        elif 'history' in query:
            present_history()
        elif 'food' in query:
            present_food_info()
        elif 'education' in query:
            present_education()
        
        elif 'temperature' in query:
            city = query.split("temperature in ")[-1]
            temperature = present_temperature(city)
            speak(f"The current temperature in {city} is {temperature}°C.")
            print(f"Current temperature in {city}: {temperature}°C")
        elif 'weather' in query:
            present_weather()
        
        elif 'exit' in query:
            speak("Thank you for using Sam. Have a nice day!")
            print("Restart the program to use again.")
            break
        else:
            talktoai(query) 