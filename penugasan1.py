# mengonversi suhu dalam derajat celcius menjadi derajat fahrenheit
celcius = int(input("Masukan suhu dalam celcius: "))
fahrenheit = (celcius * 9/5) + 32

print(celcius, 'Derajat Celcius =', fahrenheit, 'Derajat Fahrenheit')

# mengonversi suhu dalam derajat fahrenheit menjadi derajat celcius
fahrenheit = int(input("Masukan suhu dalam fahrenheit: "))
celcius = (fahrenheit - 32) * 5/9

print(celcius, 'Derajat Celcius =', fahrenheit, 'Derajat Fahrenheit')
