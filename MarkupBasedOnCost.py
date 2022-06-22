print("Calculate Merkup Based On Cost While Cost And Markup Known Ditanya Sell")
print("                     ")
cost=float(input("Mohon Masukan Cost: "))
print("                     ")
markup=float(input("Mohon Masukan Markup dalam Persentase:  "))
percent=markup/100
print("                     ")
markup_cost=cost*percent
print("Markup As Integer Is: ",markup_cost)
print("               ")
print("Markup As Selling Is: ",markup,"%")
print("                     ")

selling_price=markup_cost+cost
print("Selling Price As Integer Is: ",selling_price)
print("                     ")
print("Selling Price: ",100+markup,"%")
