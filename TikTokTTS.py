# ╭─────────────────────────── Import ───────────────────────────╮ #
import os
import json
import base64
import re
try:import requests
except:
     os.system('pip install requests')
     os.system('cls')
     import requests

# ╭─────────────────────────── Colors ───────────────────────────╮ #
cyan = "\033[0;36m"
green = "\033[0;32m"
red = "\033[0;31m"
reset = "\033[0m"

# ╭─────────────────────────── Config Data ───────────────────────────╮ #
config_default = """{
    "log": true,
    "version": true
}"""


if not os.path.exists('config.json'):open('config.json', 'w', encoding='utf-8').write(config_default) # Create config.json


configdata = json.loads(open('config.json', 'r', encoding='utf-8').read()) # Read config.json
try:log_statut = configdata["log"]  # Read log data
except:log_statut = True
try:version = configdata["version"]  # Read log data
except:version = True

# ╭─────────────────────────── Def Text to TikTok TTS ───────────────────────────╮ #
def texttotiktoktts(text, voice="en_us_001", path=""):
     # ╭─── Author ───╮ #
     try:
          if log_statut == True:print(f'{reset}[{green}-{reset}] TikTok TTS by TheGrayDream, need help or report a bug? https://dsc.gg/tgdgithub') # Log Print


          # ╭─── Check Version ───╮ #
          if version == True:
                open('version', 'w', encoding='utf-8').write('1.0.2')
                try:
                    if not requests.get('https://raw.githubusercontent.com/thegraydream/TikTok-TTS/master/version').text.strip() == open('version', 'r', encoding='utf-8').read():
                        print(f'{reset}[{red}>{reset}] {red}You are not using the latest version of TikTok TTS, please update it on "https://github.com/thegraydream/TikTok-TTS".{reset}')
                    
                        r = input('Would you like to download the latest version? (y/n) > ').strip()
                        if r == "y":
                            for dow in json.loads(requests.get(f'https://raw.githubusercontent.com/thegraydream/TikTok-TTS/master/update.json').text)["update"]:
                                print(f'{reset}[{green}>{reset}] {green}Downloading {dow}{reset}')
                                try:
                                    content = requests.get(f'https://raw.githubusercontent.com/thegraydream/TikTok-TTS/master/{dow}').text
                                    if content == "404: Not Found":print(f'{reset}[{red}>{reset}] {red} We cannot find the file {dow}')
                                    else:
                                        open(dow, 'w', encoding='utf-8').write(content)
                                except:
                                    print(f'{reset}[{red}<{reset}] {red} An error occurred while downloading the latest version of {dow}')
                                    return False, f'Update download error ({dow})'
                            return True, 'Update completed successfully, please restart program'
                except:return False, f'Update download error'





          # ╭─── Send a request to url ───╮ #
          print(f'{reset}[{green}>{reset}] {green}A request has been sent to https://tiktok-tts.weilnet.workers.dev/api/generation{reset}') # Log Print
          response = requests.post('https://tiktok-tts.weilnet.workers.dev/api/generation', # TikTok API Voice Generation
               json={"text":text,"voice":voice}) # Data
          if log_statut == True:print(f'{reset}[{green}<{reset}] {green}The request has been received{reset}') # Log Print


          # ╭─── Read Json ───╮ #
          jsondata = json.loads(response.text) # Get response Json Data       
          error = jsondata["error"] # Get error data

          # ╭─── Audio conversion ───╮ #
          if error == None:
               audio_base64 = jsondata["data"] # Get audio in base64

               text = re.sub(r"[^a-zA-Z0-9]+", "", text) # Filter Export name
               if len(text) > 61:text = text[61:] # Export name

               if log_statut == True:print(f'{reset}[{green}>{reset}] {green}convert audio base 64 to .mp3{reset}') # Log Print
               audio_data = base64.b64decode(audio_base64) # Decode in Base64
               if log_statut == True:print(f'{reset}[{green}<{reset}] {green}the audio has been converted to mp3{reset}') # Log Print

               # ╭─── Write Audio ───╮ #
               if not os.path.exists(path):os.makedirs(path, exist_ok=True) # Create export folder
               with open(f'{path}/{text}.mp3', "wb") as file:
                    file.write(audio_data) # Write audio in mp3
               if log_statut == True:print(f'{reset}[{green}+{reset}] {green}the "{text}" audio file has been exported to "{path}{text}".{reset}') # Log Print
               return True, path
          else:
               print(f'{reset}[{red}-{reset}]{red}{error}{reset}') # Log Print
               return False, error
     except:return False, "An error has occurred"


# ╭────────────── Required ──────────────╮╭───────── Optional ─────────╮ #
# ╭─ Function ─╮ ╭───── Text Speech ─────╮╭─ Voice ─╮   ╭──── Path ────╮ #
texttotiktoktts('text you want to speech', 'en_us_001', 'My/Speech/Path/')

# You can use this function anywhere with "from TikTokTTS import texttotiktoktts
