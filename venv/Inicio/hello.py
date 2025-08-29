#print("Hello world, from Python!")

name = "Daniel"
lastname = "Amarante"
#print(f"Hello {name}, from Python!")

full_name = name + " " + lastname
new_message = "Hello, " + full_name.title() + "!"

# Concatenando strings
full_name = name + " " + lastname
print(f"1 print Hello {full_name}, from Python!")

message = "You need to learn Python"
print(f'2 print{name, message}')
print(f'3 print {name.title(), message.title()}')

print(f'4 print {name.upper(), message.lower()}')

print(f'5 print {name[0:3], message[0:10]}')

print(f' 6 print {len(name), len(message)}')

print(f'7 print {name.replace("a", "4"), message.replace("learn", "master")}')

print(f'8 print {name in message, "Python" in message}')

print(f'9 print {name*3, message*2}')

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Remover espaços em branco
favorite_language = ' Python '
print(favorite_language)

# Remvoer espaços em brnaco do lado direito
print(favorite_language.rstrip())
# Remover espaços em branco do lado esquerdo
print(favorite_language.lstrip())