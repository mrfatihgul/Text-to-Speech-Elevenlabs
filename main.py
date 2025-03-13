import requests
import os
import dotenv

dotenv.load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

api_key = ELEVENLABS_API_KEY

voice_id = '21m00Tcm4TlvDq8ikWAM'

print('|----------------------------------------------------------|\n'
      '|Welcome. You can convert your inputs to audio files here. |\n'
      '|----------------------------------------------------------|')

text = input('Please write words that you want to convert to an audio file: ')

url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'

headers = {
    'Accept': 'audio/mpeg',
    'Content-Type': 'application/json',
    'xi-api-key': api_key
}

data = {
    'text': text,
    'voice_settings': {
        'stability': 0.75,
        'similarity_boost': 0.75
    }
}

print("|------------|\n"
      "|Loading...  |\n"
      "|------------|")

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    output_path = '/Users/fatih/Desktop/output.mp3'

    with open('ses.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    print('File created successfully and saved into output.mp3 \n'
          '---------------------------------------------------- \n'
          'Come again!\n'
          '----------------------------------------------------')
else:
    print(f'Request failed. Case code: {response.status_code}')
    print('Error:', response.text)
