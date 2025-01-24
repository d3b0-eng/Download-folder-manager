import shutil
import os
import time

download_path = r"C:\Users\vboxuser\Downloads"
desktop_path = r"C:\Users\vboxuser\Desktop"

def unique_filename(destination_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    newfilename = filename

    while os.path.exists(os.path.join(destination_folder, newfilename)):
        newfilename = f"{base}({counter}){ext}"
        counter += 1

    return newfilename

try:
    if not os.path.exists(f"{desktop_path}\\audio"):
        os.mkdir(r"C:\Users\vboxuser\Desktop\audio")

    if not os.path.exists(f"{desktop_path}\\video"):
        os.mkdir(r"C:\Users\vboxuser\Desktop\video")

    if not os.path.exists(f"{desktop_path}\\images"):
        os.mkdir(r"C:\Users\vboxuser\Desktop\images")

    if not os.path.exists(f"{desktop_path}\\pdf"):
        os.mkdir(r"C:\Users\vboxuser\Desktop\pdf")

    if not os.path.exists(f"{desktop_path}\\other"):
        os.mkdir(r"C:\Users\vboxuser\Desktop\other")

except Exception as e:
    print(e)

audio = f"{desktop_path}\\audio"
video = f"{desktop_path}\\video"
images = f"{desktop_path}\\images"
pdf = f"{desktop_path}\\pdf"
other = f"{desktop_path}\\other"

while True:
    for files in os.listdir(download_path):
            file_name = files
            file_path = f'{download_path}\\{file_name}'

            if file_path.endswith('.mp3'):    
                dest_path = audio
            elif files.endswith('.mp4'):
                dest_path = video
            elif files.endswith('.pdf'):
                dest_path = pdf
            elif files.endswith(('.jpg', '.png','.jpeg')):
                dest_path = images
            else:
                dest_path = other

            unique_name = unique_filename(dest_path, file_name)
            shutil.move(file_path, os.path.join(dest_path, unique_name))

    time.sleep(5)

