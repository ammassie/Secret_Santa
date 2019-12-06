import random
import numpy as np

name_list = np.empty(0)     # List of names of those participating in Secret Santa
couples = np.empty(0)       # List of couples
chosen = np.empty(0)        # List for once your name is picked 

def already_chosen(giftee, chosen):
    # This function checks to see if your name has already been picked
    if len(chosen) == 0:
        return False
    else:
        if giftee in chosen:
            return True
        else:
            return False
            
def check_if_couple_chosen(gifter,giftee,couples):
    # This function checks to see if someone picked their sig. other
    if gifter in couples[:,0]:
        couple_group = couples[np.where(gifter == couples[:,0])[0][0]]
        if giftee == couple_group[1]:
            print "Error: SO picked SO"
            return True
        else:
            return False
            
def choose_giftee(gifter, name_list):
    # This function choses the giftee at random
    mask = np.ma.masked_array(name_list != gifter)
    giftee = random.choice(name_list[mask==True]) #initial pick 
    return giftee


num_names = int(raw_input("Enter how many people are in this gift swap: "))

# This loop allows for you to enter names in the program
# I was tired of writing everyones names in to the prompts, so I made lists instead (below commented section)

#for i in range(num_names):
#    print "Type name: "
#    name = raw_input()
#    name_list = np.append(name_list, name)
#    print "Is this person in a couple? (yes/no)"
#    couple_boolean = raw_input()
#    if couple_boolean == "yes":
#        print "Who is their SO?"
#        sig_other = raw_input()
#        if len(couples) == 0:
#            couples = np.array([name, sig_other])
#        else:
#            couples = np.vstack((couples, [name, sig_other]))

name_list = np.array(['Sean', 'Rose', 'Ruston', 'Jackie','Ricky', 'Katelyn', 'Steve', 'Katie', 'Eric', 'Brooke', 
'Grace', 'Brian', 'Sam', 'Kate', 'Michael'])
couples = np.array([['Ricky', 'Katelyn'],
       ['Katelyn', 'Ricky'],
       ['Steve', 'Katie'],
       ['Katie', 'Steve'],
       ['Sean', 'Rose'],
       ['Rose', 'Sean'],
       ['Ruston', 'Jackie'],
       ['Jackie', 'Ruston']])


restart = True
restart_count = 0

while restart == True:
    chosen = np.empty(0)
    for i in range(num_names):
        gifter = name_list[i] 
        giftee = choose_giftee(gifter, name_list)
    
        # this while loop checks that you didn't pick your sig. other, you didn't pick yourself, 
        # and you didn't pick someone already picked. If you did, it'll either pick someone new or start over
        
        while check_if_couple_chosen(gifter,giftee,couples) == True or already_chosen(giftee, chosen) == True or giftee == gifter:
            #print check_if_couple_chosen(gifter,giftee,couples)
            #print already_chosen(giftee, chosen)
            #print giftee == gifter
            if num_names - len(chosen) == 1:
                #for i in range(len(chosen)):
                #    print name_list[i-1], '--->', chosen[i-1]
                print "OOPS! Let's try again!"
                #raw_input()
                restart = True
                restart_count += 1
                break
            else:
                giftee = choose_giftee(gifter, name_list)
                restart = False
                
        chosen = np.append(chosen, giftee) # this is the list of people already picked

print "All done! Here are your gifting assignments: \n"
for i in range(num_names):
    print name_list[i], " --> ", chosen[i]
       
    #print "You, " + str(gifter) + ", have " + str(giftee) + " for secret santa."
    #raw_input("Please write OK, and then pass to next person: ")
    #os.system('clear')