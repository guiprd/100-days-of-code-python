def valid_bill_amount(bill_amount=0.0):
    if bill_amount <= 0:
        print("Bill amount must be greater than 0.")
        return False
    return True

def valid_number_of_people(number_of_people=0.0):
    if number_of_people <= 0:
        print("Number of people must be greater than 0.")
        return False
    return True

def valid_tip_percentage(tip_percentage=0):
    if tip_percentage not in [10, 12, 15]:
        print("Tip percentage is not standard. Please enter a valid percentage (10, 12, 15).")
        return False
    return True