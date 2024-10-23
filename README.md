# WIP

![Recipe Bank]

The Recipe Bank is a website for saving and sharing recipes in a simple format. Have all your recipes in one place to easily refer to when you go shopping.

You can view the live site here - <a href="https://recipebank-f5eeb7306eea.herokuapp.com/" target="_blank"> Recipe Bank </a>

# User Experience (UX)

## Site Aims

* Allow the user to save, share and browse recipes
* Like other user's recipes to show appreciation
* Account registration and log in functionality

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here - <a href="https://github.com/users/KRnils/projects/3/views/1" target="_blank">  </a>

Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:
* Epics
* Todo
* In Progress
* Done

![Kanban board github]()

### User Stories

* 
* 
* 
* 
* 

**Still in backlog for future features**
* 

## Design Wireframes

### Mobile

![Home Page]()

![Login Page]()

![Contact Page]()

### Desktop

![Home Page]()

![Signup Page]()

![Login Page]()

![Blog post]()


## Database Schema

![Database Schema](/readme/images/Database%20ERD.png)

## Site Structure


## Design Choices

### Color Scheme

![Site colour scheme]()

### Typography
Font thoughts go here

# Features

## Navigation

* The site navigation is done through the navigation bar at the top of each page...
* Profile button depends on login status

## Home Screen

 * The starting page

 ![Homepage Mobile]() image goes here

 * Something about the starting page

  ![]() image pls
 
 ### Feature name

 * Feature description
 
 ![]() image pls

 * When an age range is chosen by the user they are brought to a page showing only the books recommended for that age group.
 

### Create a recipe

* Login is required before creating a recipe.

![Review page]() image

### Future Features

* Optional recipe image
* More user profile details
* Advanced search features like date based, minimum likes amount, search by ingredient
* Shopping snapshot view, easily exported format to use as shopping list

# Technologies Used

* HTML
* CSS
* Python
* Django
* Heroku

## Testing

### W3C Validator Testing

__All HTML has been tested with the W3C validator and show no errors or warnings.__

- [Results for index.html])

__All CSS has been testeed with W3C validator (Jigsaw) and show no errors or warnings.__

- [Results for style.css]()

__All JavaScript has been testeed with [JSHint](https://jshint.com/)__

Warnings found:
* WIP

see [TESTING.md](TESTING.md) for more discussion.

### Accessibility Test

All Lighthouse test scores reached 100 except performance which was at 99.

see [TESTING.md](TESTING.md) for all details and a full list of scores and other tests performed.

### Solved Bugs

* 

### Known Bugs

* There will be bugs

## Manual Testing

Manual tests were performed to check for user story criteria compliance.

### Tests Performed Per Page

`Start page (index.html)`

| Feature | Expected Outcome | Testing Performed | Pass/Fail |
| --- | --- | --- | --- |
| Location | Outcome | Action | Pass/Fail |
| Location | Outcome | Action | Pass/Fail |
| Location | Outcome | Action | Pass/Fail |
| Location | Outcome | Action | Pass/Fail |

# Deployment

## How to fork the repository
* Make sure you have Python version 3.12.4, different version might still work, especially if the version number is close.
* At the top of the github page, in the line with the project's name, on the right side find "Fork" and click it.
* Install required packages by running `pip install requirements.txt`
* These are all the packages listed:
  * asgiref==3.8.1
  * dj-database-url==0.5.0
  * Django==4.2.13
  * django-allauth==0.63.6
  * gunicorn==20.1.0
  * psycopg2==2.9.9
  * sqlparse==0.5.0
  * whitenoise==6.7.0
* You will need to set up your own database since the public data here does not include database details and credentials for security reasons. The current settings.py refers to the env.py file which stores the database information, this is not publically available and needs to be replaced to work in a fork.
* For testing you can run with a local sqlite database.

## Deploying to Heroku

1. Go to [Heroku](https://id.heroku.com/login), create account if you don't have and log in.

2. Head to your dashboard and click "New", then "Create new app"

3. Next step is to give your app a name and to choose region. After that click on "Create app".

4. Then head to "Deployment" tab which you can also find on top of your Heroku page and under "Deployment method" click on "GitHub"(in my case that's where my repository is).

5. After that, just under the "Deployment method" section is "Connect to GitHub" section where you need to find your repository and then click on "Connect".

6. Just under "Connect to GitHub" section is "Automatic deploys" section where you can click on "Enable Automatic Deploys" if that's what you want and just under is "Manual Deploy" section, where you need to click on "Deploy Manually".

# Credits

* [Django](https://www.djangoproject.com/) Is the framework that this project is built on entirely.
* [Gitpod](https://www.gitpod.io/) Provided the working environment, allowing me to work from separate computers.
* [Lucid Charts](https://www.lucidchart.com) For ERD diagrams
* [Laura Mayocks Project The Happy Reader](https://github.com/LauraMayock/The-happy-reader/tree/main) Provided inspiration for the structure of this readme
* The deployment steps for Heroku is mostly copied from [Coder's Parkhouse](https://github.com/AleksandarJavorovic/coders-parkhouse) but edited for style and small differences.
