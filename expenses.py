# General way

# expenses = [10.5, 8, 5, 15, 20, 5, 3]

# sum = 0 

# for x in expenses:
#     sum = sum + x

# print('You spent $',sum, sep='')

# Another way is using built sum() function 
# total = sum(expenses)
# print('You spent $',total, sep='')



# We want the user to be able to enter their own expenses

total = 0 
expenses = []
num_expenses = int(input('Enter number of expenses:'))
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense:')))

total = sum(expenses)
print('You spent $',total, sep='')




