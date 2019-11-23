[Back to Home](https://teanlouise.github.io)

![travel_inspiration](https://user-images.githubusercontent.com/19520346/69231404-bcfeaa00-0bd4-11ea-8b54-a4cf20bf992c.PNG)

Using Python, I developed a travel destination recommendation program demonstrating the use of control structures and functional decomposition. It was submitted as Assignment 1 for CSSE1001 at UQ. Software design choices and documentation were a key aspect of the grading criteria. This assessment received a High Distinction, and all feedback has been applied in this solution.

> Welcome to Travel Inspiration! We are going to be building a travel recommendation program. Out of ideas where to travel? Travel
Inspiration has got you covered. The program will ask the user questions about their preferences in a travel destination. It will use these to recommend the best match in a database of potential travel destinations.

The task was to implement the functionality to question the user and perform the matching. This involved creating the questionnaire (according to strict rules), prompting the user for input, using this input to output the best match ('None' if no match) and validating the input (repeatedly ask until valid input entered). 

An exact match must have the following requirements:
- The continent must match exactly
- If the user will be travelling with children, it must be kid friendly
- Cost must be less than or equal to the user's response to the money question
- Crime cannot be greater than is acceptable to the user
- Matches the user’s climate preference exactly
- Has the greatest score 
```
score = season_factor (for user's selected season) * interested score (sum of user's response multiplied by the destination's score for each interest eg. responsesports *scoresports + .....)
```

_destination.csv (the database), destination.py (file to read from the database) and specifications are the property of University of Queensland_

![travel_insp1 (1)](https://user-images.githubusercontent.com/19520346/69198435-636c9000-0b80-11ea-8f55-dbdb4259401c.PNG)
![travel_insp2 (1)](https://user-images.githubusercontent.com/19520346/69198341-1d173100-0b80-11ea-8e1b-5ea3c924633d.PNG)




