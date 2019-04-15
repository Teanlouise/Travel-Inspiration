""" Travel Inspiration - CSSE1001 - Assignment 1

A travel recommendation program. The user will be given a questionaire that
matches their travel preferences to the 'destination' database to return the
best match for the user.
"""

__author__ = "Tean-louise McGrath (42637460)"
__date__ = "29.03.19"


from destinations import Destinations

def get_user_preference(question, valid_range):
    """ Ask the user a question about their travel preference and return the
    input as a string. Also, check if input is valid.

    Paramaters:
        question (str): Question to print for travel preference paramater
        valid_range (list): List of strings that are valid inputs. Each
        preference has unique range.

    Variables:
        user_input (str): Input from user in response to question

    Return:
        str: Return of input()
    """
    
    print(question)
    user_input = input("> ")
    print ("")
    while user_input not in valid_range:
        print ("I'm sorry, but ", user_input, " is not a valid choice."
               " Please try again.\n", sep="")
        print (question)
        user_input = input("> ")
        print ("")

    return user_input

def get_user_interest(database_list, user_list):
    """ Ask user a question about how much they like an interest from -5 to 5.
    Loop through lists of interests and store use inputs in new list.

    Paramaters:
        database_list (list): List of interests.
        user_input (list): User inputs stored as int in order of interest list.
    """

    for interest in database_list:
        print ("How much do you like ", interest,"? (-5 to 5)", sep = "")
        user_input = int(input("> "))
        print ("")
        while user_input not in range(-5,6):
            print ("I'm sorry, but ", user_input, " is not a valid choice."
                   " Please try again.\n", sep="")
            print ("How much do you like ", interest,"? (-5 to 5)", sep = "")
            user_input = int(input("> "))
            print ("")
        user_list.append (user_input)

def match_continent(user_input, database_value):
    """ Matches the user's input for 'Continent' with the data from destinations.

    Paramaters:
        user_input (int): User's input when prompted for 'continent' preference.
        database_value (str): Continent name stored in destinations database.

    Variables:
        destination_continent (str): Name of the continent according to the
        user's input to match to database.

    Return:
        bool: Destination is match (True), if and only if, the destination of
        the continent is an exact match for user.
    """

    if user_input==1:
        destination_continent = "asia"
    elif user_input==2:
        destination_continent = "africa"
    elif user_input==3:
        destination_continent = "north america"
    elif user_input==4:
        destination_continent = "south america"
    elif user_input==5:
        destination_continent = "europe"
    elif user_input==6:
        destination_continent = "oceania"
    elif user_input==7:
        destination_continent = "antarctica"

    # Return True if user input matches database value, else False
    return (database_value == destination_continent)

def match_cost(user_input, database_value):
    """ Match the user's input for 'cost' with the data from the database.
    Convert string inputs of user and database to integers to compare.

    Paramaters:
        user_input (str): User's input when prompted for 'cost' preference.
        database_value (str): Cost of destination stored in database.

    Variables:
        user_cost_int (int): Converts the users string input to int.
        destination_cost_int (int): Converts the database string values to int.

    Return:
        bool: Destination is match (True) if the 'cost' of the destination in
        the database is less than or equal to the user's input.
    """

    if user_input=="$$$":
        user_cost_int = 3
    elif user_input=="$$":
        user_cost_int = 2
    elif user_input=="$":
        user_cost_int = 1

    if database_value =="$$$":
        destination_cost_int = 3
    elif database_value =="$$":
        destination_cost_int = 2
    elif database_value =="$":
        destination_cost_int = 1

    # Return True if user input is >= the database value, else False
    return (user_cost_int >= destination_cost_int)

def match_children(user_input, database_value):
    """ Match the user's input for 'kid friendly' with the database.

    Paramaters:
        user_input (int): User's input when prompted for 'kid friendly'
        database_value (bool): Stored in database as True (Yes) or False (No)

    Return:
        bool: True, if the user selects kid friendly (user input 1) and the
        destination is True. Or if user selects no preference (user input 2).
    """

    # User requires kid friendly. Return True if kid friendly, else False
    if user_input == 1:
        return database_value
    # User has no preference. So all countries match, always return True
    else:
        return True


def match_crime(user_input, database_value):
    """ Match the user's input for 'crime' with database.

    Paramaters:
        user_input (int): User's input when prompted for 'crime' preference.
        database_value (str): String value of crime level in database.
    Variables:
        destination_crime (int): Converts the database string values to int.

    Return:
        bool: Return True if 'crime' value of user input >= database value.
    """

    if database_value == "low":
        destination_crime = 1
    elif database_value == "average":
        destination_crime = 2
    elif database_value == "high":
        destination_crime = 3

    # Return True if user input >= database value, else False
    return user_input >= destination_crime

def match_climate (user_input,database_value):
    """ Match the user's input for 'climate' with the database.

    Paramaters:
        user_input (int): User's input when prompted for 'climate' preference.
        database_value (str): Climate description name stored in database.

    Variables:
        destination_climate (int): Converts the database string values to int.

    Return:
        bool: Return True if 'climate' value in database matches the user input.
    """

    if database_value == "cold":
        destination_climate = 1
    elif database_value== "cool":
        destination_climate = 2
    elif database_value == "moderate":
        destination_climate = 3
    elif database_value == "warm":
        destination_climate = 4
    elif database_value == "hot":
        destination_climate = 5

    # Return True if user input matches database value, else False
    return user_input == destination_climate

