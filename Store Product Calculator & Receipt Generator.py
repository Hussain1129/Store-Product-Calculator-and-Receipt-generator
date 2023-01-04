
# program to create store calculater and receipt generarator

from fpdf import FPDF


def Recipt_calculate_gen():

    # Code to taking user input and showing of Sum of Calulation
    sum_price = 0
    user_list = []
    print("\n\t\t\t\t\tWelcome to Hussain Store")
    Buywer_name = input('Hey welcome ! \nEnter your name here :')
    while True:
        user = input("\nEnter price of thing else press q to Quict ... ")
        
        if (user != 'q'):
            user_list.append(int(user))
            sum_price = sum_price + int(user)
            print(f"Till now you total bill is : {sum_price}")
            
        else:
            print('You program has been quict :( ')
            print(f"\nYour total bill untill is : {sum_price}.RS")
            break



    # Code to generate the Recipt of bill is :

    print('\nAnd Recipt of bill is :')
    product_list = []

    for index, price in enumerate(user_list):
        print(f"{index}. list of your bill is :  {price}")
        product_list.append(f"{index}. List you Enter is :  {price}\n")
    print(f"Sum of Bill is : {sum(user_list)}")

    
    
    # # Format of generating Script of bill ---

    # store_name = 'Welcome to Hussain Store\n'
    # bill_sum = f'Sum of Bill is : {sum(user_list)}'

   
    # # Code to generate Recipt of Bill in Text form ---

    # print("\nWould you like to see your Recipt in PDF file ?")
    # user_ask = input('yes / no \t').lower()
    # if user_ask == 'yes':
    #     pdf = FPDF()

    #     # Add a new page to the PDF
    #     pdf.add_page()

    #     # Set the font and size
    #     pdf.set_font("Arial", size=18)

    #     # Write the string to the PDF
        
    #     pdf.cell(200, 10, txt=store_name, ln=1)
        
    #     for line in product_list:
    #         pdf.cell(200, 10, txt=line, ln=1)
            
    #     pdf.cell(200, 10, txt=bill_sum, ln=1)

    #     # Save the PDF to a file
    #     pdf.output(Buywer_name+'.pdf')


# Exrcution of code by main condition ---

if __name__ == '__main__':
    Recipt_calculate_gen()
