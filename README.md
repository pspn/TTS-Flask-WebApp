# TTS-Flask-WebApp
A web application built with Flask that converts user-input text to speech using Google Cloud Text-to-Speech API.

Sure, here is a basic README.md file template for your project. You can modify it according to your project's requirements.

# Text2Speech-WebApp

Text2Speech-WebApp is a simple Flask-based web application that converts user-input text to speech using Google Cloud Text-to-Speech API.

## Features

- Converts user-input text into speech
- Provides the speech as an MP3 file that can be played directly in the browser
- User authentication for added security

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/Text2Speech-WebApp.git
   ```

2. Navigate to the project directory:
   ```
   cd Text2Speech-WebApp
   ```

3. Create a virtual environment:
   ```
   python3 -m venv env
   ```

4. Activate the virtual environment:
   ```
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Set up environment variables. Replace `<secret-key>`, `<username>`, and `<password>` with your actual values:
   ```
   export SECRET_KEY=<secret-key>
   export USER_NAME=<username>
   export USER_PASS=<password>
   ```

7. Run the application:
   ```
   python app.py
   ```

## Usage

Go to `http://127.0.0.1:5000` in your browser. You'll be prompted to log in.

After logging in, you can enter text into the form and click "Convert to Speech". The converted text will be available as an MP3 file that you can play in your browser.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
