#for customer name
while True:
    customer_name = input("Enter your Name: ").strip()
    valid = True  

    for ch in customer_name:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
            valid = False
            break

    if customer_name != "" and valid:
        break
    else:
        print("Only characters are allowed.")
#for customer_id
while True:
    customer_id = input("Enter customer id: ").strip()
    valid = True

    for num in customer_id:
        if not ('0' <= num <= '9'):
            valid = False
            break

    if customer_id != "" and valid:
        break
    else:
        print("Only integers are allowed.")

#for number_of_items        
while True:
    number_of_items = input("Enter no. of items purchased: ").strip()
    valid = True
    for num in number_of_items:
        if not ('0' <= num <= '9'):
            valid = False
            break
    if number_of_items != "" and valid:
        break
    else:
        print("Only integers are allowed.")

number_of_items = int(number_of_items)
#Part A – Customer Information
#Accept customer name.
#Accept customer ID.
#Accept the number of items purchased



if number_of_items <=0:
    print("Number of items must be greater than Zero.")
else:
    purchased_items=[]
    item_names=[]
    item_quantities=[]
    item_prices=[]
    total_item_prices=[]

for item_number in range(1,number_of_items +1):
    print("\nEnter details of item ",item_number)

    while True:
      item_name=str(input("\nEnter name of the item :")).strip()
      valid =True
      for ch in item_name:
          if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
              valid=False
              break
      if item_name !="" and valid:
          break
      else:
          print("only characters are allowed.")



    while True:
       item_quantity = input("Enter no.of items: ")

       valid_quantity = True

       if item_quantity == "":
           valid_quantity = False

       for character in item_quantity:
           if character < "0" or character > "9":
              valid_quantity = False
              break

       if valid_quantity == False:
           print("Only integers are allowed.")
           continue

       item_quantity = int(item_quantity)

       if item_quantity <= 0:
          print("Quantity should be more than zero.")
          continue

       break


# Price validation

    while True:
        item_price = input("Enter item per price: ")

        valid_price = True
        decimal_count = 0

        if item_price == "":
            valid_price = False

        for character in item_price:
           if character == ".":
               decimal_count = decimal_count + 1

               if decimal_count > 1:
                   valid_price = False
                   break

           elif character < "0" or character > "9":
               valid_price = False
               break

        if valid_price == False:
            print("Only numbers are allowed.")
            continue

        item_price = float(item_price)

        if item_price <= 0:
            print("Price should be more than zero.")
            continue

        break
    total_price=item_quantity*item_price

    item_tuple=(item_name,item_quantity,item_price,total_price)

    item_dictionary={
        "Name":item_name,
        "Quantity":item_quantity,
        "Price":item_price,
        "Total Price":total_price
    }

    purchased_items.append(item_dictionary)
    item_names.append(item_name)
    item_quantities.append(item_quantity)
    item_prices.append(item_price)
    total_item_prices.append(total_price)

    print("Item added successfully.")
# Part B – Item Entry
# Using a loop, allow the user to enter:
# Item Name
# Quantity
# Price per Unit
# Store the information using appropriate Python data structures
#  (Lists, Tuples, Dictionaries)



# Billing
overall_bill = 0
for price in total_item_prices:
    overall_bill = overall_bill + price


discount = 0

if overall_bill > 5000:
    discount = 15
elif overall_bill >= 3000 and overall_bill <= 5000:
    discount = 10
elif overall_bill >= 1000 and overall_bill < 3000:
    discount = 5
else:
    discount = 0
    pass
final_discount = overall_bill * discount / 100
final_amount = overall_bill - final_discount
# Part C – Billing
# Calculate:
# Total amount for each item
# Overall bill amount
# Apply the following discount rules:
# Bill greater than ₹5000 → 15% Discount
# Bill between ₹3000 and ₹5000 → 10% Discount
# Bill between ₹1000 and ₹2999 → 5% Discount
# Otherwise → No Discount
# Display:
# Total Bill
# Discount Amount
# Final Payable Amount


#summary
print("--------PURCHASE SUMMARY-------")

print("Customer Name :", customer_name)
print("Customer ID   :", customer_id)

print("\n---------------Purchased Items----------------")
print("\nItem Name | Quantity | Unit Price | Total Price")

if len(purchased_items) == 0:
    print("No valid items were entered.")
else:
    for item in purchased_items:
        print(
            item["Name"], "     |",
            item["Quantity"], "       |",
            "₹", format(item["Price"], ".2f"), "   |",
            "₹", format(item["Total Price"], ".2f")
        )

print("\nTotal Bill           : ₹", format(overall_bill, ".2f")) 
print("Discount Percentage  :", discount, "%")
print("Discount Amount      : ₹", format(final_discount, ".2f"))
print("Final Payable Amount : ₹", format(final_amount, ".2f"))
print("\n-----------Thank you for shopping!-------------")
# Part D – Purchase Summary
# Display:
# Customer Details
# List of Purchased Items
# Quantity
# Unit Price
# Total Price
# Final Bill Amount