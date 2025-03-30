import os
import shutil
import time

source = "C:/Users/bhargava/Downloads/"
dest = "D:/Bhargava/"

while True:
    files = os.listdir(source)

    for file in files:
        file_lower = file.lower()
        full_path = os.path.join(source, file)

        if 'edu' in file_lower:
            if 'doc' in file_lower:
                target = '00-Education/00-Documents'
            elif 'cert' in file_lower:
                target = '00-Education/01-Certificates'
            elif 'receipt' in file_lower:
                target = '00-Education/02-Fee_Receipts'
            elif 'stu' in file_lower:
                target = '00-Education/03-Study_Materials'
            else:
                target = '00-Education/99-Archives'

        elif 'offc' in file_lower:
            if 'doc' in file_lower:
                target = '02-Official/00-Documents'
            elif 'app' in file_lower:
                target = '02-Official/01-Applications'
            else:
                target = '02-Official/99-Archives'

        else:
            if file_lower.endswith(('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a')):
                target = '05-Media/00-Audio'
            elif file_lower.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                target = '05-Media/01-Photos'
            elif file_lower.endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg')):
                target = '05-Media/02-Videos'
            elif file_lower.endswith('.iso'):
                if 'os.iso' in file_lower:
                    target = '06-Disc_Images/00-OSes'
                elif 'sw.iso' in file_lower:
                    target = '06-Disc_Images/01-Softwares'
                else:
                    target = '06-Disc_Images/99-Archives'
            else:
                target = '99-Archives'

        destination = os.path.join(dest, target)
        final = os.path.join(destination, file)

        shutil.move(full_path, final)

    time.sleep(60)
