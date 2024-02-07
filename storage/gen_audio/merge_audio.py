from pydub import AudioSegment

path_ = r"src\\gen_audio\\sounds"
lst = [rf"{path_}\\1_2.wav", rf"{path_}\\1_3.wav"]
i = 2
while(i != 5):
    j = 1
    while(j != 4):
        name = f"{path_}\\{i}_{j}.wav"
        lst.append(name)
        j += 1
    i += 1  
i = 5
j = 1    
name = f"{path_}\\{i}_{j}.wav"
lst.append(name)   

i = 5
j = 2  
name = f"{path_}\\{i}_{j}.wav"
lst.append(name)
for audio in lst:
    print(audio)

merge_ = AudioSegment.from_file(f"{path_}\\1_1.wav", format="wav")
for audio in lst:
    print(audio)
    sound = AudioSegment.from_file(audio, format="wav")
    merge_ += sound   

merge_.export(f"{path_}\\20.mp3", format="mp3")
