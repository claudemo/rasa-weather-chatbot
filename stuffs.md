# virutal env and setup

Here are the steps to recreate the virtual environment with Python 3.9:

1. **Deactivate the current virtual environment** (if active):
    ```sh
    deactivate
    ```

2. **Remove the existing virtual environment**:
    ```sh
    rm -rf /Users/mengyue/Desktop/24Fall/Jutly-24Fall-coop/2nd/venv-rasa/rasa_env
    ```

3. **Create a new virtual environment with Python 3.9**:
    ```sh
    virtualenv -p python3.9 /Users/mengyue/Desktop/24Fall/Jutly-24Fall-coop/2nd/venv-rasa/rasa_env
    ```

4. **Activate the new virtual environment**:
    ```sh
    source /Users/mengyue/Desktop/24Fall/Jutly-24Fall-coop/2nd/venv-rasa/rasa_env/bin/activate
    ```

5. **Install Rasa**:
    ```sh
    pip install rasa
    ```

6. **Run the Rasa server**:
    ```sh
    rasa run actions
    ```

If you don't have Python 3.9 installed, you can install it using Homebrew:

```sh
brew install python@3.9
```

Then, use the full path to the Python 3.9 executable when creating the virtual environment:

```sh
virtualenv -p /usr/local/bin/python3.9 /Users/mengyue/Desktop/24Fall/Jutly-24Fall-coop/2nd/venv-rasa/rasa_env
```

After following these steps, you should be able to install Rasa and run the server without issues.


rasa run -m models --enable-api

# Set up 
rasa run -m models --enable-api --port 5005


# Run
rasa run -m models --enable-api


# good reference/explanation 

[https://www.geeksforgeeks.org/chatbots-using-python-and-rasa/]
Rasa has two main components:

Rasa NLU (Natural Language Understanding): Rasa NLU is an open-source natural language processing tool for intent classification (decides what the user is asking), extraction of the entity from the bot in the form of structured data and helps the chatbot understand what user is saying.

Rasa Core: a chatbot framework with machine learning-based dialogue management which takes the structured input from the NLU and predicts the next best action using a probabilistic model like LSTM neural network rather than if/else statement. Underneath the hood,  it also uses reinforcement learning to improve the prediction of the next best action.

Let's break down the components of Rasa in terms of their input and output:

### Rasa NLU (Natural Language Understanding)

**Input:**
- **User Message:** A text message from the user, such as "What's the weather like today?" or "Book a flight to New York."

**Output:**
- **Intent:** The classification of the user's intent, such as `weather_query` or `book_flight`.
- **Entities:** Extracted pieces of information from the user's message, such as `location: New York` or `date: today`.

**Example:**
- **Input:** "Book a flight to New York for tomorrow."
- **Output:**
  - **Intent:** `book_flight`
  - **Entities:** `{"location": "New York", "date": "tomorrow"}`

### Rasa Core

**Input:**
- **Structured Input from NLU:** The intent and entities extracted by Rasa NLU.
- **Conversation History:** The history of the conversation so far, including previous user messages and bot responses.

**Output:**
- **Next Action:** The next action the bot should take, such as sending a response, asking a follow-up question, or executing a custom action.

**Example:**
- **Input:**
  - **Intent:** `book_flight`
  - **Entities:** `{"location": "New York", "date": "tomorrow"}`
  - **Conversation History:** Previous messages and actions in the conversation.
- **Output:**
  - **Next Action:** `utter_confirm_booking` (a response confirming the booking details)

### Summary

- **Rasa NLU** takes a raw user message as input and outputs structured data in the form of intents and entities.
- **Rasa Core** takes the structured data from Rasa NLU and the conversation history as input and outputs the next best action for the bot to take.

This combination allows Rasa to understand user inputs and manage conversations effectively, providing a more natural and intelligent chatbot experience.

# further steps to take
- connect to other platforms facebook, insta etc

# Chat Visualizaition
`rasa visualize`


# run Rasa Bot-
Make Sure you are using your conda env environment.
Navigate to project directory cd Rasa-Weather-Bot
Train your Rasa Nlu and core using 
    `rasa train`
Run your custom actions using Rasa SDK server. rasa run actions
In a seperate shell or terminal, run your rasa server. (Make sure you are within your conda env here as well.) 
`rasa run`
Your default rasa server will start on http://localhost:5005, and rasa action server on http://localhost:5055.


# error msgs
 
2024-09-12 16:56:31 ERROR    rasa.core.processor  - Encountered an exception while running action 'action_greet_name'.Bot will continue, but the actions events are lost. Please check the logs of your action server for more information.

### debug that it can not recongnize a city and fetch related info when user input a city name

# weather API
https://openweathermap.org/current


# command cheatsheet
https://rasa.com/docs/rasa/command-line-interface/
    