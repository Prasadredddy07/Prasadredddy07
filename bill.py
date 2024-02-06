#write a program to calculate  amount of total units used to generate electric bill

prevreading=int(input("Enter the prev reading:"))
curreading=int(input("Enter the cur reading:"))
totalreading=prevreading-curreading
cost_perunit=7
amount=totalreading*cost_perunit

print("The electricity bill:",amount)
