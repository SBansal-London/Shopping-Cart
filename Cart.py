list_item=[]
list_cost = []

def shopping_cart(list_item , list_cost):
    print("-"*60)
    print("This is your shopping Cart :")
    for counter, items in enumerate(list_item,1) :
       print(f"{items} \t\t\t\t\t {list_cost[counter-1]} ")
    print("-"*60)
    total_cost = 0
    for costs in list_cost :
        total_cost +=int(costs)
    print(f"Total \t\t\t\t\t {total_cost}")
    print("-"*60)


done = True

print("Welcome to Paws and Cart \n\n")
shopping_cart(list_item , list_cost)
while (done) :
    print("Would you like to :")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. Update an item in your cart")
    print("4. Checkout")
    p = int(input("Enter the number of the option you would like to choose : "))

    if p==1:
        add_item = input("What item would you like to add :")
        list_item.append(add_item)
        item_cost = input("How much does the item cost : ")
        list_cost.append(item_cost)
        print(f"{add_item} has been added to your cart successfully\n")
        shopping_cart(list_item , list_cost)
    
    elif p==2:
        remove_item = input("What item would you like to remove :")
        rem_pos = list_item.index(remove_item)
        list_item.pop(rem_pos)
        list_cost.pop(rem_pos)
        print(f"{remove_item} has been removed from your cart successfully\n")
        shopping_cart(list_item , list_cost)

    elif p==3:
        update_item = input("What item would you like to update :")
        update_pos = list_item.index(update_item)
        update_cost = input(f"Enter the updated cost of {update_item} :")
        list_cost[update_pos] = update_cost
        print(f" cost for {update_item} has been updated in your cart successfully\n")
        shopping_cart(list_item , list_cost)

    elif p==4:
        total_cost = 0
        for costs in list_cost :
            total_cost +=int(costs)
        print(f"Thank you for shopping. Your total cart cost is {total_cost}")
        done = False
    
    else :
        print("This is not a valid option")  
