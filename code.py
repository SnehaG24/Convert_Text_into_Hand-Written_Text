import pywhatkit

import flask

# text = "Hello Everyone!"

text = input("Enter text := ")

# filename = input("Type Your Text : ")

filename = input("Enter the Filename : ")     # Filename : filename.png 

pywhatkit.text_to_handwriting(text,filename,[0,20,254])

print("Done!")
