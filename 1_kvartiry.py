number_of_flat = int(input("Квартира: "))
amount_of_floors = 9
amount_of_flats_per_floor = 4
entrance = (number_of_flat-1)//amount_of_floors * amount_of_flats_per_floor
floor = ((number_of_flat-1) % amount_of_floors * amount_of_flats_per_floor) // amount_of_flats_per_floor
print("Під'зд",entrance+1)
print("Поверх",floor+1,"\n")
