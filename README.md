
# Dyslexia-Friendly Reading Assistant

Dyslexia-friendly OCR app: Converts images to readable text and speech.

## Description

This application is designed to assist individuals with dyslexia by converting images of text into a more readable format and providing an audio version. It uses OpenAI's GPT-4 Vision for OCR (Optical Character Recognition) and the Text-to-Speech API for audio generation.

## Features

- Image to text conversion using GPT-4 Vision
- Dyslexia-friendly text formatting
- Text-to-speech conversion
- User-friendly interface using Gradio

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/dyslexia-friendly-reading-assistant.git
   cd dyslexia-friendly-reading-assistant
   ```

2. Install the required dependencies:
   ```
   pip install gradio openai
   ```

3. Replace the API key in the script:
   Open `app.py` and replace `"your_api_key_here"` with your actual OpenAI API key.

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open the provided Gradio interface URL in your web browser.

3. Upload an image containing text.

4. The app will process the image and display:
   - The extracted text in a dyslexia-friendly format
   - An audio player with the text-to-speech version of the content

## Important Notes

- This application uses a hardcoded API key for demonstration purposes. In a production environment, use secure methods to handle API keys.
- Ensure you comply with OpenAI's use-case policies when using this application.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/dyslexia-friendly-reading-assistant/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)



