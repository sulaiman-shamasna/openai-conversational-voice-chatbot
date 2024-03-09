# OpenAI Conversational-Voice-Chatbot

Within this technical discourse, I embark on an exploration of OpenAI's
cutting-edge *text-to-speech (TTS)* and *speech-to-text (STT)* capabilities.
These innovations are not only revolutionizing the dynamics of human-machine
interaction but also unlocking novel avenues of accessibility and efficiency.
Whether you are a seasoned developer, a fervent tech enthusiast,
or simply curious about the forefront of AI advancements, this implementation
can be used as a prototype for more sophisticated projects leveraging TTS and STT 
functionalities.

## Usage
To use this app please follow the following steps:

- It's recommended to have **Python 3.10** or higher 
- Create a virtual environment and install requirements

    Navigate to the project directory, create a virtual environment using the command:
    ```py
    python -m venv env
    ```
    And activate it, using the command:
    ```py
    - source env/Scripts/activate   # for Windows in the git bash
    - source env/bin/activate       # for Linux and OSX
    ```
## Streamlit Usage
Having done the previous steps, it's time to chat. Follow the following steps, please.

1. create a **.env** file and paste there your *OPENAI_API_KEY*. The content of the **.env** should be identical to:
    ```py
    OPENAI_API_KEY=sk-xxxx
    ```
    which should be 51 character-long in total.


2. create a **.streamlit/secrets.toml** directory and paste there your *OPENAI_API_KEY*. The content of the **secrets.toml** should look like:
    ```py
    # .streamlit/secrets.toml

    [passwords]
    # Follow the rule: username = "password"
    username = "sk-xxxx"
    ```
    which should be 51 character-long in total. Also, the word *username* 
    can be changed, which represents the selected username to input the 
    streamlit app, along with the *OPENAI_API_KEY*.


3. Run the app using the command:
    ```py
    streamlit run app.py    #Or, to select a port, you can run the command
    stremalit run app.py --server.port=85XX
    ```

4. According to the settings, open a browser and the app should now be running on: 
    ```py
        http://localhost:85XX/          # or
        http://127.0.0.1:85XX/          
    ```
    Note even without specifying the IP and port in the app, these values will be set by default.

5. Enter your credentials:
    ```py
    username=username               # Use the string: username for that 
                                    # (defined in the script, can be adjusted)
    passward=YOUR_OPENAI_API_KEY    # Identical to that exists in the .env file
    ```
