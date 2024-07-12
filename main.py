import json
import os
import time
from datetime import datetime
from pathlib import Path

import requests
import vertexai
from dotenv import load_dotenv
from google.auth import default
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from slack_sdk import WebClient
from vertexai.generative_models import GenerationConfig, GenerativeModel

REGION = 'us-central1'
MODEL_VERSION = "gemini-1.5-pro-preview-0409"
API_KEY = os.getenv('API_KEY')
URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data():

    params = {
        'q': 'Warsaw',
        'appid': API_KEY,
        'lang': 'pl',
        'units': 'metric'
    }

    response = requests.get(URL, params=params).json()

    return response

def generate_prompt(response):

    prompt = f"""
    Stwórz krótki opis pogody na podstawie pliku json {response}
    Uwzględnij informacje takie jak:
    - miasto, państwo
    - temperatura
    - temperatura odczuwalna
    - prędkość wiatru
    - opis pogody (pochmurnie, deszczowo etc)
    - ciśnienie
    - wilgotność
    Dodaj emoji, wykorzystaj te daty, podawaj tylko godzinę i minutę:
    - wschód słońca = {datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])}
    - zachód słońca = {datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])}
    Nagłowek ma być w formacie: Miasto Emoji Flaga Kraju - {datetime.today().strftime('%Y-%m-%d')} i ma być zakończony i poprzedzony symbolem *
    """

    vertexai.init(location=REGION)

    model = GenerativeModel(model_name=MODEL_VERSION)

    config = GenerationConfig(
        max_output_tokens=5000, temperature=0.4, top_p=1, top_k=32
    )

    response = model.generate_content(
        prompt, generation_config=config
    )

    return response

def post_to_slack(response):

    slack_token = os.getenv('SLACK_TOKEN')
    client = WebClient(token=slack_token)

    client.chat_postMessage(channel='#python-project', text=response.text)


def generate_weather_summary(event, context):
    response = get_weather_data()
    response =  generate_prompt(response)
    post_to_slack(response)
    return 'Weather summary generated and posted to Slack successfully.', 200
