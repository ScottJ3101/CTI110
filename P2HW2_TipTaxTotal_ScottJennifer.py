# CTI-110 
# P2HW2 - Tip Tax Total 
# Jennifer Scott
# 02/18/2018

# Get the project total cost of a meal
total_tax = float(input('Enter the projected cost: '))

# Calculate the profit as 7 percent of tax
profit = total_tax * 0.07

# Display the tax
print('The tax is $', format(profit, ',.2f'))

# Get the project total cost of a meal
total_tip = float(input('enter the project cost: '))

# Calculate the profit as 18 percent of tip
profit = total_tip * 0.18

#Display the tip
print ('The tip is $', format(profit, ',.2f'))

#Display the profit
print ("The profit is $", format(profit, ",.2f"))
