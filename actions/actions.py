# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
class ActionRemindToWashHands(Action):
    def name(self):
        return "action_remind_to_wash_hands"

    def run(self, dispatcher, tracker, domain):
        # Remind the user to wash their hands
        dispatcher.utter_message(text="You need to wash your hands before attending to the patient.")
        return []
class ActionWashHands(Action):
    def name(self):
        return "action_wash_hands"

    def run(self, dispatcher, tracker, domain):
        # Assume the nurse confirms hand washing
        dispatcher.utter_message(text="Great! You have washed your hands.")
        return [SlotSet("hands_washed", True)]  # Mark the task as done

class ActionAttendPatient(Action):
    def name(self):
        return "action_attend_patient"

    def run(self, dispatcher, tracker, domain):
        # Check if hands have been washed before attending the patient
        hands_washed = tracker.get_slot("hands_washed")
        if hands_washed:
            dispatcher.utter_message(text="You can now attend to the patient.")
        else:
            dispatcher.utter_message(text="Please wash your hands before attending the patient.")
        return []

class ActionRemindToWashHands(Action):
    def name(self):
        return "action_remind_to_wash_hands"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="You need to wash your hands before attending to the patient.")
        return []
    
class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the location or GPE entity from the user input
        location = next(tracker.get_latest_entity_values("location"), None)
        if location is None:
            location = next(tracker.get_latest_entity_values("GPE"), None)
        
        if not location:
            dispatcher.utter_message(text="Please provide a location to check the weather.")
            return []
        weather_api_key = "b4bf90dafb34ce2c795299cb74224f94"
        # Step 1: Get latitude and longitude from the city name
        geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={weather_api_key}'
        geocode_response = requests.get(geocoding_url)
        if geocode_response.status_code == 200 and len(geocode_response.json()) > 0:
            geocode_data = geocode_response.json()[0]
            lat = geocode_data['lat']
            lon = geocode_data['lon']
        # Step 2: Use the latitude and longitude to get weather data
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}"
            weather_response = requests.get(weather_url)
            if weather_response.status_code == 200:
                weather_data = weather_response.json()
              
                temperature = weather_data['main']['temp']
                condition = weather_data['weather'][0]['description']
                temperature_celsius = temperature - 273.15
                dispatcher.utter_message(text=f"The current temperature in {location} is {temperature_celsius:.2f}°C with {condition}.")
            
            else:
                dispatcher.utter_message(text="Sorry, I couldn't fetch the weather information. Please try again.")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find the location. Please try again.")
        return []
class ActionFeedback(Action):
    def name(self) -> str:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Check the feedback slot (true for affirm, false for deny)
        feedback = tracker.get_slot('feedback')
        
        if feedback is True:
            dispatcher.utter_message(text="Thank you for your positive feedback! I'm glad I could help.")
        elif feedback is False:
            dispatcher.utter_message(text="I'm sorry that I couldn't meet your expectations. Please share your feedback to help me improve.")
        
        return []
class ActionGreetName(Action):
    def name(self) -> str:
        return "action_greet_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Get the person's name from the slot
        person_name = tracker.get_slot('PERSON')
        
        if person_name:
            dispatcher.utter_message(text=f"Hello, {person_name}! How can I help you today?")
        else:
            dispatcher.utter_message(text="Hello! What's your name?")
        
        return []