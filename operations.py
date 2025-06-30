#importing functions from other Python files
from read import display_products  #function to display available products
from write import write_sell_invoice, write_restock_invoice  #functions to write invoices for sell, and restock

#function to handle product selling
def sell_products(dict_, count):
    """
    Handles product purchases, updates stock, applies 'buy 3 get 1 free' offer, and generates an invoice if requested.
    
    Parameters:
    - dict_ (dict): A dictionary containing product IDs as keys and product details as lists.
    - count (int): The total number of products in the dictionary.
    
    Returns:
    - dict_: The updated dictionary with modified stock quantities.
    - count: The unchanged count of products.
    """
    print("\n You have decided to sell products.\n")
    
    #display all available products
    display_products(dict_)
    
    #ask for buyer's name
    seller_name = input(" Enter seller's name: ")  

    #initialize lists to store purchased product details
    product_name = []
    brand_name = []
    quantity_product = []
    
    free = 0  # Number of free items given on buy 3 get 1 free
    total = 0  # Total amount of the purchase

    #outer loop continues until user exits
    while True:
        #inner loop handles buying each product
        while True:  
            try:
                #ask user for the product ID 
                product_id = int(input("\n Please enter the product ID that you want to sell: "))
                if product_id not in dict_:
                    print("Invalid product ID.")
                    continue  #ask again if ID is not found
               
                #ask for quantity
                quantity = int(input("\n Please enter the quantity of the product that you want to sell: "))
                if quantity <= 0:
                    print("Invalid Input.")
                    continue  #quantity should be positive

                available_quantity = int(dict_[product_id][2])  #current stock

                #if enough stock is available
                if quantity <= available_quantity:
                    print(" Proceeding with sell...\n")

                    #calculate free items (buy 3 get 1 free)
                    free_item = quantity // 3
                    totalproducts = quantity + free_item  #total items taken

                    #double the price
                    price1 = int(int(dict_[product_id][3]) * 2)

                    #check if total with free items exceeds stock
                    if totalproducts > available_quantity:
                        dict_[product_id][2] = str(available_quantity - quantity)
                        total += (quantity - free_item) * price1
                        quantity_product.append(str(quantity))  #append paid quantity only
                    else:
                        dict_[product_id][2] = str(available_quantity - totalproducts)
                        total += quantity * price1
                        quantity_product.append(str(totalproducts))  #append total (including free items)

                    #store product info for invoice
                    product_name.append(dict_[product_id][0])  #product type
                    brand_name.append(dict_[product_id][1])    #brand name
                    free += free_item  #add to total free items

                    #ask if user wants to sell more
                    question = input("\n Do you want to sell more products? (yes/no): ")
                    if question.lower() == "no":
                        break  #exit inner loop
                    elif question.lower() == "yes":
                        continue  #repeat inner loop
                else:
                    print("\n Sorry, only " + str(available_quantity) + " items are available.")
                    continue
            except:
                print("Invalid input.")
                continue

        #ask if user wants to generate the invoice
        ask = input("\n Do you want to generate the invoice? (yes/no): ")
        if ask.lower() == "yes":
            # generate and write invoice to file
            write_sell_invoice(seller_name, product_name, brand_name, quantity_product, total, free)
            break
        else:
            print("\n You chose not to generate an invoice. You can continue to enter products.")
    return dict_, count  #return updated product dictionary and count


#function to handle restocking products
def restock_products(dict_, count):
    """
    Facilitates product restocking, updates stock, calculates cost with 13% VAT, and generates an invoice if requested.
    
    Parameters:
    - dict_ (dict): A dictionary containing product IDs as keys and product details as lists.
    - count (int): The total number of products in the dictionary.
    
    Returns:
    - dict_: The updated dictionary with increased stock quantities.
    - count: The unchanged count of products.
    """
    print("\n You have selected to restock products.\n")

    #display all available products
    display_products(dict_)

    #ask for vendor's name
    vendor_name = input("\n Enter the vendor's name: ")

    #initialize lists to store purchased product details
    product_name = []
    brand_name = []
    quantity_product = []
    
    #variables to keep track of total restock amount and VAT
    total_restock_amount = 0  
    vat = 0  

    #outer loop continues until user exits
    while True:
        #inner loop handles buying each product
        while True:
            try:
                #ask user for the product ID
                product_id = int(input("\n Please enter the product ID that you want to restock: "))
                if product_id not in dict_:
                    print("Invalid product ID!")
                    continue #ask again if ID is not found
               
                #ask for quantity
                quantity = int(input("\n Please enter the quantity of the product: "))
                if quantity <= 0:
                    print("Invalid Input.")
                    continue

                #calculate cost price (double) and VAT
                cost_price = int(int(dict_[product_id][3]) * 2) #double the price
                total_cost_price = cost_price * quantity
                current_vat = (total_cost_price * 13) // 100  #13% VAT
                current_total_cost = total_cost_price + current_vat
                vat += current_vat

                #update stock quantity
                available_quantity = int(dict_[product_id][2])
                dict_[product_id][2] = str(available_quantity + quantity)

                
                product_name.append(dict_[product_id][0]) #product type
                brand_name.append(dict_[product_id][1]) #brand name
                quantity_product.append(str(quantity))
                total_restock_amount += current_total_cost

                #ask if user wants to restock more    
                question = input("\n Do you want to restock more items? (yes/no): ")
                if question.lower() == "no":
                    break #exit inner loop
                elif question.lower() == "yes":
                    continue  #repeat inner loop
            except:
                print("Invalid input.")
                continue

        #ask if user wants to generate the invoice
        ask = input("\n Do you want to generate the invoice? (yes/no): ")
        if ask.lower() == "yes":
            #generate and write invoice to file
            write_restock_invoice(vendor_name, product_name, brand_name, quantity_product, vat, total_restock_amount)
            break
        else:
            print("\n You chose not to generate an invoice. You can continue to enter products.")
    return dict_, count #return updated product dictionary and count
