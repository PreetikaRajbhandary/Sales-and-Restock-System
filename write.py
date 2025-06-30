#importing necessary modules
import datetime #to work with date and time
import random #to generate random invoice numbers

#function to update products in the file
def update_product_file(dict_):

    """
    Updates the products.txt file with the current product dictionary.
    
    Parameters:
    - dict_ (dict): A dictionary containing product IDs as keys and product details as lists.
    
    Returns:
    - None
    """
    try:
        file=open("products.txt", "w")  #open file in write mode
        for key, value in dict_.items():
            file.write(','.join(value) + '\n') #write each product's details as comma-separated
        file.close() #close the file after writing
        print("Product file updated successfully.") #confirmation message
    except Exception as e:
        print("Error in updating products:", e) #error message if something goes wrong

#function to create a sell invoice
def write_sell_invoice(seller_name, product_name, brand_name, quantity_product, total, free):
    """
    Generates and saves a sell invoice as a text file, showing seller's name, product details, total, and free products.
    
    Parameters:
    - seller_name (str): The name of the seller.
    - product_name (list): A list of product names sold.
    - brand_name (list): A list of brand names for the sold products.
    - quantity_product (list): A list of quantities seold.
    - total (int): The total cost of the sell.
    - free (int): The number of free products received.
    
    Returns:
    - None
    """

    #get today's date
    datetime_ = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day)
    #generate random invoice number
    sell_number = str(random.randint(1000, 9999))

    #print invoice on screen
    print('*' * 75)
    print("\t\t\t\t WeCare Invoice")
    print("\n")
    print("\t Invoice: " + sell_number + "\n")
    print("\t Invoice Date: " + datetime_ + "\n")
    print("\t Name: " + seller_name + "\n")
    print('*' * 75)
    print("\tS.N.\tProduct Name       \tBrand         \tQuantity")
    print('*' * 75)
    SN = 1
    for i in range(len(product_name)):
        print("\n")
        print("\t" + str(SN) + "     " + product_name[i] + "       " + brand_name[i] + "           " + quantity_product[i])
        SN += 1
    print("\nTransaction: ", len(product_name)) #total number of transactions
    print('*' * 75)
    print("Net Amount: ", str(total)) #show total amount
    if free != 0:
        print("\n")
        print("\t\t You have got " + str(free) + " free products")
        print('*' * 75)
    print("\n")
    print("\t\t Thank you for selling the product!")
    print('*' * 75)

    #save the invoice to a text file
    filename = "Invoice " + sell_number + ".txt"
    try:
        invoice_file = open(filename, "w")
        invoice_file.write('*' * 75 + "\n")
        invoice_file.write("\t\t\t\t WeCare Invoice\n")
        invoice_file.write("\n")
        invoice_file.write("\t Invoice: " + sell_number + "\n")
        invoice_file.write("\t Invoice Date: " + datetime_ + "\n")
        invoice_file.write("\t Name: " + seller_name + "\n")
        invoice_file.write('*' * 75 + "\n")
        invoice_file.write("\tS.N.\tProduct Name       \tBrand         \tQuantity\n")
        invoice_file.write('*' * 75 + "\n")
        SN = 1
        for i in range(len(product_name)):
            invoice_file.write("\n")
            invoice_file.write("\t" + str(SN) + "     " + product_name[i] + "       " + brand_name[i] + "           " + quantity_product[i] + "\n")
            SN += 1
        invoice_file.write("\nTransaction: " + str(len(product_name)) + "\n")
        invoice_file.write('*' * 75 + "\n")
        invoice_file.write("Net Amount: " + str(total) + "\n")
        if free != 0:
            invoice_file.write("\n")
            invoice_file.write("\t\t You have got " + str(free) + " free products\n")
            invoice_file.write('*' * 75 + "\n")
        invoice_file.write("\n")
        invoice_file.write("\t\t Thank you for selling the product!\n")
        invoice_file.write('*' * 75 + "\n")
        invoice_file.close()
    except Exception as e:
        print("Error writing sell invoice file:", e)


#function to create a restock invoice
def write_restock_invoice(vendor_name, product_name, brand_name, quantity_product, vat, total_restock_amount):

    """
    Generates and saves a restock invoice as a text file, showing vendor's name, product details, VAT, and total amount.
    
    Parameters:
    - vendor_name (str): The name of the vendor.
    - product_name (list): A list of product names restocked.
    - brand_name (list): A list of brand names for the restocked products.
    - quantity_product (list): A list of quantities restocked.
    - vat (int): The total VAT amount (13%).
    - total_restock_amount (int): The total cost of restocking, including VAT.
    
    Returns:
    - None
    """

    date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day)
    restock_number = str(random.randint(1000, 9999))

    #print restock invoice
    print('*' * 75)
    print("\t\t\t\t WeCare Invoice")
    print("\n")
    print("\t Invoice Number: " + restock_number + "\n")
    print("\t Date: " + date + "\n")
    print("\t Name: " + vendor_name + "\n")
    print('*' * 75)
    print("\tS.N.\tProduct Name       \tBrand         \tQuantity")
    print('*' * 75)
    SN = 1
    for i in range(len(product_name)):
        print("\n")
        print("\t" + str(SN) + "     " + product_name[i] + "       " + brand_name[i] + "           " + quantity_product[i])
        SN += 1
    print('*' * 75)
    print("VAT (13%):", vat)
    print("Net Amount:", str(total_restock_amount))
    print('*' * 75)
    print("\n")
    print("\t\t Thank you for restocking the items!")
    print('*' * 75)

    #save restock invoice to a file
    filename = "Restock " + restock_number + ".txt"
    try:
        restock_file = open(filename, "w")
        restock_file.write('*' * 75 + "\n")
        restock_file.write("\t\t\t\t WeCare Restock\n")
        restock_file.write("\n")
        restock_file.write("\t Restock ID: " + restock_number + "\n")
        restock_file.write("\tDate: " + date + "\n")
        restock_file.write("\t Name: " + vendor_name + "\n")
        restock_file.write('*' * 75 + "\n")
        restock_file.write("\tS.N.\tProduct Name       \tBrand         \tQuantity\n")
        restock_file.write('*' * 75 + "\n")
        SN = 1
        for i in range(len(product_name)):
            restock_file.write("\n")
            restock_file.write("\t" + str(SN) + "     " + product_name[i] + "       " + brand_name[i] + "           " + quantity_product[i] + "\n")
            SN += 1
        restock_file.write('*' * 75 + "\n")
        restock_file.write("VAT (13%): " + str(vat) + "\n")
        restock_file.write("Net Amount: " + str(total_restock_amount) + "\n")
        restock_file.write('*' * 75 + "\n")
        restock_file.write("\n")
        restock_file.write("\t\t Thank you for restocking the items!\n")
        restock_file.write('*' * 75 + "\n")
        restock_file.close()
    except Exception as e:
        print("Error writing restock invoice file:", e)
