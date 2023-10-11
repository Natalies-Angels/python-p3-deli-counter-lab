katz_deli =[]

def line(katz_deli):
    customer_line = "The line is currently: "
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
         for i in range(len(katz_deli)):
             if i < len(katz_deli) - 1:
                 customer_line += str(i + 1) + ". " + katz_deli[i] + " "
             else:
                 customer_line += str(i + 1) + ". " + katz_deli[i]
         print(customer_line)

def take_a_number(katz_deli, customer):
    katz_deli.append(customer)
    # line(katz_deli)
    print(f"Welcome, {customer}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = katz_deli.pop(0)
        print(f"Currently serving {current_customer}.")

take_a_number(katz_deli, "Logan")
take_a_number(katz_deli, "Avi")
take_a_number(katz_deli, "Spencer")

now_serving(katz_deli)
