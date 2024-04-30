#container of containers - menus is a list of lists

menus = [['Egg Sandwich', 'Coffee'],
         ['Rice', 'curd rice'],
         ['Soup','Salad']]


print(menus[1][1])


'''we could also use a dictionary for our menus with keys for Breakfast, Lunch, Dinner'''

menus_dict = { 'Breakfast' : ['Egg Sandwich', 'Coffee'],
              'Lunch' : ['Rice', 'curd rice'],
              'Dinner' : ['Soup','Salad']
}

for name, menu in menus_dict.items():
    print(name,':',menu)