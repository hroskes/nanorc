import os
import re

colors = (
          ("black", "white"),
          ("red", "cyan"),
          ("blue", "yellow"),
          ("green", "magenta"),
         )

def replace(s, color1, color2):
    s = re.sub(r"\b(bright|)"+color1+r"\b", r"\1TMPTMPTMP", s)
    s = re.sub(r"\b(bright|)"+color2+r"\b", r"\1"+color1, s)
    s = re.sub(r"\b(bright|)TMPTMPTMP\b", r"\1"+color1, s)
    return s

def replaceall(filename):
    with open(filename) as f:
        s = f.read()
    for pair in colors:
        s = replace(s, *pair)
    with open(filename, "w") as f:
        f.write(s)

if __name__ == "__main__":
    for filename in os.listdir("."):
        if filename.endswith(".nanorc"):
            replaceall(filename)
