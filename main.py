#import necessary functions from other modules
from read import read_product,display_products
from operations import sell_products, restock_products
from write import update_product_file

def main():

    """
    Runs the main program with a menu for displaying products,selling, restocking, or exiting.
    
    Parameters:
    - None
    
    Returns:
    - None
    """
    
    #read the product data from the file at the start of the program
    dict_, count = read_product()
    run = True

    #main program loop
    while run:
        #display menu options
        print("\n 1.Display Products\n 2.Sell\n 3.Restock\n 4.Exit")

        try:
            #ask the user for their menu choice
            choice = int(input("\n Please enter your choice: "))

            #if user chooses to display products
            if choice == 1:
                print("\n Displaying the products.\n")
                display_products(dict_)
                
            #if user chooses to sell a product
            elif choice == 2:
                dict_, count = sell_products(dict_,count) #perform sell operation
                update_product_file(dict_) #save changes to file
            

            #if user chooses to restock products
            elif choice == 3:
                dict_, count = restock_products(dict_,count) #perform restock operation
                update_product_file(dict_) #save changes to file
            
            #if user chooses to exit the program
            elif choice == 4:
                print("\n You have selected to exit the application.\n")
                update_product_file(dict_) #save final changes before exit
                run = False #exit the loop and end the program

            #if user enters a number outside 1–5
            else:
                print("\n Exiting the program.")
                
        #handle non-integer input from the user
        except:
            print("\n Invalid choice. Please choose from 1 to 4.")
            
#start the program
main()
