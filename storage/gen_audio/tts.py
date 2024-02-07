# V3
import os
import torch
from tqdm import tqdm
# from tqdm.auto import tqdm  # notebook compatible
import time

def TTS(name_file, model):
    with open(name_file, "r", encoding="utf-8") as file:
            ssml_sample = file.read()
            sample_rate = 48000
            speaker='xenia'
            print(ssml_sample)
            audio_paths = model.save_wav(ssml_text=ssml_sample,
                                        speaker=speaker,
                                        sample_rate=sample_rate, 
                                        audio_path=path)

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)
i = 1
j = 1

while i != 5:
    j = 1
    while j != 4:
        path = f"sounds/{i}_{j}.wav"
        print(f"sounds/{i}_{j}")
        TTS(f'text/text{i}_{j}.txt', model)
        j += 1                                
    i += 1

i = 5
j = 1    
path = f"sounds/{i}_{j}.wav"
print(f"sounds/{i}_{j}")
TTS(f'text/text{i}_{j}.txt', model)

j = 2
path = f"sounds/{i}_{j}.wav"
print(f"sounds/{i}_{j}")
TTS(f'text/text{i}_{j}.txt', model)