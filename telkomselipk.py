def main() :
	x = input("Masukan Provider Anda : ")
	y = input("Masukan IPK Anda : ")

	if x == "Telkomsel" and y >= "3" and y <= "4" :
		print("Selamat Anda Mendapatkan Iphone X")
	elif x != "Telkomsel" and y >= "3" and y <= "4" :
		print("Selamat Anda Mendapatkan Samsung J Galaxy Series")
	elif x == "Telkomsel" and y >= "2,5" and y <= "3" :
		print("Selamat Anda Mendapatkan PS 4")
	elif x != "Telkomsel" and y >= "2,5" and y <= "3" :
		print("Selamat Anda Mendapatkan Voucher Menginap di Ibis Trans Studio Mall")
	elif x == "Telkomsel" and y >= "2" and y <= "2,5" :
		print("Selamat Anda Mendapatkan Voucher Menginap di Pesantren Daarut Tauhid")
	elif x != "Telkomsel" and y >= "2" and y <= "2,5" :
		print("Selamat Anda Mendapatkan Voucher Konsul Klinik Psikologi")
	elif y >= "4" :
		print("IPK Anda tidak valid")
		print("Kembali ke menu awal?\n1.Ya\n2.Tidak")
		z = input("Pilihan Anda : ")
		if z == "1" :
			main()
		elif z == "2" :
			print("Silahkan Ulang Kembali")
	else :
		print("Selamat, Terima Kasih!")
main()