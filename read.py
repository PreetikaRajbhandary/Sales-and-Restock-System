def read_product():
    """
    Reads product data from 'products.txt' and stores it in a dictionary with unique IDs.

    Parameters:
    - None
    
    Returns:
    - dict_ (dict): A dictionary containing product IDs as keys and product details as lists
    - count: An integer representing the total number of products.
    """
    #open the file 'product.txt' in read mode
    file = open("products.txt", "r")                    

    #read all the text in the file and store it in a variable called 'product'
    product = file.read()

    #close the file after reading
    file.close()
    
    #create an empty dictionary to store product details with a unique ID
    dict_ = {}
    #Counter to keep track of product IDs
    count = 0

    #spliting the content in new lines
    l = product.split('\n')  #splits the content by each new line

     
    '''loop through each line,
    split product data by comma,
    and store it in the dictionary with an ID key.'''
    for i in range(len(l)):
        if l[i] and ',' in l[i]:#check if line is not empty and contains comma
                count = count + 1
                dict_[count] = l[i].split(',')#split line by comma and store as a list


    #return the dictionary and the count of products
    return dict_,count
        
def display_products(dict_):

    """
    Displays all products in a formatted table with details like ID, name, brand, quantity, price, and country.
    
    Parameters:
    - dict_ (dict): A dictionary containing product IDs as keys and product details as lists.
    
    Returns:
    - None
    """
    
    #print table headers for better formatting
    print("=" * 90)
    
    #print column headings with proper spacing
    print("ID\tProduct Name       \tBrand         \tQuantity\tPrice   \tCountry")
    print("=" * 90)

    #loop through the dictionary to print each product
    for key, value in dict_.items():
        print(key, end='\t') #print product ID
        
        #loop through the list of product details
        for j in range(len(value)):
            
            if j == 3:
                #double the original price for display
                price = int(int(value[j]) * 2)
                print("\t", price, end="\t")#print the new price with spacing
                
            elif j == 1:
                print(value[j], end="\t")#if it's the brand name, print with extra tab for alignment
                
            else:
                 print(value[j], end="\t")#print other values (like product name, quantity, country)

        #move to the next line for the next product
        print()

    #print the bottom border of the table
    print("=" * 90)

