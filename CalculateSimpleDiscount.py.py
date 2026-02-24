item = (input("Masukan Nama Barang: "))
price = int(input("Masukan Harga{item}: "))

if price >= 100000:
    discount = price * 0.10
    status = "Mendapatkan discount 10%"
elif price <= 100000:
    discount = 0
    status = "Tidak ada discount"
    
totalPayment = price - discount

print(f"Nama Barang  : {item}")
print(f"Harga Satuan : Rp {price:,.0f}")
print(f"Status       : {status}")
print(f"Potongan     : Rp {discount:,.0f}")
print("------------------------")
print(f"TOTAL BAYAR  : Rp {totalPayment:,.0f}")