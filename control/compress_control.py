import os
import subprocess
import gzip
import shutil

class Control_Compress:
    def __init__(self):
        pass

    def compress_file(self, input_file, crf=23):
        _, extension = os.path.splitext(input_file)

        output_file = f"{os.path.splitext(input_file)[0]}-konpress{extension}"

        n = 1
        while os.path.exists(output_file):
            output_file = f"{os.path.splitext(input_file)[0]}-konpress-{n}{extension}"
            n += 1

        try:
            if extension.lower() in {".png", ".jpg", ".jpeg", ".gif"}:
                # Compression d'image avec ffmpeg
                ffmpeg_command = f"ffmpeg -i {input_file} -q:v {crf} {output_file}"
                subprocess.run(ffmpeg_command, shell=True, check=True)
            elif extension.lower() == ".mp4":
                # Compression de vidéo avec ffmpeg
                ffmpeg_command = f"ffmpeg -i {input_file} -c:v libx264 -crf {crf} -c:a aac -strict experimental {output_file}"
                subprocess.run(ffmpeg_command, shell=True, check=True)
            else:
                # Pour d'autres types de fichiers, utilisez gzip comme avant
                with open(input_file, 'rb') as f_in:
                    with gzip.open(output_file, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)

            print(f"Compression réussie. Fichier compressé enregistré sous {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la compression avec ffmpeg : {e}")
        except Exception as e:
            print(f"Erreur lors de la compression : {e}")
    # def compress_file(self, input_file):
    #
    #     _, extension = os.path.splitext(input_file)
    #
    #     output_file = f"{os.path.splitext(input_file)[0]}-konpress{extension}"
    #
    #     n = 1
    #     while os.path.exists(output_file):
    #         output_file = f"{os.path.splitext(input_file)[0]}-konpress-{n}{extension}"
    #         n += 1
    #
    #     try:
    #         with open(input_file, 'rb') as f_in:
    #             with gzip.open(output_file, 'wb') as f_out:
    #                 shutil.copyfileobj(f_in, f_out)
    #     except Exception as e:
    #         print(f"Error during compression: {e}")
