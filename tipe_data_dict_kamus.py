"""
tipe data dictionary sekedar menghubungkan antara key dan value
kpv = key valeu pair
dictionary = kamus
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print (f"nama :{dict['Name']}")
print (f"age :{dict['Age']}")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("Name", dict['Name'])
print ("Age", dict['Age'])


kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'

print(kamus)
print('anak :', kamus['anak'])


print('data ini dikirim oleh server gojek, untuk memberikan info disekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-11-20',
    'driver_list': [
        {'nama': 'eko', 'jarak': '100'},
        {'nama': 'dwi', 'jarak': '50'},
        {'nama': 'tri', 'jarak': '75'},
        {'nama': 'catur', 'jarak': '40'},

    ]
}
print(data_dari_server_gojek)
print(f"\ndriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][3]['jarak']} meter")