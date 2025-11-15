# Codetech Internship Projects

This repository contains multiple projects completed as part of the Codetech internship program. Each project demonstrates capabilities in web development, API integration, chatbot development, and machine learning workflows.

## Projects Overview

### api_visualization/
- **Description:** Fetches weather forecast data using the OpenWeatherMap API and visualizes temperature over time using Matplotlib.
- **How to Run:**
  1. Activate virtual environment.
  2. Install dependencies: `pip install -r requirements.txt`
  3. Set environment variable for OpenWeather API key: `OPENWEATHER_API_KEY="your_key"`
  4. Run: `python fetch_and_visualize.py [city_name]`
  
### chatbot_project/
- **Description:** Interactive console-based chatbot with menu-driven commands and simple responses.
- **How to Run:**
  1. Activate virtual environment.
  2. Run: `python chatbot.py`
  3. Choose commands by input numbers to interact.

### ml_model_project/
- **Description:** Machine Learning project to train a Random Forest model on Iris dataset and interactively predict flower species.
- **How to Run:**
  1. Activate virtual environment.
  2. Install dependencies: `pip install -r requirements.txt`
  3. Train model: `python train_model.py`
  4. Predict interactively: `python predict.py`

## General Setup

- Use Python 3.8 or higher.
- Create and activate virtual environments individually within each project folder.
- Ensure proper API keys where needed.
