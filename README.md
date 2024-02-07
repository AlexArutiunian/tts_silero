# Book reader

[<img src="img/Colab.webp" width=20%>](https://colab.research.google.com/drive/1YE611ZFXAytNXgGCFdTcHbeR6CDlKvAz?usp=drive_link#scrollTo=DeTmknN1gfDV)<br>

Click on the "colab" for launching my project in google colab.

In this repository is program 'book_reader.py' - it is text to speech in russian with [silero models](https://github.com/snakers4/silero-models).

In my opinion the best voice in russian is 'xenia'. So in my project I use it. 

## Necessary libraryes
```
pip install -r requirements.txt
```


```bash
pip3 install silero
pip3 install torch
pip3 install torchaudio
pip3 install tqdm
pip3 install sounddevice
```
If that is not enough, you can see [my list of library](https://github.com/AlexArutiunian/book_reader/blob/main/src/headers.txt) and check your list with command
```bash
pip3 list
```
### Some software to work with merged_audio
```bash
pip3 install pydub
```
If you have this error in windows
```bash
RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
```
then you can see this [tutorial](https://www.youtube.com/watch?v=PYeksH-n4fo&t=954s) and launch ffmpeg from [link](https://ffmpeg.org/download.html#build-windows)
## Correction of speech's errors of the model

In directory [book_reader/src/helpers](https://github.com/AlexArutiunian/book_reader/tree/main/src/helpers) you can find files 'word.txt' and 'word+.txt', with which you can place accents in words of your text.
Also you can correct of another speech errors of the model with the [guide](https://github.com/snakers4/silero-models/wiki/SSML) from developers of silero model.
