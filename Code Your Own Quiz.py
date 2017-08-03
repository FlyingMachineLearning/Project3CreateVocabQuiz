#Variables that feed into the arguments of their distinctive and unique functions
#Probably could have made a list of lists...
mild_set = ["A hamburger does not contain __1__. A cheeseburger does contain __2__. The bread surrounding a burger is called a __3__. Sometime you can have two __4__.", ["ham","cheese","bun","patties"]]
medium_set = ["Weather can be __1__. The color __2__ is made of yellow and blue. Pokemon is short for '__3__ monsters'. Salt goes with __4__.", ["rainy","green","pocket","pepper"]]
hot_set = ["I got that __1__ in my __2__. Got that good __3__ in my __4__.", ["sunshine","pocket","soul","feet"]]
tamale_set = ["A __1__ is 1/100th of a second. The things on a fork are called __2__. A palindrome in sentence form is a __3__. The dots on a pair of dice are called the __4__.", ["jiffy","tines","chiasmus","pips"]]
tamale_plus_set = ["Put these in order: __1__, __2__, __3__, __4__.", ["celeste","electric","cyan","cobalt"]]

#during the 'brain' process, when a word matches, this replaces the blank number with the actual word 
#tied to 'answer_currently_on' in 'brain' function
#hard-coded, assumes parameters the way they were built in format __N__
#returns the paragraph with the actual word, keeping the remaining words hidden
def replace_words(choice,word,sentence):
    choice = "__"+str(choice)+"__"
    for i in range(len(sentence)):
        if sentence[i:i+5] == choice:
            sentence = sentence[:i]+word+sentence[i+5:]
    print sentence 
    return sentence

#during the 'brain' process, this removes the correct choice the user made
#returns a list, without the correct choice
def pop_element(list_to_change,item_to_remove):
    total = 0
    for item in list_to_change:
        if item == item_to_remove:
            list_to_change.pop(total)
        total += 1
    return list_to_change

#during the 'brain' process, this parses a list into a string with commas
#in retrospect, i think there's a built-in function I could have used.
def print_all_elements(list_to_print):
    part = ""
    for num in range(len(list_to_print)):
        part = " " + list_to_print[num] + "," + part 
    return part

#this is what makes all the magic happens. 
#After the user selects their level, this is the loop that controls
#how far they are into guessing.
#brings user back to main menu when finished or they are sick of the quiz
#hard coded with four answers :/
def brain(new_sentence,proper_answer,rearranged_items):
    answer_currently_on = 1
    while True:
        answer = raw_input("What goes next?\n")
        if answer == "M" or answer == "M":
            break
        elif answer == proper_answer[answer_currently_on-1] and answer_currently_on == 4:
            new_sentence = replace_words(answer_currently_on,proper_answer[answer_currently_on-1],new_sentence)
            print "\nNice! Well done!\n\nBack to the menu"
            break
        elif answer == proper_answer[answer_currently_on-1] and answer_currently_on != 4:
            print "Yes! Your options are now:" + print_all_elements(pop_element(rearranged_items,answer))
            new_sentence = replace_words(answer_currently_on,proper_answer[answer_currently_on-1],new_sentence)
            answer_currently_on += 1
        else:
            print "No, try again" 
    intro()

################################################################################
#Along with the individual functions, probably some opportunity for refactoring#
################################################################################

#this handles the choices the user makes by taking in the arguments defined in the variables earlier
def mapping(introchoice):
    if introchoice == "1":
        mild(mild_set[0],mild_set[1])
    elif introchoice == "2":
        medium(medium_set[0],medium_set[1])
    elif introchoice == "3":
        hot(hot_set[0],hot_set[1])
    elif introchoice == "4":
        tamale(tamale_set[0],tamale_set[1])
    elif introchoice == "5":
        tamale_plus(tamale_plus_set[0],tamale_plus_set[1])
    else:
        return None
    
#the first thing the user sees
#it's a menu where they can select their level of difficulty or leave
#sends to mapping
def intro():
    message = """Welcome to this Vocab Quiz!
    How spicy do you want your quiz?
    1 - Mild
    2 - Medium
    3 - Hot
    4 - Tamale
    5 - Tamale Plus
    Q - Also you can leave. 
    """
    choice = raw_input(message)
    mapping(choice)

##############################################################
#A lot of repetition here, lot of opportunity for refactoring#
##############################################################

#very easy mode
#includes user interaction
#the options are a hard-coded rearrangement of the answer key
def mild(paragraph, key):
    opening_choices = "Here are your choices: " + key[2] + ", " + key[0] + ", " + key[1] + ", " + key[3] + " or go back to the menu with 'M' "
    options = [key[2],key[0],key[1],key[3]]
    print "You've picked Mild. Great! Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices 
    brain(paragraph, key, options)

#easy mode
#includes user interaction
#the options are a hard-coded rearrangement of the answer key        
def medium(paragraph, key):
    opening_choices = "Here are your choices: " + key[3] + ", " + key[2] + ", " + key[1] + ", " + key[0] + " or go back to the menu with 'M' "
    options = [key[3],key[2],key[1],key[0]]
    print "You've picked Medium. Good for you! Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices
    brain(paragraph, key, options)

#right in between easy and hard mode
#includes user interaction
#the options are a hard-coded rearrangement of the answer key    
def hot(paragraph, key):
    opening_choices = "Here are your choices: " + key[0] + ", " + key[2] + ", " + key[3] + ", " + key[1] + " or go back to the menu with 'M' "
    options = [key[0],key[2],key[3],key[1]]
    print "You've picked Hot. Like a challenge, eh? Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices
    brain(paragraph, key, options)

#hard mode
#includes user interaction
#the options are a hard-coded rearrangement of the answer key
def tamale(paragraph, key):
    opening_choices = "Here are your choices: " + key[3] + ", " + key[1] + ", " + key[2] + ", " + key[0] + " or go back to the menu with 'M' "
    options = [key[3],key[1],key[2],key[0]]
    print "You've picked Tamale. Amazing! Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices
    brain(paragraph, key, options)

#very hard mode
#includes user interaction
#the options are a hard-coded rearrangement of the answer key
def tamale_plus(paragraph, key):
    opening_choices = "Here are your choices: " + key[2] + ", " + key[0] + ", " + key[1] + ", " + key[3] + " or go back to the menu with 'M' "
    options = [key[2],key[0],key[1],key[3]]
    print "You've picked Tamale Plus. Brave! Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices
    brain(paragraph, key, options)

#starts everything
intro()
