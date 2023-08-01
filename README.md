# Natural Language Chatbot with Rasa

![Rasa Logo](https://rasa.com/assets/img/hero.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project is a Natural Language Chatbot implemented in Python using the Rasa framework. Rasa is a powerful open-source conversational AI platform that allows developers to build intelligent chatbots and virtual assistants. The chatbot uses natural language processing (NLP) and machine learning techniques to understand and respond to user input, providing a more interactive and human-like conversational experience.

## Features

- **Natural Language Understanding (NLU)**: The chatbot is trained to understand and extract information from user messages using Rasa NLU, which employs machine learning models for intent recognition and entity extraction.

- **Natural Language Generation (NLG)**: The chatbot generates responses based on the user's input using Rasa NLG, which allows developers to create dynamic and context-aware responses.

- **Custom Actions**: The chatbot can execute custom actions, enabling it to interact with external services, databases, or APIs to perform specific tasks based on user requests.

- **Interactive Learning**: The chatbot can be improved through interactive learning, where developers can review and correct its responses, making it smarter over time.

- **Easy Integration**: The chatbot can be integrated with various messaging platforms like Facebook Messenger, Slack, or your own custom front-end.

## Prerequisites

Before running the chatbot, you'll need the following prerequisites:

- Python 3.6+
- pip package manager

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Michelalmeidasilva/daqui-ml.git
   cd chatbot
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install rasa
   ```

## Usage

1. Train the chatbot:

   ```
   rasa train
   ```

2. Start the chatbot server:

   ```
   rasa run -m models --endpoints endpoints.yml --port 5005 --credentials credentials.yml
   ```

3. Interact with the chatbot through the command line:

   ```
   rasa shell
   ```

   Or, you can integrate it with a messaging platform (e.g., Facebook Messenger, Slack) using Rasa's connector.

## Contributing

Contributions to this project are always welcome. If you find any issues or want to enhance the chatbot's functionality, feel free to create a pull request.