def match_season (user_input):
    """ Match the user's input for 'season' with the corresponding string name.

    Paramaters:
        user_input (int): User's input when prompted for 'season' preference.

    Variables:
        destination_season (str): Store season name according to user input.

    Return:
        str: The season name corresponding to user input.
    """

    if user_input == 1:
        destination_season = "spring"
    elif user_input == 2:
        destination_season = "summer"
    elif user_input == 3:
        destination_season = "autumn"
    elif user_input == 4:
        destination_season = "winter"

    # Return string name of season
    return destination_season

def match_interest (user_input, dest):
    """ Match the user's input for 'interest' with the destination value.

    Paramaters:
        user_input (list): List of user's input according to each interest.
        Each interest value in list stored as float in order.
        dest (Destination): Destination being checked from database.

    Variables:
        sports_score (float): user input for 'sports' * database score
        [same for wildlife, nature, historical, cuisine, adventure, beach]

    Return:
        float: The sum of all of the interests scores.
    """

    # Get the value of each interest from the database.
    # Interest score = user input * database value
    sports_score = user_input[0] * dest.get_interest_score("sports")
    wildlife_score = user_input[1] * dest.get_interest_score("wildlife")
    nature_score = user_input[2] * dest.get_interest_score("nature")
    historical_score = user_input[3] * dest.get_interest_score("historical")
    cuisine_score = user_input[4] * dest.get_interest_score("cuisine")
    adventure_score = user_input[5] * dest.get_interest_score("adventure")
    beach_score = user_input[6] * dest.get_interest_score("beach")

    # Return sum of all the interest scores
    return (sports_score + wildlife_score + nature_score + historical_score +
            cuisine_score + adventure_score + beach_score)

def main():
    """ Logic for Travel program. The user will be asked a number of questions
    and an exact match (or None) will be returned based on parameters.

    Variables:
        final_match (bool): Exact match based on parameters. Start as FALSE.
        greatest_score (int): Value start at -200 (min score for any destination)
        user_xxx (misc): User input for each question. 
        interest_score (int): Sum of all interest scores for destination.
        season_factor (float): Season factor of destination based on user input.
        destination_score (float): Total score is interest score * season factor.

    Return:
        Destination name:  if match for continent, kid friendly, cost, crime and
        climate. The destination will have the greatest destination score.
        OR "None" if no match.
    """

    #INTRODUCTION - Welcome and name
    print ("Welcome to Travel Inspiration!\n")
    user_name = input("What is your name? ")
    print ("\nHi, ", user_name, "!\n", sep="")

    #TRAVEL PREFERENCE INPUTS - Continent, Money, Children, Season, Climate
    user_continent = int(get_user_preference("Which continent would you like to travel to?\n"
        "  1) Asia\n  2) Africa\n  3) North America\n  4) South America\n  5) Europe\n"
        "  6) Oceania\n  7) Antarctica", ["1","2","3","4","5","6","7"]))
    user_cost = get_user_preference("What is money to you?\n"
        "  $$$) No object\n  $$) Spendable, so long as I get value from doing so\n"
        "  $) Extremely important; I want to spend as little as possible", ["$$$", "$$","$"])
    user_crime = int(get_user_preference("How much crime is acceptable when you travel?\n"
        "  1) Low\n  2) Average\n  3) High", ["1","2","3"]))
    user_children = int(get_user_preference("Will you be travelling with children?\n"
        "  1) Yes\n  2) No", ["1","2"]))
    user_season = float(get_user_preference("Which season do you plan to travel in?\n"
        "  1) Spring\n  2) Summer\n  3) Autumn\n  4) Winter", ["1","2","3","4"]))
    user_climate = int(get_user_preference("What climate do you prefer?\n"
        "  1) Cold\n  2) Cool\n  3) Moderate\n  4) Warm\n  5) Hot", ["1","2","3","4","5"]))

    # INTEREST INPUTS - Sports, wildlife, nature, historical, cuisine, adventure, beach
    print ("Now we would like to ask you some questions about your interests,"
        " on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates"
        " strong interest, and 0 indicates indifference.\n")
    destination_interests = ["sports", "wildlife", "nature", "historical sites",
                            "fine dining", "adventure activities", "the beach"]
    user_interests = []
    get_user_interest(destination_interests, user_interests)

    # CHECK PARAMETERS
    greatest_score = -200 # Any matching destination will have a higher score.
    final_match = False # Set default to false

    for destination in Destinations().get_all():
        # For each destination run through parameters based on user inputs.
        if match_continent(user_continent, destination.get_continent()):
            if match_children(user_children, destination.is_kid_friendly()):
                if match_cost (user_cost, destination.get_cost()):
                    if match_crime (user_crime, destination.get_crime()):
                        if match_climate (user_climate,destination.get_climate()):
                            # All the user inputs match the current destination.
                            # At least one final match will be returned.
                            # Now calculate destination score.
                            # Determine season factor and interest score.
                            season_factor = destination.get_season_factor(match_season(user_season))
                            interest_score = match_interest(user_interests, destination)
                            destination_score = interest_score * season_factor

                            # Name and greatest destination score will be stored.
                            if destination_score > greatest_score:
                                greatest_score = destination_score
                                final_match_name = destination.get_name()
                                final_match = True
 
    #FINAL OUTPUT:
    print("Thank you for answering all our questions."
          " Your next travel destination is:", sep="\n")
    if final_match == True:
        print (final_match_name)
    else:
        print ("None")

if __name__ == "__main__":
    main()
