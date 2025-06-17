#CSV to HTML
import os
dir = "C://Users/luca.ferreirawolters/Desktop/PythonTest"
csv_datei = open(dir + "/BoxOfficeMojo.csv", "r")
html_datei = open(dir + "/BoxOfficeMojo.html", "a")
html_datei.write("<html><body><h1>Box Office Mojo Ranking</h1><table>")
table = csv_datei.readlines()
for zeile in table:
    neue_zeile = zeile.replace(";", "</td><td>")
    html_datei.write("<tr><th>" + neue_zeile)
html_datei.write("</table></body></html>")