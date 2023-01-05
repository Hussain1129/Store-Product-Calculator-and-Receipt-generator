
# Calculate Products and Generate a Receipt PDF.

A Python project which calculate the Products entered by user and Create a Receipt of User Products which includes all Products and their prices entered by user and give total Sum of such Products.




___
![App Screenshot](https://www.klippa.com/wp-content/uploads/2022/07/Travel_Expenses_Title.png)


# Deployment

To deploy this project you need only python and for generating of PDf file here you can use FPDF library.

### Install fpdf library :
To install run this command in cmd / Anaconda powershell --

```bash
  pip install fpdf
```
Now here we will disscuss about development of this project by saperating code to Explore better. 

### Importing fpdf library :
First I will import FPDF library to get Receipt in PDF form :

```bash
  from fpdf import FPDF
```

### Create a funtion in which we write code :
I do this all code in Recipt_calculate_gen() function and at the end of code call this function under main condition.
```bash
  def Recipt_calculate_gen():

    ###     --------

  if __name__ == '__main__':
      Recipt_calculate_gen()
```

### Creating While loop to continously take input
Under this function first i create a While loop to continously get the input by user and enter to list to sum them. And in this we use Condition to Quit and running and in this we apply condition to get and arrange the products and their prices.

```bash
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
```

### Generate the Recipt of bill :

Now its time to Generate the Receipt of bill in command line. so write the code to get this :

```bash
  # Code to generate the Recipt of bill in Command line :

    print('\nAnd Recipt of bill is :) ')
    
    product_list = []
    index = 1
    
    for item in products_name:
        print(f"{index}. Price of '{item}' you enter is :   {products_name[item]}")
        product_list.append(f"{index}. Price of '{item}' you enter is :   {products_name[item]}\n")
        index += 1
        
    print(f"Sum of All Products and Bill is : {sum(user_list)}.RS")
```

### Creating a Format for Receipt PDF
Now we create a format of Receipt which will show in PDF so :

```bash
  # Creating format of generating Script of bill ---

    store_name = 'Welcome to Hussain Store\n'
    bill_sum = f'Sum of Bill is : {sum(user_list)}'
```

### Code to Generate Receipt in PDF form :

Here is the code which will create a PDF by taking all product_list and their prices entered by user :



```bash
    # Code to generate Recipt of Bill in PDF form ---
    
    print("\nWould you like to see your Recipt in PDF file ?")
    
    user_ask = input('yes / no \t').lower()
    if user_ask == 'yes':

        pdf = FPDF()

        # Add a new page to the PDF
        pdf.add_page()

        # Set the font and size
        pdf.set_font("Arial", size=20)

        # Write the string to the PDF
        pdf.cell(200, 10, txt='', ln=4)
        
        pdf.cell(200, 10, txt=store_name, align="C", ln=1)
        
        pdf.cell(200, 10, txt='', ln=1)
        
        pdf.cell(200, 10, txt=('Dear '+Buywer_name) + ' ! \tyour bill is :', ln=1)
        
        pdf.cell(200, 10, txt='', ln=1)        # Insert a Blank line

        for line in product_list:
            pdf.cell(200, 10, txt=line, ln=1)

        pdf.cell(200, 10, txt='', ln=1)
        pdf.cell(200, 10, txt=bill_sum, ln=1)

        # Save the PDF to a file
        pdf.output(Buywer_name+'.pdf')
  ```
## Features

- Friendly Interface
- Include Execution file
- Simple and Easy code to Understand
- well running


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd Create store Calculator & Receipt Generator
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/Hussain1129/Store-Product-Calculator-and-Receipt-generator.git
```

Go to the project directory

```bash
  cd Create store Calculator & Receipt Generator
```

Install dependencies

```bash
  pip Install fpdf
```

Start the server

Open command prompt and type this :
```bash
  python Create store Calculator & Receipt Generator.py
```

Insteed of this Run Create store Calculator & Receipt Generator.exe file directly.

## 🛠 Skills
Javascript, HTML, CSS, python, Django, Docker, Numpy, Pandas, Matplotlib, seaborns...


## 🚀 About Me
visit :  https://github.com/hussain1129


## Contributing

Contributions are always welcome!

See `store Calculator & Receipt Generator.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Support

For support, email hussainali54711@gmail.com or Follow me on Github for more imformation

