import main_script
import os
from pathlib import Path
if input("type crop if you want = ") == "crop":
    link = input("link = ")
    start = float(input("start in sec = "))
    stop = float(input("stop in sec = "))
    sussy = main_script.Download(link)
    if sussy != "-1":
        sussy2 = main_script.VideoCrop(sussy, start, stop)
        print(sussy2)
        print ("deleting Original")
        os.remove(sussy)
        input("ok?")

else:
    main_script.Download(input("link = "))
    input("ok?")