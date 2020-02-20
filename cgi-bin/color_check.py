#!/usr/local/bin/python3
import cgi
form = cgi.FieldStorage()

file = open('colorlist.txt', "r")
text = file.read()

username = form.getvalue('username')
color = form.getvalue('color')

#unlogisch aber klappt nur so:
print("""
<p></p>
""")

#um die Farbe in der Text-Datei zu durchsuchen
# %s setzt wie {}.format das in den Klammern Geschriebene in den print-Satz

if color in text:
    print("""
    <h1 style="color: %s">Hello %s,  %s is a color! </h1>
    """ %(color, username, color))
else:
    print("""
    <h1>Hello %s,  %s is not in my list of colors... </h1>""" %(username, color))

#cgi-bin ordner erstellen, wo die .py datei drin ist
#Zugriffsrechte: um auf die Datei zugreifen zu können muss ich chmod 777 cgi-bin/color_check.py ins Terminal eingeben. (777 = read, write,...)
#wenn ich das Programm laufen lassen will muss ich den Local Host im terminal starten: python3 -m http.server --cgi 8000
#im Browser: http://localhost:8000 eingeben