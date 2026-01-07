## Latihan 1
try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    op = input("Masukkan operator (+, -, *, /): ")

    if op == "+":
        hasil = a + b
    elif op == "-":
        hasil = a - b
    elif op == "*":
        hasil = a * b
    elif op == "/":
        try:
            hasil = a / b
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol")
            exit()
    else:
        raise Exception("Error: Operator tidak valid")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka")
except Exception as e:
    print(e)

## Latihan 2
nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah = 0

for n in nilai:
    try:
        total += n
        jumlah += 1
    except TypeError:
        continue

rata_rata = total / jumlah
print("Rata-rata nilai:", rata_rata)

