from google.cloud import texttospeech
from google.cloud import storage
import os
import uuid

def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # Use uuid4 to generate a unique filename
    filename = f"text_{uuid.uuid4()}.mp3"

    # Save the audio content to a file in Google Cloud Storage
    public_url = save_audio_to_gcs(response.audio_content, filename)

    return public_url

def save_audio_to_gcs(audio_content, filename):
    """Save the audio content to a file in Google Cloud Storage"""
    # Your Google Cloud Storage bucket name
    bucket_name = os.environ.get('GCS_BUCKET_NAME')

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)

    blob.upload_from_string(audio_content)

    # Make the blob publicly viewable
    blob.make_public()

    return blob.public_url

