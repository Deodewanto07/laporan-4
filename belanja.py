def hitung_belanja (belanja, diskon = 10 ) :
    bayar = belanja - (belanja * diskon) / 100

    return bayar

print (hitung_belanja(100000))
print (hitung_belanja(100000,50))
print (hitung_belanja(100000,100))