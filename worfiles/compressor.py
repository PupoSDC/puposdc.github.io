import sys
import string

classes       = []
finalcss      = ""
finalhhtml    = ""

# Defines new classes ( a, b, c.... aa,ab,...)
newClasses = list(string.ascii_lowercase)
for i in range(0,26):
    for j in range(0, 26):
        newClasses.append(newClasses[i] + newClasses[j])


# open files
with open("html.html") as html, open("css.css") as css:

    for line in css:
        if line.lstrip()[:1].find(".") == 0: 
            for word in line.split():
                if word.find(".") == 0: 
                    classes.append(word.replace(".","").replace("{",""))

    # removes duplicate classes and mods
    classes = list(set(classes))
    for i, s in enumerate(classes):
        classes[i] = classes[i].split(":")[0]

    # creates compressed css line
    for line in css:
        if line.lstrip()[:1].find(".") == 0: 
            for word in line.split():
                if word.find(".") == 0: 
                    for idx, val in enumerate(classes):
                        if word.replace(".","").replace("{","") == classes[idx]:
                            line = line.replace(classes[idx],newClasses[idx])
        css+=line.strip().replace(" ","")


    for line in html:
        for i, s in enumerate(classes):
            if line.lstrip("class=")[:15].find(classes[i]) > -1: 
                print line

    print html

