import wikipedia

def start():
    """This is the intro of the President's game, allowing you to input your name and location,
    assessing your knowledge and giving you a recommendation on which level, the user 
    ultimately deciding which level to play, and then starts that level.
    
    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    # input name and location to print a custom welcome message
    name = input("What's your name? ")
    location = input("Where are you joining us from? ")
    print("\nHello {}, and welcome to the All About The Presidents!\n"
          "I see that you're joining us from {}, great to have you here!\n"
          "In this quiz game you'll be answering trivia questions\n"
          "about the U.S. Presidents.\n".format(name, location))
    
    # assesses knowledge of presidents and recommends which level
    knowledge = int(input("On a scale of 1-10, how much do you think you know about the U.S. Presidents? "))
    if knowledge < 4:
        statement = ("I see that you don't know too much about the presidents\n"
        "so I recommend you try the easy difficulty -- but feel free to\n"
        "choose any difficulty that you want -- especially if you want a challenge!\n")
    elif knowledge < 7:
        statement = ("I see that you know a decent amount about the presidents\n"
        "so I recommend you try the medium difficulty -- but feel free to\n"
        "choose any difficulty that you want -- especially if you want a challenge!\n")
    else:
        statement = ("I see that you know a lot about the presidents\n"
        "so I recommend you try the hard difficulty -- but feel free to\n"
        "choose any difficulty that you want!\n")    
    print(statement)
    
    # selecting which difficulty
    select_difficulty = input("What difficulty do you want(easy, medium, or hard)?")
    if select_difficulty == "easy":
        easy()
    elif select_difficulty == "medium":
        medium()
    elif select_difficulty == "hard":
        hard()

def easy():
    """This is the easy difficulty, asking you 3 easy questions, 
    providing you your final score, and printing out the number
    of U.S. Flags according to your score. Then, transitions to
    the learn_more() function.
    
    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    # initalizes score to 0
    score = 0
    print("You selected easy, great choice! Here's your first question:\n" 
          "(make sure to type first and last name, all lowercase)")
          
    question_1 = input("\nWho was the first U.S. President? ")
    if question_1 == "george washington":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was George Washington.")
        print("Your score is " + str(score)) 
          
    question_2 = input("\nWho is the current U.S. President? ")
    if question_2 == "joe biden":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Joe Biden.")
        print("Your score is " + str(score)) 
          
    question_3 = input("\nWhich President ended slavery and is on the U.S. Penny? ")
    if question_3 == "abraham lincoln":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Abraham Lincoln.")
        print("\nCongrats! Your final score is " + str(score)) 
    
    print(star(score))
    
    learn_more()
    
def medium():
    """This is the medium difficulty, asking you 3 medium questions, 
    providing you your final score, and printing out the number
    of U.S. Flags according to your score. Then, transitions to
    the learn_more() function.
    
    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    # initalizes score to 0
    score = 0
    print("You selected medium, great choice! Here's your first question:\n" 
          "(make sure to type first and last name, all lowercase)")
          
    question_1 = input("\nWho is the oldest president ever? ")
    if question_1 == "jimmy carter":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Jimmy Carter.")
        print("Your score is " + str(score)) 
          
    question_2 = input("\nWhich President's campaign slogan was 'I like Ike'? ")
    if question_2 == "dwight d. eisenhower":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Dwight D. Eisenhower.")
        print("Your score is " + str(score)) 
          
    question_3 = input("\nWho was the first President to be impeached? ")
    if question_3 == "andrew johnson":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Andrew Johnson.")
        print("\nCongrats! Your final score is " + str(score)) 
    
    print(star(score))
        
    learn_more()
    
def hard():
    """This is the hard difficulty, asking you 3 hard questions, 
    providing you your final score, and printing out the number
    of U.S. Flags according to your score. Then, transitions to
    the learn_more() function.
    
    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    # initalizes score to 0
    score = 0
    print("You selected hard, great choice! Here's your first question:\n" 
          "(make sure to type first and last name, all lowercase)")
          
    question_1 = input("\nWho was the only President to serve 2 non-consecutive terms? ")
    if question_1 == "grover cleveland":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Grover Cleveland.")
        print("Your score is " + str(score)) 
          
    question_2 = input("\nWho first the first president to have electricity in the White House? ")
    if question_2 == "benjamin harrison":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was Benjamin Harrison.")
        print("Your score is " + str(score)) 
          
    question_3 = input("\nWhich president also served as Chief Justice of the Supreme Court? ")
    if question_3 == "william howard taft":
        print("You're right!")
        score += 1
        print("Your score is " + str(score))
    else:
        print("Sorry, the answer was William Howard Taft.")
        print("\nCongrats! Your final score is " + str(score)) 
    
    print(star(score))
    
    learn_more()

def star(score):
    """Prints out the number of U.S. flags according to your score.
    
    Parameters
    ----------
    score : int
        Score that you got in the quiz.
    
    Returns
    -------
    num_star : str
        The number of U.S. flags according to your score.
    """
    
    num_star = ("🇺🇸")
    return(num_star * score)
    
    
    
def learn_more():
    """In this function, you get to learn more about the Presidents
    (if you want), providing a President's Wikipedia summary and
    a link to their picture.
    
    PARAMETERS
    ----------
    none

    RETURNS
    -------
    none
    """
    
    # initalizes end to False
    end = False
    
    # continues asking which president the user would
    # like to learn more about until they don't
    # respond yes
    while end != True:
        learn_bool = input("\nWould you like to learn more about the Presidents? (respond yes or no) ")
        
        if learn_bool == "yes":
            prez = input("Great! Write a president you would like to learn more about: ")
            
            # initalizes counter to 0 and found_image to false; 
            # it loops through all the images on whatever president
            # the user inputted until it finds a picture url that contains
            # "White" or "portrait", since the pictures on each president's
            # page are not just of them
            counter = 0
            found_image = False
            while found_image == False:
                image = wikipedia.page("{}".format(prez)).images[counter]
                if (image.find("White") > 0) or (image.find("portrait") > 0):
                    print("Here's a picture of {}:".format(prez))
                    print(image)
                    found_image = True    
                else:
                    counter += 1
            
            print(wikipedia.summary(prez))
        
        else: 
            print("No worries, hope you enjoyed the game! Have a great day :) ")
            end = True
            break
