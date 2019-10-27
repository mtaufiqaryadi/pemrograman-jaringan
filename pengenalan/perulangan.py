#for

#for i in [1, 2, 3, 4, 5]:
#   print ("ini pengulangan ke -", i)


#for i in["Rawon", "nasi kuning", "soto madura", "kupat tahu"]:
#    print(i, "adalah masakan khas nusantara ...")    

#for i in range(1, 10, 2):
#    print ("ini perulangan ke - ", i)

#angka = 0
#while (angka < 10):
#    print("putaran ke", angka)
#    angka += 1

terus_tanya = True
while terus_tanya :
    temp = input("masukkan angka kurang dari 10 : ")
    angka = int(temp)
    if angka < 10:
        terus_tanya = True
    else:
        terus_tanya = False