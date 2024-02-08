import re
import codecs
import itertools
import os
import shutil
import torch
import pathlib
from tqdm import tqdm
from pydub import AudioSegment


def delete_bad_sym(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
        c = re.sub("[\'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]", "", content)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(c)    


def lower_sym(fname):
    lst_big_alp = dump_strfile_in_lst('storage/helpers/alpA.txt', [])
    lst_lower_alp = dump_strfile_in_lst('storage/helpers/alp.txt', [])         
    for elem1, elem2 in zip(lst_big_alp, lst_low_alp):        
        replace_word(fname, elem1, elem2)                


def add_plus_and_textnum(fname):
    lst1 = dump_strfile_in_lst('storage/helpers/word.txt', [])
    lst2 = dump_strfile_in_lst('storage/helpers/word+.txt', [])               
    for elem1, elem2 in zip(lst1, lst2):
    
        # There is important spaces into the form: f" {elem1} "
        
        replace_word(fname, f" {elem1} ", f" {elem2} ") 


def dump_strfile_in_lst(filename, lst):
    filename = os.path.abspath(filename)
    with open(f'{filename}', 'r', encoding="utf-8") as file:
        for line in file:
            lst.append(line.rstrip()) 
    return lst        


def replace_word(fname, before, after):
    with open(fname, 'r', encoding="utf-8") as file :
        filedata = file.read()        
    filedata = filedata.replace(before, after)  
    with open(fname, 'w', encoding="utf-8") as file:
        file.write(filedata) 


def txt_to_parts(source_file, path_out_files, i_max, j_max):
    with open(source_file, "r", encoding="utf-8") as f:
    
        # Trough here i_max * j_max parts will created
    
        for i in range(i_max):
            for j in range(j_max):
                with open(f'{path_out_files}/text{i + 1}_{j + 1}.txt', "w", encoding="utf-8") as res:
                    res.write("\n<speak>\n")
                    c = '\n'
                    for k in range(750):
                        c = f.read(1)    
                        if (k > 700) and (c == '.'):
                            res.write(c)
                            break
                        else:
                            res.write(c)
                            if (c == '.') or (c == ' ' and k % 50 == 0):
                                res.write('\n')

                    c = f.read(1)
                    if c != ' ':
                        res.write(c)
                        for t in range(0, 100):
                            c = f.read(1)
                            if c == ' ':
                                break
                            res.write(c)
                                     
                    res.write("\n</speak>\n")


def TTS(name_file, model, path):
    with open(name_file, "r", encoding="utf-8") as file:
            ssml_sample = file.read()
            sample_rate = 48000
            speaker='xenia'
            print(ssml_sample)
            audio_paths = model.save_wav(ssml_text=ssml_sample,
                                        speaker=speaker,
                                        sample_rate=sample_rate, 
                                        audio_path=path)
                                        
                                        
def text_prepare(fname, outfiles, i_max):
    delete_bad_sym(fname)
    lower_sym(fname)
    
    replace_word(fname, ",", " <s></s> ")
    replace_word(fname, ".", " <p></p> ")
    replace_word(fname, ")", " ) ")
    add_plus_and_textnum(fname)
    txt_to_parts(fname, outfiles, i_max, 3)   
                                         

def count_chars(out_text):
    n = 0
    with open(out_text, 'r', encoding="utf-8") as f:
        while True:
            c = f.read(1)
            n += 1
            if not c:
                break
    return n    
        

def main(text_for_tts, name_audio_out):

    # Preparing files from and where data will processed

    f = text_for_tts
    fname = f"input_text/{f}"
    out_text = f"storage/file_input.txt"
    outfiles = r"storage/gen_audio/text"
  
    fname = os.path.abspath(fname)
    out_text = os.path.abspath(out_text)
    outfiles = os.path.abspath(outfiles)
 
    shutil.copyfile(fname, out_text)
    
    # Cutting the input text for chuncks that will OK processed by SILERO_models
    # NOTE: SILERO_models limits numbers of chars that can be TTS
    # If text is too big - there will exceptions. It's why we need to do chunks
    
    size_f = count_chars(out_text)   
    print(size_f)
    i_max = (int)(size_f / 2100) + 1
    print("imax = ", i_max)
    
    text_prepare(out_text, outfiles, i_max)
    
    # Setup the system to generate speech from text trough 'model.pt' - SILERO_TTS 

    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)
    
    # Generate speeches from chuncks that are i_max * 3 (3 selected from an experiment)

    for i in range(1, i_max + 1):
        for j in range(1, 4):
            path = rf"storage/gen_audio/sounds/{i}_{j}.wav"
            print(rf"sounds/{i}_{j}")
            TTS(rf'storage/gen_audio/text/text{i}_{j}.txt', model, path=path)
        
    # Merge and save generated speeches        

    path_ = "storage/gen_audio/sounds"
    lst = [f"{path_}/1_2.wav", f"{path_}/1_3.wav"]
   
    for i in range(2, i_max + 1):
        for j in range(1, 4):
            name = f"{path_}/{i}_{j}.wav"
            lst.append(name)
                
    for audio in lst:
        print(audio)

    merge_ = AudioSegment.from_file(rf"{path_}/1_1.wav", format="wav")
    for audio in lst:
        print(audio)
        sound = AudioSegment.from_file(audio, format="wav")
        merge_ += sound   

    out_audio = f"output_audio"
    out_audio = os.path.abspath(out_audio)
    merge_.export(f"{out_audio}/{name_audio_out}.mp3", format="mp3")


if __name__ == "__main__":

	file_text = 'input_text.txt'
	main(f'input_text.txt', file_text.replace(".txt", ""))
