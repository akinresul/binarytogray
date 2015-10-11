# kullanicidan alinan 10 luk tabandaki sayiyi ikilik tabana ve daha sonra gray koduna donusturen program
dec=input("Onluk tabanda bir sayi giriniz\n")
def decimaltobinarytogray(dec): 
	binary=[]
	while (dec>0):
		binary.insert(0,(dec%2))
		dec=dec/2
	gray=[]
	gray.append(binary[0]) #binary'nin en anlamli biti eklenir
	indis=0
	while(indis<len(binary)-1) :
		toplam=binary[indis]+binary[indis+1] 
		gray.append(toplam%2) #toplam ve sonunda 2 ile mod alinarak bir nevi xor alinir ve gray dizisine eklenir.
		indis=indis+1
	print "Girilen onluk tabandaki(decimal) sayinin ikilik tabandaki(binary) karsiligi :\n",binary,"olarak hesaplandi"
	print "Olusan ikilik tabandaki(binary) sayinin gray karsiligi :\n",gray,"olarak hesaplandi"
decimaltobinarytogray(int(dec))
