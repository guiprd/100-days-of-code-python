from validations import *

def divide_total_bill(bill_amount, number_of_people):
    return bill_amount / number_of_people

def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * tip_percentage / 100

if __name__ == '__main__':
    while True:
        try:
            bill_amount = float(input("Enter the bill amount: "))
            while not valid_bill_amount(bill_amount):
                bill_amount = float(input("Enter the bill amount: "))

            number_of_people = int(input("Enter the number of people: "))
            while not valid_number_of_people(number_of_people):
                number_of_people = int(input("Enter the number of people: "))

            tip_percentage = int(input("Enter the tip percentage 10, 12 or 15: "))
            while not valid_tip_percentage(tip_percentage):
                tip_percentage = float(input("Enter the tip percentage 10, 12 or 15: "))

            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

    total_bill = bill_amount + calculate_tip(bill_amount, tip_percentage)
    amount_per_person = divide_total_bill(total_bill, number_of_people)
    print(f"Total bill per person: ${amount_per_person:.2f}")
