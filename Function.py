def P_M(popcorn_count, amount_of_mountaindew) :
    print(f"You have {popcorn_count} Popcorns!")
    print(f"You have {amount_of_mountaindew} cans of MtnDew")
    print("Man. that's enough for a party!")
    print("Get a Blanket.\n")

print("We can give the function numbers directly: ")
P_M(100,50)

print("We can give the numbers in script too: ")
amount_of_popcorn=50
amount_of_mtndew=100

P_M(amount_of_popcorn,amount_of_mtndew)

print("We can do math inside it too: ")
P_M(50+60,110+90)

print("We can combine both: ")
P_M(amount_of_popcorn+100, amount_of_mtndew+1000)
 
