# Weather Mood App

A small Tkinter app that displays current weather and a matching mood for a
city using the OpenWeather API.

## Setup

1. Install Python and the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

2. Set your OpenWeather API key in the environment:

   ```powershell
   $env:OPENWEATHER_API_KEY = "your-api-key"
   ```

3. Run the app:

   ```powershell
   python app.py
   ```

The API key is read from `OPENWEATHER_API_KEY` and should not be committed to
the repository.
