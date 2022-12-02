from pydub import AudioSegment



lst = ["sounds/par6/1_2.wav", "sounds/par6/1_3.wav"]

i = 2
while(i != 6):
    j = 1
    while(j != 4):
        name = f"sounds/par6/{i}_{j}.wav"
        lst.append(name)
        j += 1
    i += 1 
i = 6
j = 1    
lst.append(f"sounds/par6/{i}_{j}.wav")       
for audio in lst:
    print(audio)

helper_ = AudioSegment.from_file("sounds/par6/1_1.wav", format="wav")
helper_.export("sounds/par6/1_1.mp3", format="mp3")

merge_ = AudioSegment.from_file("sounds/par6/1_1.wav", format="wav")
for audio in lst:
    print(audio)
    sound = AudioSegment.from_file(audio, format="wav")
    merge_ += sound
merge_.export("sounds/par6/merged.mp3", format="mp3")
