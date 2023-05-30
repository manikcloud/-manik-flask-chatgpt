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
2.1 Docker Build
If you make changes to the project and wish to build a new Docker image, you can do so using the docker build command. Here's how:

```
docker build -t your-username/manik-flask-chatgpt .
```
- Replace your-username with your Docker Hub username. After running this command, Docker will use the Dockerfile present in the current directory (.) to build the image. Once the image has been built, it can be run or pushed to Docker Hub.

3. Run the Docker image (replace `<OPENAI_API_KEY>` with your OpenAI API key):
    ```bash
    docker run -p 5000:5000 -e OPENAI_API_KEY=<OPENAI_API_KEY> varunmanik/manik-flask-chatgpt
    ```

4. Open your web browser and navigate to `http://localhost:5000` to start using the application.

## File Structure

- `app.py` - This is the main application file. It sets up the Flask application and defines the routes.
- `Dockerfile` - This file contains the instructions for Docker to build the image. It specifies the base image, the working directory, dependencies to install, the port the app should run on, and the command to launch the app.
- `requirements.txt` - This file lists the Python dependencies that need to be installed for the app to work.
- `static/` - This directory contains static files that the app uses. This includes CSS and JavaScript files.

- static/css/: This directory contains CSS files for styling the app. It includes style.css for general styles and prism.css for styling code blocks.

- static/js/: This directory contains JavaScript files. It includes script.js for handling chat interactions and prism.js for handling code block interactions
- `templates/` - This directory contains the `index.html` file, which is the main HTML template for the app. Flask uses this file to generate the web pages.

## Conclusion

This project offers a convenient way to interact with OpenAI's powerful GPT model. With its Dockerized setup, it is easy to deploy
