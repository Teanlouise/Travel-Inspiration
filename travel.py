"""

"""

__author__ = ""
__date__ = ""


from destinations import Destinations


def match_continent(user, database):
    """
    Matches the user's input for 'Continent' with the data from destinations file.

    Paramaters:
        user (str): User's input when prompted for 'continent' preference. User input between 1 and 7
        database (str): Continent name stored in destinations database.

    Variables:
        destination_continent (str): The name of the continent according to the user's input

    Return:
        bool: Destination is match (True), if and only if, the destination of the continent is an exact match for user.
    """

    if user==1:
        destination_continent = "asia"
    elif user==2:
        destination_continent = "africa"
    elif user==3:
        destination_continent = "north america"
    elif user==4:
        destination_continent = "south america"
    elif user==5:
        destination_continent = "europe"
    elif user==6:
        destination_continent = "oceania"
    elif user==7:
        destination_continent = "antartica"
    else:
        print ("None - Continent")

    if database.get_continent() == destination_continent:
        return True
    else:
        return False


def match_cost(user, database):
    """
    Match the user's input for 'cost' with the data from the database.  Assigns string inputs of user and database to match to integers to compare.
    
    Paramaters:
        user (str): User's input when prompted for 'cost' preference. User input $ or $$ or $$
        database (str): Continent name stored in destinations database.

    Variables:
        user_cost (int): Converts the users string input to integers 1 to 3.
        destination_cost (int): Converts the database string values to integers 1 to 3 to match user_cost.

    Return:
        bool: Destination is match (True) if the 'cost' of the destination in the database is less than or equal to the user's input (i.e. within user budget).
    """

    if user=="$$$":
        user_cost_int = 3
    elif user=="$$":
        user_cost_int = 2
    elif user=="$":
        user_cost_int = 1
    else:
        print ("None")

    if database.get_cost()=="$$$":
        destination_cost = 3
    elif database.get_cost()=="$$":
        destination_cost = 2
    elif database.get_cost()=="$":
        destination_cost = 1


    if user_cost_int >= destination_cost:
        return True
    else:
        return False

def match_children(user, database):
    """
    Match the user's input for 'kid friendly' with the data from the database.
    
    Paramaters:
        user (int): User's input when prompted for 'kid friendly' preference. User input 1 or 2.
        database (bool): Stored in database as TRUE for kids and FALSE for not kid friendly.

    Return:
        bool: True, if the user selects kid friendly (user input 1) and the destination is True. Or if user selects no preference (user input 2)
        Otherwise the functions returns false.
    """

    # User requires kid friendly
    if user == 1:
        if database.is_kid_friendly() == True:
            return True
        else:
            return False
    # User has no preference i.e. not travelling with children so all countries match
    else:
        return True


def match_crime(user, database):
    """
    Match the user's input for 'crime' with the data from the database.
    
    Paramaters:
        user (str): User's input when prompted for 'crime' preference. User input 1 to 3.
        database (str): Crime level stored in destinations database.

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

    if user >= destination_crime:
        return True
    else:
        return False

def match_climate (user,database):
    """
    Match the user's input for 'climate' with the data from the database.
    
    Paramaters:
        user (str): User's input when prompted for 'climate' preference. User input from 1 to 5.
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

    if user == destination_climate:
        return True
    else:
        return False

def match_season (user, database):
    """
    Match the user's input for 'season' with the associated season factor for each destination from the database.
    
    Paramaters:
        user (str): User's input when prompted for 'season' preference. User input from 1 to 4.
        database (str): Season name stored in destinations database.

    Variables:
        destination_season (str): Retrieve the season factor associated with the user's input for 'season' from the database.
        
    Return:
        str: The value of the season factor for the season is returned.
    """
        
    if user == 1:
        destination_season = database.get_season_factor ("spring")
    elif user == 2:
        destination_season = database.get_season_factor ("summer")
    elif user == 3:
        destination_season = database.get_season_factor ("autumn")
    elif user == 4:
        destination_season = database.get_season_factor ("winter")

    return destination_season
    
def match_interest (interestlist, database):
    """
    Match the user's input for every 'interest' with the interest factor from the database.
    
    Paramaters:
        sports (str): User's input for 'sports' question.
        wildlife (str): User's input for 'wildlife' question.
        nature (str): User's input for 'nature' question.
        historical (str): User's input for 'historical' question.
        cuisine (str): User's input for 'cuisine' question.
        adventure (str): User's input for 'adventure' question.
        beach (str): User's input for 'beach' question.
        database (float): Interest factor store for each interest in destinations database.

    Variables:
        sports_score (float): user input for 'sports' * database score for 'sports'
        [same for wildlife, nature, historical, cuisine, adventure, beach]
        interest score (float): sum of all xxx_score
        
    Return:
        float: The result of the interest_score formula.
    """
    
    sports_score = interestlist[0]*database.get_interest_score ("sports")
    wildlife_score = interestlist[1]*database.get_interest_score ("wildlife")
    nature_score = interestlist[2]*database.get_interest_score ("nature")
    historical_score = interestlist[3]*database.get_interest_score ("historical")
    cuisine_score = interestlist[4]*database.get_interest_score ("cuisine")
    adventure_score = interestlist[5]*database.get_interest_score ("adventure")
    beach_score = interestlist[6]*database.get_interest_score ("beach")
    
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
        
        interest_score: Variable for interest score of destination.
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
    user_season = int(input("> "))
    print ("")

    print ("What climate do you prefer?", "  1) Cold", "  2) Cool", "  3) Moderate", "  4) Warm", "  5) Hot", sep="\n")
    user_climate = int(input("> "))
    print ("")


    # INTEREST INPUTS - Sports, wildlife, nature, historical, cuisine, adventure, beach
    print ("Now we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")
    print ("")

    
    interest_list = ["sports", "wildlife", "nature", "historical sites", "fine dining", "adventure activities", "beach"]
    interest_result = []
    
    for interest in interest_list:
        print ("How much do you like ", interest,"? (-5 to 5)")
        interest_result.append (float(input("> ")))
        print ("")

    #print ("How much do you like sports? (-5 to 5)", )
    #user_sports = input("> ")
   # print ("")

    #print ("How much do you like wildlife? (-5 to 5)", sep="\n")
   # user_wildlife = input("> ")
   # print ("")

    #print ("How much do you like nature? (-5 to 5)", sep="\n")
    #user_nature = input("> ")
   # print ("")
    
   # print ("How much do you like historical sites? (-5 to 5)", sep="\n")
    #user_historical =input("> ")
    #print ("")

    #print ("How much do you like fine dining? (-5 to 5)", sep="\n")
   # user_cuisine =input("> ")
    #print ("")

   # print ("How much do you like adventure activities? (-5 to 5)", sep="\n")
   # user_adventure = input("> ")
   # print ("")

    #print ("How much do you like the beach? (-5 to 5)", sep="\n")
   # user_beach = input ("> ")
   # print ("")
  
    # CHECK PARAMETERS
    final_match = False
    greatest_score = -200
    
    for destination in Destinations().get_all():
        if match_continent(int(user_continent), destination):
            if match_children(int(user_children), destination):
                if match_cost (user_cost, destination):
                    if match_crime (int(user_crime), destination):
                        if match_climate (int(user_climate),destination):
                            interest_score = match_interest (interest_result, destination)
                            season_factor = match_season (float(user_season), destination)
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
