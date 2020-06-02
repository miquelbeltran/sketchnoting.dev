import os
import fileinput

print("Process images")

for filename in os.listdir("img/sketchnotes"):
    print(filename)
    os.system("mogrify -resize 300x300 -quality 75 \-format webp -write static/img/sketchnotes/" + os.path.splitext(filename)[0] + "-mini.webp img/sketchnotes/" + filename)
    os.system("cp img/sketchnotes/" + filename + " static/img/sketchnotes/"+ os.path.splitext(filename)[0] + "-full.jpg")


for filename in os.listdir("content/sketchnotes"):
    print(filename)
    with open("content/sketchnotes/" + filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('img/sketchnotes/', '')
    filedata = filedata.replace('.jpeg', '')
    filedata = filedata.replace('.jpg', '')

    with open("content/sketchnotes/" + filename, 'w') as file:
        file.write(filedata)

