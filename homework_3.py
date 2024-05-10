my_string = input("Какое задание, нужно сделать? ")
print(type(my_string))
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[:1])#Нулевой символ не стал вписывать, т.к посчитал что нужена именно первая буква.
print(my_string[-1])