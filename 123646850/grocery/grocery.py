grocery_list = [] # start with empty grocery list
# here used empty list because for me was easier to deal with

while True:
    try:
        order = input("").lower() # must be lower to catch if user inputs different case
        grocery_list.append(order) # otherwise python processes as different item
        continue # receives user input and adds these items to grocery list
    except KeyError:
        continue # catch any key error and return to prompt
    except EOFError:
        break # catch Ctr-D to end loop and run following block of code

#created dictionary which counts number of items using dict comprehension
# used sorted list to keep alphabetized list
word_counts = {word: grocery_list.count(word) for word in sorted(list(grocery_list))}
keys = word_counts.keys() # get item count as dict keys
values = word_counts.values() # get items as dict values

for item in zip(values, keys): # used zip method to create tuple of items and count
    final_order = (list(item)) # converted tuple back to list
    item_count = (final_order[0]) # assign variable to indexed item count
    final_order = final_order[1].upper() # assign variable to indexed uppercase item
    print(f"{item_count} {final_order}") # print formatted output