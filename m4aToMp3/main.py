from pydub import AudioSegment
import os
import asyncio

files = os.listdir()

def nameFilter (name):
    if name.endswith('m4a'):
        return True
    else:
        return False

audios = filter(nameFilter, files)

async def convert(file):
    try:
        print('Loading: ', file)
        m4a_audio = AudioSegment.from_file(file, format="m4a")
        export_name = file.split('.')[0]+".mp3"
        m4a_audio.export(export_name, format="mp3")
        await asyncio.sleep(2)
        os.remove(file)
        print("File converted: ", export_name)
    except:
        print('Error on file: ', file)
        os.remove(file)

async def main():
    for x in audios:
        await convert(x)


asyncio.run(main())
