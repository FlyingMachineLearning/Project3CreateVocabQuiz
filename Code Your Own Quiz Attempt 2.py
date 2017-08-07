"""
Variables that feed into the arguments of the game function
"""
game_data = {
    "mild_set":
        ["Mild",
        "A hamburger does not contain __1__. "
        + "A cheeseburger does contain __2__. "
        + "The bread surrounding a burger is called a __3__. "
        + "Sometimes you can have two __4__. ",
        ["ham","cheese","bun","patties"],
        ["bun","ham","cheese","patties"]],
    "medium_set":
        ["Medium",
        "Weather can be __1__. "
        + "The color __2__ is made of yellow and blue. "
        + "Pokemon is short for 'pocket __3__'. "
        + "Salt goes with __4__.",
        ["rainy","green","monsters","pepper"],
        ["pepper","monsters","green","rainy"]],
    "hot_set":
        ["Hot",
        "I got that __1__ "
        + "in my __2__. "
        + "Got that good __3__ "
        + "in my __4__.",
        ["sunshine","pocket","soul","feet"],
        ["soul","feet","sunshine","pocket"]],
    "tamale_set":
        ["Tamale",
        "A __1__ is 1/100th of a second. "
        + "The things on a fork are called __2__. "
        + "A palindrome in sentence form is a __3__. "
        + "The dots on a pair of dice are called the __4__.",
         ["jiffy","tines","chiasmus","pips"],
         ["pips","jiffy","chiasmus","tines"]],
    "extra_set":
        ["EXTRA",
        "Put these in order: __1__, "
        + "__2__, "
        + "__3__, "
        + "__4__.",
         ["celeste","electric","cyan","cobalt"],
         ["electric","cyan","cobalt","celeste"]]
    }



def replace_words(choice,word,sentence):
    """
    during the 'brain' process, when a word matches, this replaces the blank number with the actual word 
    tied to 'answer_currently_on' in 'brain' function
    hard-coded, assumes parameters the way they were built in format __N__
    returns the paragraph with the actual word, keeping the remaining words hidden
    """
    choice = "__"+str(choice)+"__"
    parsing_length = 5
    for i in range(len(sentence)):
        if sentence[i:i+parsing_length] == choice:
            sentence = sentence[:i]+word+sentence[i+parsing_length:]
    print sentence 
    return sentence

def pop_element(list_to_change,item_to_remove):
    """
    during the 'brain' process, this removes the correct choice the user made
    returns a list, without the correct choice
    """
    total = 0
    for item in list_to_change:
        if item == item_to_remove:
            list_to_change.pop(total)
        total += 1
    return list_to_change

def print_all_elements(list_to_print):
    """
    during the 'brain' process, this parses a list into a string with commas
    """
    part = ""
    for num in range(len(list_to_print)):
        part = " " + list_to_print[num] + "," + part 
    return part

def brain(new_sentence,proper_answer,rearranged_items):
    """
    this is what makes all the magic happens. 
    After the user selects their level, this is the loop that controls
    how far they are into guessing.
    brings user back to main menu when finished or they are sick of the quiz
    hard coded with four answers :/
    """
    answer_currently_on = 1
    max_answer = 4
    while True:
        answer = raw_input("What goes next?\n").lower()
        if answer == "m":
            break
        elif answer == proper_answer[answer_currently_on-1] and answer_currently_on == max_answer:
            new_sentence = replace_words(answer_currently_on,proper_answer[answer_currently_on-1],new_sentence)
            print "\nNice! Well done!\n\nBack to the menu"
            break
        elif answer == proper_answer[answer_currently_on-1] and answer_currently_on != max_answer:
            print "Yes! Your options are now:" + print_all_elements(pop_element(rearranged_items,answer))
            new_sentence = replace_words(answer_currently_on,proper_answer[answer_currently_on-1],new_sentence)
            answer_currently_on += 1
        else:
            print "No, try again" 
    intro()

def mapping(introchoice):
    """
    this handles the choices the user makes by taking in the arguments defined in the variables earlier
    """
    if introchoice == "1" or introchoice == "mild":
        game(game_data["mild_set"][0],game_data["mild_set"][1],game_data["mild_set"][2],game_data["mild_set"][3])
    elif introchoice == "2" or introchoice == "medium":
        game(game_data["medium_set"][0],game_data["medium_set"][1],game_data["medium_set"][2],game_data["medium_set"][3])
    elif introchoice == "3" or introchoice == "hot":
        game(game_data["hot_set"][0],game_data["hot_set"][1],game_data["hot_set"][2],game_data["hot_set"][3])
    elif introchoice == "4" or introchoice == "tamale":
        game(game_data["tamale_set"][0],game_data["tamale_set"][1],game_data["tamale_set"][2],game_data["tamale_set"][3])
    elif introchoice == "5" or introchoice == "extra":
        game(game_data["extra_set"][0],game_data["extra_set"][1],game_data["extra_set"][2],game_data["extra_set"][3])
    elif introchoice == "q":
        return None
    else:
        print "Sorry, didn't get that.\nHere are your choices again"
        intro()
    

def intro():
    """
    the first thing the user sees
    it's a menu where they can select their level of difficulty or leave
    sends to mapping
    """
    message = """Welcome to this Vocab Quiz!
    How spicy do you want your quiz? (Enter a number or the word)
    1 - Mild
    2 - Medium
    3 - Hot
    4 - Tamale
    5 - EXTRA
    Q - Also you can leave. 
    """
    choice = raw_input(message).lower()
    mapping(choice)

def game(level, paragraph, key, options):
    """
    This provides the initial state of the quiz
    """
    user_choices = ", ".join(options)
    opening_choices = "Here are your choices: " + user_choices + " or go back to the menu with 'M' "
    print "You've picked " + level + ". Great! Here's your Vocab Quiz:\n"+paragraph+"\n"
    print opening_choices 
    brain(paragraph, key, options)

"""    
starts everything
"""
intro()
