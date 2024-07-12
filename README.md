<a name="readme-top"></a>
# 👨‍💻 Built with

<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" /><img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" /> 
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*q4EVSAndlvgFLyR6ncc4Bg.png" width="100" height="27.5" style="background-color:white"/>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> 
<img src="https://miro.medium.com/v2/resize:fit:1200/1*g2Biaf_hCIkrBsE1AU1Nsw.png" width="100" height="27.5" style="background-color:white"/>


<!-- ABOUT THE PROJECT -->
# ℹ️ About The Project

This project deploys Google Cloud Function with CI/CD pipeline.<br>
Function gather data from [OpenWeather API](https://openweathermap.org/api), which is used by Gemini 1.5 Pro to create a weather summary and post it on slack daily at 20:00 CET.

Weather Summary posted to Slack:<br>
&shy;<img src="https://github.com/PKuziola/weather_forecast/blob/main/images/image_4.png?raw=true"/>
&shy;<img src="https://github.com/PKuziola/weather_forecast/blob/main/images/image_3.png?raw=true"/>

# 🔑Setup

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Getting Started

```bash
# Clone the repository
$ git clone https://github.com/PKuziola/weather_forecast
# Navigate to the project folder
$ cd weather_forecast
# Remove the original remote repository
$ git remote remove origin
```
### OpenWeather API

Create an account on [OpenWeather API](https://openweathermap.org/api) <br>
After logging in head to My API Keys and you can find key here<br>
&shy;<img src="https://github.com/PKuziola/weather_forecast/blob/main/images/image_1.png?raw=true"/>

### Slack

Create an Slack application, you can do it [here](https://api.slack.com/apps)<br>
Later head to OAuth & Permissions <br>
You have to make sure that app is able to join and post on particular slack channel<br>
&shy;<img src="https://github.com/PKuziola/weather_forecast/blob/main/images/image_5.png?raw=true"/>

You also have to obtain OAuth Token.<br>
&shy;<img src="https://github.com/PKuziola/weather_forecast/blob/main/images/image_2.png?raw=true"/>

### Google Cloud

You have to create project and service account with correct permissions <br>
You can do that by going to IAM & Admin > Service Accounts <br>
Add functions below to your service account:<br>
- Cloud Functions Developer Role
- IAM Service Account User Role
- Pub/Sub Admin Role
- Project Editor

You also need to activate below APIs:<br>
 - Cloud Functions API
 - Cloud Scheduler API
 - Cloud Pub/Sub API

You also have to obtain a .json key, you need to copy it's contents to GCP_ACCOUNT_KEY variable.<br>
To do it open Service Account and navigate to key section, if there is no key you have to create one.

### GitHub Secrets

- API_KEY
- GCP_ACCOUNT_KEY
- SLACK_TOKEN

# 🌲 Project tree
```bash
.
├───images
│   ├── image_1.png
│   ├── image_2.png
│   ├── image_3.png
│   ├── image_4.png
│   └── image_5.png
├───.github/workflows
│   └── WeatherForecast.yml
├── .pre-commit-config.yaml
├── README.md
├── license.txt
├── main.py
└── requirements.txt 

```


<!-- LICENSE -->
# 📄 License

Distributed under the MIT License. See `LICENSE.txt` for more information.
