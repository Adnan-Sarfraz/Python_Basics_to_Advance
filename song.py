# print_lyrics.py
# Prints a multi-line script one word at a time with delay matching ~96 BPM (~0.625 seconds per word).
import re
import time
import sys

text = """Ni tenu Dekh k jee lagda 
Dekh deeva jagda
Tenu dekh k tan lgda
Tu Moraa'n kolo
Sikhdi toraa'n
Das Ki chauhni ae?
Jaan sakauni ae!
Ni Tu jad vaal sakauni ae
Fir Sulfe vaangu Charhdia lora
Jo
Kahegi jatt karju goriye
Dova da changa sarju goriye
Tusi Eve na daro
Kade milke betho
Gal kriye pyar di
Vaaj kaali kaali raat Mardi
Dekho Tare'an di lo"""

tokens = re.split(r'(\s+)', text)

DELAY_SECONDS = 60.0 / 96.0  # ~0.625 seconds delay per word

try:
    for token in tokens:
        if token.isspace():
            sys.stdout.write(token)
            sys.stdout.flush()
        else:
            sys.stdout.write(token)
            sys.stdout.flush()
            time.sleep(DELAY_SECONDS)
except KeyboardInterrupt:
    sys.stdout.write("\n\nInterrupted by user. Exiting.\n")
    sys.stdout.flush()
