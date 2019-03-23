"""
Travel Inspiration - CSSE1001 - Assignment 1

A travel recommendation program. The user will be given a questionaire that
matches their travel preferences to the 'destination' database to return the
best match for the user.
"""

__author__ = "Tean-louise McGrath"
__date__ = "29.03.19"


from destinations import Destinations


def match_continent(user_input, database_value):
    """
    Matches the user's input for 'Continent' with the data from destinations file.

    Paramaters:
        user_input (int): User's input when prompted for 'continent' preference. User input between 1 and 7
        database_value (str): Continent name stored in destinations database.

    Variables:
        destination_continent (str): The name of the continent according to the user's input

    Return:
        bool: Destination is match (True), if and only if, the destination of the continent is an exact match for user.
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

    # Return True if user matches database, else False
    return (database_value == destination_continent)

def match_cost(user_input, database_value):
    """
    Match the user's input for 'cost' with the data from the database.  Convert string inputs of user and database to integers to compare.

    Paramaters:
        user_input (str): User's input when prompted for 'cost' preference. User input $ or $$ or $$$
        database_value (str): Cost of destination stored in destinations database as $ or $$ or $$$

    Variables:
        user_cost_int (int): Converts the users string input to integers 1 to 3.
        destination_cost (int): Converts the database string values to integers 1 to 3.

    Return:
        bool: Destination is match (True) if the 'cost' of the destination in the database is less than or equal to the user's input (i.e. within user budget).
    """

    if user_input=="$$$":
        user_cost_int = 3
    elif user_input=="$$":
        user_cost_int = 2
    elif user_input=="$":
        user_cost_int = 1

    if database_value =="$$$":
        destination_cost = 3
    elif database_value =="$$":
        destination_cost = 2
    elif database_value =="$":
        destination_cost = 1

    # Return True if user matches database, else False
    return (user_cost_int >= destination_cost)

def match_children(user_input, database_value):
    """
    Match the user's input for 'kid friendly' with the data from the database.

    Paramaters:
        user_input (int): User's input when prompted for 'kid friendly' preference. User input 1 (Yes) or 2 (No).
        database_value (bool): Stored in database as TRUE for kids (Yes) and FALSE for not kid friendly (No).

    Return:
        bool: True, if the user selects kid friendly (user input 1) and the destination is True. Or if user selects no preference (user input 2)
        Otherwise the functions returns false.
    """

    # User requires kid friendly, check database. Return True if user matches database, else False
    if user_input == 1:
        return database_value
    # User has no preference, always TRUE i.e. not travelling with children so all countries match
    else:
        return True


def match_crime(user_input, database):
    """
    Match the user's input for 'crime' with the data from the database.

    Paramaters:
        user_input (int): User's input when prompted for 'crime' preference. User input 1 to 3.
        database_value (str): Crime level stored in destinations database as low, average or high.

    Variables:
        destination_crime (str): Converts the database string values to integers 1 to 3 to match user input.

    Return:
        bool: Destination is a match (True) if the 'crime' of the destination in the database is less than or equal to the user's input (i.e. within user preference).
    """

    if database.get_crime()=="low":
        destination_crime = 1
    elif database.get_crime()=="average":
        destination_crime = 2
    elif database.get_crime()=="high":
        destination_crime = 3

    if user_input >= destination_crime:
        return True
    else:
        return False

def match_climate (user_input,database):
    """
    Match the user's input for 'climate' with the data from the database.

    Paramaters:
        user_input (str): User's input when prompted for 'climate' preference. User input from 1 to 5.
        database (str): Climate description name stored in destinations database.

    Variables:
        destination_climate (int): Converts the database string values to integers 1 to 3 to match user_cost.

    Return:
        bool: Destination is a match (True) if the 'climate' of the destination in the database is the same as the user input.
    """

    if database.get_climate()=="cold":
        destination_climate = 1
    elif database.get_climate()=="cool":
        destination_climate = 2
    elif database.get_climate()=="moderate":
        destination_climate = 3
    elif database.get_climate()=="warm":
        destination_climate = 4
    elif database.get_climate()=="hot":
        destination_climate = 5
    else:
        print ("None Climate")

    if user_input == destination_climate:
        return True
    else:
        return False

def match_season (user_input, database):
    """
    Match the user's input for 'season' with the associated season factor for each destination from the database.

    Paramaters:
        user_input (str): User's input when prompted for 'season' preference. User input from 1 to 4.
        database (str): Season name stored in destinations database.

    Variables:
        destination_season (str): Retrieve the season factor associated with the user's input for 'season' from the database.

    Return:
        str: The value of the season factor for the season is returned.
    """

    if user_input == 1:
        destination_season = database.get_season_factor ("spring")
    elif user_input == 2:
        destination_season = database.get_season_factor ("summer")
    elif user_input == 3:
        destination_season = database.get_season_factor ("autumn")
    elif user_input == 4:
        destination_season = database.get_season_factor ("winter")

    return destination_season

def match_interest (interest_list, database):
    """
    Match the user's input for every 'interest' with the interest factor from the database.

    Paramaters:
        interest_list (list): List of user's input from list of interests. Stored in list as float.
        database (float): Interest factor store for each interest in destinations database.

    Variables:
        sports_score (float): user input for 'sports' * database score for 'sports'
        [same for wildlife, nature, historical, cuisine, adventure, beach]
        destination_interest (float): sum of all xxx_score

    Return:
        float: The result of the destination_interest formula.
    """

    sports_score = interest_list[0]*database.get_interest_score ("sports")
    wildlife_score = interest_list[1]*database.get_interest_score ("wildlife")
    nature_score = interest_list[2]*database.get_interest_score ("nature")
    historical_score = interest_list[3]*database.get_interest_score ("historical")
    cuisine_score = interest_list[4]*database.get_interest_score ("cuisine")
    adventure_score = interest_list[5]*database.get_interest_score ("adventure")
    beach_score = interest_list[6]*database.get_interest_score ("beach")

    destination_interest = sports_score + wildlife_score + nature_score + historical_score + cuisine_score + adventure_score + beach_score
    return destination_interest

def main():
    """
    Travel program. The user will be asked a number of questions and an exact match (or none) will be returned based on parameters.

    Parameters of final match:
        # 1 CONTINENT: True if continent matches user input.
        # 2 KID FRIENDLY: True if user selects children and destination is kid friendly, or if user doesn't select kid friendly.
        # 3 COST: True if cost of destination is less than or equal to the user input for cost.
        # 4 CRIME: True if crime of destinations is less than or equal to the user input for crime.
        # 5 CLIMATE: True if the climate of the destination is equal to the use rinput for climate.
        # 6 SEASON & INTEREST: True if the destination has the greatest total score (greatest season factor * greatest interest factor)

    Precondtions:
        final_match: The exact country match according to the parameters. Start as FALSE.
        greatest_score: The greatest possible score (interest factor*season factor) for a destination. Greatest value set as -200.

    Variables:
        user_xxx: User input for each question. To be used as reference for parameters.

        destination_interest: Variable for interest score of destination.
        season_factor: Variable for season factor of destination.
        destination_score: Total for a destination's interest score * destination's season factor.

    Return:
        destination.get_name of the country with the exact match for the parameters. If no exact match the return is 'none'.
    """

    #INTRODUCTION - Welcome and name
    print ("Welcome to Travel Inspiration!")
    print ("")
    user_name = input("What is your name? ")
    print ("")
    print ("Hi, ", user_name, "!", sep="")
    print ("")

    #TRAVEL PREFERENCE INPUTS - Continent, Money, Children, Season, Climate
    user_continent = 0
    while user_continent not in range (1,7):
        print("Which continent would you like to travel to?", "  1) Asia", "  2) Africa", "  3) North America", "  4) South America", "  5) Europe", "  6) Oceania", "  7) Antarctica", sep="\n")
        print ("")
        user_continent = int(input("> "))
        print ("Please try again")

    print ("What is money to you?", "  $$$) No object", "  $$) Spendable, so long as I get value from doing so", "  $) Extremely important; I want to spend as little as possible", sep="\n")
    user_cost = input("> ")
    print ("")

    print ("How much crime is acceptable when you travel?", "  1) Low", "  2) Average", "  3) High",sep="\n" )
    user_crime = int(input("> "))
    print ("")

    print ("Will you be travelling with children?", "  1) Yes", "  2) No", sep="\n")
    user_children = int(input("> "))
    print ("")

    print ("Which season do you plan to travel in?", "  1) Spring", "  2) Summer", "  3) Autumn", "  4) Winter", sep="\n")
    user_season = float(input("> "))
    print ("")

    print ("What climate do you prefer?", "  1) Cold", "  2) Cool", "  3) Moderate", "  4) Warm", "  5) Hot", sep="\n")
    user_climate = int(input("> "))
    print ("")

    # INTEREST INPUTS - Sports, wildlife, nature, historical, cuisine, adventure, beach
    print ("Now we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")
    print ("")

    interests_list = ["sports", "wildlife", "nature", "historical sites", "fine dining", "adventure activities", "beach"]
    user_interests = []

    for interest in interests_list:
        print ("How much do you like ", interest,"? (-5 to 5)")
        user_interests.append (float(input("> ")))
        print ("")

    # CHECK PARAMETERS
    final_match = False
    greatest_score = -200

    for destination in Destinations().get_all():
        if match_continent(user_continent, destination.get_continent()):
            if match_children(user_children, destination.is_kid_friendly()):
                if match_cost (user_cost, destination.get_cost()):
                    if match_crime (user_crime, destination):
                        if match_climate (user_climate,destination):
                            interest_score = match_interest (user_interests, destination)
                            season_factor = match_season (user_season, destination)
                            destination_score = interest_score * season_factor
                            if destination_score > greatest_score:
                                greatest_score = destination_score
                                final_match_country_name = destination.get_name()
                                final_match = True

                                print ("MATCH ALL: ",destination.get_name(), destination.get_cost(), destination.is_kid_friendly(), destination.get_crime(), destination.get_climate(), destination_score)
                            else: print ("FAIL - Score", destination.get_name())
                        else: print("FAIL - Climate", destination.get_name())
                    else: print ("FAIL - Crime: ", destination.get_name())
                else: print ("FAIL - Cost: ", destination.get_name())
            else: print ("FAIL - Children: ", destination.get_name())
        else: print ("FAILED - Continent: ", destination.get_name())

    #FINAL OUTPUT:
    print("Thank you for answering all our questions. Your next travel destination is:", sep="\n")
    if final_match == True:
        print (final_match_country_name)
    else:
        print ("None")
        print ("NO MATCH: ",destination.get_name(), destination.get_cost(), destination.is_kid_friendly(), destination.get_crime(), destination.get_climate())

if __name__ == "__main__":
    main()
