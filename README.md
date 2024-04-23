# Joy of Food

This is a Python and Django application for a newly started restaurang, here you can view the menu and there after book a table.

When a user visits the website user can register so that they can keep track of their bookings.

[Here is the live version](https://sink-a-ship-283abb4062a9.herokuapp.com/)

![Website in diffrent browsers](assets/images/devicepic.JPG)


# UX (User Experience)

## Target Audience

The targeted audience for this application are people who love food. People who are seeking to enjoy a good tasting meal. This website is easy to navigate and easy to book a reservation for you and your family.

## User Stories

There are two user who can access this application, the users and the site owner. The site owner can utilise all the futures for booking and cancelling a reservation. Site owen also have the tools to remove or add other users.

As a user you have access to making a reservation, accessing you reservation so that you can se the date and time if needed. You can also delete a reservation if needed.

### User Stories were 

* As a User I can create an account so that my details are remembered.
* As a User I can book one or more guest for a meal in a restaurant so that we have a reservation without any double booking.
* As a User I can cancel my booking so that if i get sick or have to reschedule.
* As a User I can book multiple table so that our team can eat
* As a User I can view the menu of the restaurant so that i know ahead what to order.

### User Stories that i didnt not implement

* As a User I can review the restaurant with a star system so that more people can experience the food.

## Wireframes

The following images shows wireframe of the primary design of the application. These wireframes were created using [Balsamiq Wireframe](https://balsamiq.com/)

### Wireframe of Home Page

This wireframe shows the main page, which is also the base wireframe for the other pages. This is the same if the user is logged in or not. Its give a good feel of the general layout of the page.

![Home page](<static/images/wireframe 1.JPG>)

### Existing features

* Random board generation
  * Ships are randomly placed on both of the player and computer boards.
  * User cannot see where computers ships are.

 ![Generated board](assets/images/board.JPG)

  * Play against the computer 
  * Accepts user input
  * Maintains scores

 ![First round](assets/images/first_guess.JPG)

* Input validation and error-checking
  * Entering coordinates outside the board grids promt an error message.
  * Only numbers are accepted.
  * Entering the same guesses twice will not be accepted.

 ![Validation Errors](assets/images/grids.JPG)

 * Data maintained in  class instances.
  

### Features left to Implement

*  Allow player to choose choose board size and amount of ships.
*  Allow players to place their own ships by inputing coordinates.

## Data Model

Saw a video from an instructure that they use a class model to hold the board size, number of ships, position of ships, the guesses and details as the boar type.

I decided to impliment the same and it was a good decision cause it make it eaiser to run it from Board class. 

Through the Board class i created methods as guess, add ships and print board.

## Testing 

I have manually tested this project by doing the following:

* Passed the code through a PEP8 linter and confirmed there are no errors.
* Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
* Tested in my local terminal and the Code Institue Heroku terminal
* Check that there is always four randomly generated ships.



## Bugs

Solved bugs

* When populating the board keept getting this error prompt. It was due to that i dint not print out the board on sceen
![Bug](<assets/images/error cannot add any more ships.JPG>)
* Had issues with getting the board names to show after each round, i just had to move it by the end of the code in run_game function.

## Remaining Bugs

*  No bugs remaining 


## Validator Testin

* PEP8
  * No errors where returned


 ## Deployment 

 This project was deployed using Code institute's mock terminal for Heroku.

 * Steps for deployment:
   * Create a new Heroku app
   * Link the Heroku app to the repository.
   * Click on Deplo

  The live link to this page - [In Three](https://maadajibao.github.io/Project-2-In-Three/)

## Credits

* Code institute for the deployment terminal
* Code institute for the basice setup of the idea 
* Code institute for the idea of classes

