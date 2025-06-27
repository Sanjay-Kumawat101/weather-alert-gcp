import requests
import smtplib
from email.mime.text import MIMEText
from google.cloud import secretmanager

def get_secret(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    project_id = "daily-weather-alert-app"  
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def weather_alert(event, context):
    city = "Mumbai"
    api_key = get_secret("weather-api-key")
    email_password = get_secret("email-password")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    message = f"Weather in {city}: {weather}\nTemperature: {temp}°C"

    sender = "@gmail.com"
    receiver = "@gmail.com"

    msg = MIMEText(message)
    msg["Subject"] = f"Daily Weather Alert for {city}"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, email_password)
        server.send_message(msg)

    print("✅ Email sent successfully.")
