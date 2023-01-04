
# program to create store calculater and receipt generarator

from fpdf import FPDF


def Recipt_calculate_gen():

    # Code to take user input and show the Sum of user inputs
    sum_price = 0
    user_list = []
    products_name = {}
    print("\n\t\t\t\t\tWelcome to Hussain Store")
    Buywer_name = input('Hey welcome ! \nEnter your name here :')
    while True:
        user = input('\n---  If you want to Enter Product then press Any Key else Press q to Quit  ---  ')

        if (user != 'q'):

            product = input('Enter Product Name here !  ')
            user_price = int(input("Enter price of your product !  "))

            user_list.append(int(user_price))
            sum_price = sum_price + int(user_price)
            products_name[product] = user_price

            print(f"\nTill now you total bill is : {sum_price}\n")

        else:
            print('You program has been quict :( ')
            print(f"\nYour total bill untill is : {sum_price}.RS")
            break


    # Code to generate the Recipt of bill in Command line :
    print('\nAnd Recipt of bill is :) ')
    
    product_list = []
    index = 1
    
    for item in products_name:
        print(f"{index}. Price of '{item}' you enter is :   {products_name[item]}")
        product_list.append(f"{index}. Price of '{item}' you enter is :   {products_name[item]}\n")
        index += 1
        
    print(f"Sum of All Products and Bill is : {sum(user_list)}.RS")

   
    # Creating format of generating Script of bill ---

    store_name = 'Welcome to Hussain Store\n'
    bill_sum = f'Sum of Bill is : {sum(user_list)}'

    
    # Code to generate Recipt of Bill in PDF form ---

    print("\nWould you like to see your Recipt in PDF file ?")
    
    user_ask = input('yes / no \t').lower()
    if user_ask == 'yes':
        pdf = FPDF()

        # Add a new page to the PDF
        pdf.add_page()

        # Set the font and size
        pdf.set_font("Arial", size=18)

        # Write the string to the PDF

        pdf.cell(200, 10, txt=store_name, ln=1)

        for line in product_list:
            pdf.cell(200, 10, txt=line, ln=1)

        pdf.cell(200, 10, txt=bill_sum, ln=1)

        # Save the PDF to a file
        pdf.output(Buywer_name+'.pdf')


# Exrcution of code under main condition ---

if __name__ == '__main__':
    Recipt_calculate_gen()
