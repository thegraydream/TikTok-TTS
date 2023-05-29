# Import
import os
import json
import base64
import re
try:import requests
except:
     os.system('pip install requests')
     os.system('cls')

# Colors
cyan = "\033[0;36m"
green = "\033[0;32m"
red = "\033[0;31m"
reset = "\033[0m"

# Default Config Data
config_default = """{
    "export_path": "audio/",
    "voice": "en_us_001"
}"""


def texttotiktoktts(text):
     open('version', 'w', encoding='utf-8').write('1.0.0')
     if not requests.get('https://raw.githubusercontent.com/thegraydream/TikTok-TTS/master/version').text.strip() == open('version', 'r', encoding='utf-8').read():
          print(f'{red}You are not using the latest version of TikTok TTS, please update it on "https://github.com/thegraydream/TikTok-TTS".{reset}')
     if not os.path.exists('config.json'):open('config.json', 'w', encoding='utf-8').write(config_default) # Create config.json

     configdata = open('config.json', 'r', encoding='utf-8').read() # Read config.json
        
     exportpath = json.loads(configdata)["export_path"] # Get export path
     voice = json.loads(configdata)["voice"] # Get voice 

     response = requests.post('https://tiktok-tts.weilnet.workers.dev/api/generation', # TikTok API Voice Generation
                              json={"text":text,"voice":voice}) # Data

     jsondata = json.loads(response.text) # Get response Json Data       
     error = jsondata["error"] # Get error data

     if error == None:
          audio_base64 = jsondata["data"] # Get audio in base64

          text = re.sub(r"[^a-zA-Z0-9]+", "", text) # Filter Export name
          if len(text) > 61:text = text[61:] # Export name

          audio_data = base64.b64decode(audio_base64) # Decode in Base64

          if not os.path.exists(exportpath):os.makedirs(exportpath, exist_ok=True) # Create export folder
          with open(f'{exportpath}{text}.mp3', "wb") as file:
             file.write(audio_data) # Write audio in mp3
          print(f'{green}the {reset}"{text}"{green} audio file has been exported to {reset}"{exportpath}{text}"{green}.{reset}')
     else:print(f'{red}{error}')

while True:
     texttotiktoktts(input(f'{cyan}Enter your text > {reset}'))