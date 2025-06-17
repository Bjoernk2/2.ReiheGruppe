text = input("Enter a text: ")

x = 0
for i in text:
    if i.isdigit():
        x = x + 1

print("Anzahl von Zahlen " + str(x))