import gradio as gr
import base64
from openai import OpenAI
from pathlib import Path
import tempfile

# Hardcoded API key (replace with your actual API key)
API_KEY = "sk-GeJ-zPXVgIGC2UIhA42dvW2g6lsc9SXjkHMsU9S5EgT3BlbkFJiG94ZfVUll-OgSkIivuBYEa3xGIErTL_u6DSQDUt4A"

def process_image(image_path):
    client = OpenAI(api_key=API_KEY)
    
    # Read the image file and encode to base64
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Use GPT-4 Vision to perform OCR
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an OCR system. Extract all text from the image and return it without any additional commentary."
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What text is in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    extracted_text = response.choices[0].message.content
    
    # Format text for dyslexia-friendly reading
    formatted_text = f"<p style='font-family: Arial, sans-serif; font-size: 18px; line-height: 1.5; font-weight: bold;'>{extracted_text}</p>"
    
    # Generate speech from text
    speech_file_path = Path(tempfile.gettempdir()) / "speech.mp3"
    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=extracted_text
    )
    speech_response.stream_to_file(speech_file_path)
    
    return formatted_text, str(speech_file_path)

# Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="filepath", label="Upload Image")
    ],
    outputs=[
        gr.HTML(label="Extracted and Formatted Text"),
        gr.Audio(label="Text-to-Speech")
    ],
    title="Dyslexia-Friendly Reading Assistant",
    description="Upload an image of text. The app will extract the text, format it for easier reading, and provide an audio version."
)

iface.launch()
