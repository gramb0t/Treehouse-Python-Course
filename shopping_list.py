# Shopping List program
# what do we want it to do?
    # run the script to start using it
    # put new things into the list one by one
    # enter DONE to quit
    # show all items on list

# simple right?

#make list to hold onto stuff
shopping_list = []

#print instructions
print("awwwww yeah, shopping time!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Add items to the list below")
print("""
Enter HELP for more information.
Enter SHOW to see the list.
Enter DONE to quit.""")
    

#add new item function
def add_new(new_item):
    shopping_list.append(new_item)
    print("{} has been added, there are now {} entries".format(new_item, len(shopping_list)))
    return new_item

#Show Help Function
def show_help(): 
    print("help menu v1.0")
    print("~~~~~~~~~~~~~~")
    print("To add an item, enter the item.")
    print("To see the list, type SHOW.")
    print("To see Help menu, type HELP.")
    print("To exit, type DONE.")

#Show List Function
def show_list() :
    if len(shopping_list) == 0:
            print("the list is empty")
    else:
        print("The List and its {} entries!".format(len(shopping_list)))
        for item in shopping_list:
            print(item)
        print("such a nice list, its got {} items".format(len(shopping_list)))
    
#ask for new items
while True:
    new_item = input("{}> ".format(len(shopping_list)))
    
    #quitting the app
    if new_item == 'DONE':
        break
  
    #show help
    elif new_item == 'HELP':
        show_help()
        continue
    #show list       
    elif new_item == 'SHOW':
        show_list()
        continue
    #none of the above, add a new item 
    else:
        add_new(new_item)

