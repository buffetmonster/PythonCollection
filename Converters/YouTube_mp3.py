from pytube import YouTube
from pytube import extract
import re
#url = "https://www.youtube.com/watch?v=ZTrrc6Ni5eM"
#Gimme! Gimme! Gimme! (ABBA); Cover by Beatrice Florea
#url = "https://www.youtube.com/watch?v=k2YJIseoB-k"
#Stayin' Alive - Bee Gees; Cover by Beatrice Florea
#url = "https://www.youtube.com/watch?v=TMYF0c79i_s"
#Chiquitita - ABBA (by Beatrice Florea)
#url = "https://www.youtube.com/watch?v=ob9s050n7qE"
#Dancing Queen - ABBA (by Beatrice Florea)
#url = "https://www.youtube.com/watch?v=6y6lXqH8zAY"
#Harder, Better, Faster, Stronger | Daft Punk | Pomplamoose
#url = "https://www.youtube.com/watch?v=fUpdfpOPf4Y"
#Instant Crush | Daft Punk | Pomplamoose
#url = "https://www.youtube.com/watch?v=5GRRsZip6-o"
#Technologic // Daft Punk // POMPLAMOOSE
#url = "https://www.youtube.com/watch?v=vQ50OmUs_0E"
#Digital Love | Daft Punk | Pomplamoose
#url = "https://www.youtube.com/watch?v=xy98W3a26gs&list=PLiJey_76CkNRBzI2b-D5Jt_zaqPBu5cQC"
#Daft Punk - Pentatonix // POMPLAMOOSE
#url = "https://www.youtube.com/watch?v=TXgF1LyUA3I&list=PLiJey_76CkNRBzI2b-D5Jt_zaqPBu5cQC"
#Daft Punk - Instant Crush (Video) ft. Julian Casablancas
#url = "https://www.youtube.com/watch?v=a5uQMwRMHcs"
#Depeche Mode - Enjoy the Silence (Remastered Audio) UHD 4K
#url = "https://www.youtube.com/watch?v=BorhbN6CpVw"
#I'm Still Standing | Elton John | Pomplamoose
#url = "https://www.youtube.com/watch?v=eB5EZXLv6PM"
#Bomfunk MC's - Freestyler (Video Original Version)
#url = "https://www.youtube.com/watch?v=ymNFyxvIdaM"
#Personal Jesus
#url = "https://www.youtube.com/watch?v=pm3sP0n7F-M"
#Depeche Mode - Never Let Me Down Again
url = "https://www.youtube.com/watch?v=snILjFUkk_A"
#This is a mashup of Daft Punk's "Technologic", "One More Time", "Get Lucky", "Digital Love", "Harder Better Faster Stronger", "Television Rules the Nation", & "Around the World".


try:
   yt = YouTube(url)
   stream = yt.streams.filter(only_audio=True).first()
   yt.title = re.sub(r"/", "", yt.title)
   print(f"The Song title is currently: \"{yt.title}\"")
   message = (f"y to add {yt.author} to filename ? ")
   user_input = input (message)
   match (user_input.lower()):
    case 'y':
        filename=f"{yt.title}-{yt.author}.mp3"
    case _:
        filename=f"{yt.title}.mp3"
   print("")
   print(f"The Song \"{filename}\" is downloaded")
   stream.download(filename=f"{filename}")

except KeyError:
   print("Unable to fetch video information. Please check the video URL or your network connection.")