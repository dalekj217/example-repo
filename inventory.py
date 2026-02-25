class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Returns the cost of the shoes
    def get_cost(self):
        return self.cost

    # Returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"Country: {self.country}, Code: {self.code}, Product: {self.product}, "
                f"Cost: {self.cost}, Quantity: {self.quantity}")
        

shoe_list = []

# Reads data from txt file, create a shoe object, append object to show list
def read_shoes_data():

    try:
        with open("inventory.txt", "r") as file:
            next(file)
            
            for lines in file:
                
                try:

                    temp = lines.strip()
                    temp = lines.split(",")

                    shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

                except (IndexError, ValueError) as e:
                    print(f"Skipping invalid line: {lines.strip()} | Error: {e}")

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")


# Allows user to capture data about shoe object and append this object to shoe list
def capture_shoes():
    
    country = input("Enter the Country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    cost = int(input("Enter the cost: "))
    qty = int(input("Enter the quantity of the product: "))

    shoe_list.append(Shoe(country, code, product, cost, qty))

    print(f"{product} has been added to the inventory.")

# Iterate over the shoe list and print details of shoes returned from the str method
def view_all(shoe_list):
    
    if not shoe_list:
        print("No shoes in inventory.")
        return
    
    print("\n---Shoe Inventory ---")
    for shoe in shoe_list:
        print(shoe)

# Finds shoe object with lowest quantity, ask user if they want to add this quantity
# then update it in the file
def restock(shoe_list):
    if not shoe_list:
        print("No shoes in inventory.")
        return None
    
    # Find the lowest quantity shoe
    lowest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < lowest_shoe.quantity:
            lowest_shoe = shoe

    print("Shoe with lowest stock: ", lowest_shoe)

    # Ask user to restock
    re_stock = input("Would you like to restock this shoe? Y or N").lower()
    if re_stock == 'n':
        print("Restock cancelled.")
        return

    try:
        
        amount = int(input("How many units would you like to add? "))
        if amount <0:
            print("Units must be greater than 0.")
            return
        
        lowest_shoe.quantity += amount
        print("Stock updated in the system for ", lowest_shoe)

        with open ("inventory.txt", "w") as file:
            file.write("Country, Code, Product, Cost, Quantity\n")

            for shoe in shoe_list:
                line = f"{shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}\n"
                file.write(line)

        print("Inventory file updated successfully.")

    except ValueError:
        print("Invalid number entered.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Searches for shoe using the shoe code and return the object
def search_shoe():
    
    if not shoe_list:
        print("No shoes in inventory.")
        return None

    search_code = input("Enter the shoe code to search: ").strip()

    for shoe in shoe_list:
        if shoe.code.lower() == search_code.lower():
            print("\nShoe found:")
            print(shoe)   # Calls __str__()
            return shoe

    print("Shoe not found.")
    return None

# Calculates the total value for each item ---> value = cost * quantity
def value_per_item(shoe):

    return shoe.cost * shoe.quantity


# Determines the product with the heighest quantity, then prints the shoe being for sale
def highest_qty():
    
    if not shoe_list:
        print("No shoes in inventory.")
        return None

    # Assume first shoe has highest quantity
    highest_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.quantity > highest_shoe.quantity:
            highest_shoe = shoe

    print("\nThis shoe is FOR SALE:")
    print(highest_shoe)

    return highest_shoe

def menu():
    read_shoes_data()   # Load file data into shoe_list

    while True:
        print("\n" + "=" * 50)
        print("Shoe Inventory Manager ")
        print("=" * 50)
        print("1. View all shoes")
        print("2. Add a new shoe")
        print("3. Search for a shoe")
        print("4. View value of a shoe")
        print("5. Restock lowest quantity shoe")
        print("6. View highest quantity shoe (FOR SALE)")
        print("0. Exit")
        print("=" * 50)

        choice = input("Select an option: ")

        if choice == "1":
            view_all(shoe_list)

        elif choice == "2":
            capture_shoes()

        elif choice == "3":
            search_shoe()

        elif choice == "4":
            shoe = search_shoe()
            if shoe:
                print(f"Total value: {value_per_item(shoe)}")

        elif choice == "5":
            restock(shoe_list)

        elif choice == "6":
            highest_qty()

        elif choice == "0":
            print("Exiting program. Goodbye")
            break

        else:
            print("Invalid option. Please try again.")