variabel = 'tempat penyimpanan data'
print(variabel)

code = ['python', 'java', 'kotlin', 'laravel']
code.append('go')
print(code)
print(f' code {code[0]}') # mengambil kode ke 1
for c in code: # menampilkan semua kode
    print(f' code {c}') # ambil semua kode
for c in range(0, len(code)): # menampilkan kode cara rumit
    print(f' {c+1} code {code[c]}') # pakai 'len'