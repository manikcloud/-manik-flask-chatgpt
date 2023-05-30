# Manik-Flask-ChatGPT

## Introduction

This repository contains the code for "manik-flask-chatgpt", a chatbot application powered by OpenAI's GPT model. It's built using Python Flask for the backend and uses HTML/CSS/JavaScript for the front end.

## Objective

The objective of this project is to create an easy-to-use web interface for interacting with the OpenAI's GPT model. Users can enter their queries in a chat-like interface, and the model will generate a response that is displayed on the same interface.

## Prerequisites

To run this project, you need:

- Docker installed on your system.
- An OpenAI API key. You can get one from the [OpenAI website](https://beta.openai.com/).

## Features

- Interactive chat interface.
- Fast and responsive design.
- Dockerized for easy deployment.

## Setup & Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/varunmanik/manik-flask-chatgpt.git
    cd manik-flask-chatgpt
    ```

2. Pull the Docker image:
    ```bash
    docker pull varunmanik/manik-flask-chatgpt
    ```

3. Run the Docker image (replace `<OPENAI_API_KEY>` with your OpenAI API key):
    ```bash
    docker run -p 5000:5000 -e OPENAI_API_KEY=<OPENAI_API_KEY> varunmanik/manik-flask-chatgpt
    ```

4. Open your web browser and navigate to `http://localhost:5000` to start using the application.

## File Structure

- `app.py` - The main Flask application.
- `Dockerfile` - Docker configuration file.
- `requirements.txt` - Contains the Python dependencies for the project.
- `static/` - Contains static files like CSS and JavaScript.
- `templates/` - Contains HTML templates.

## Conclusion

This project offers a convenient way to interact with OpenAI's powerful GPT model. With its Dockerized setup, it is easy to deploy
