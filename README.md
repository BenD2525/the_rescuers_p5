# The Rescuers

The Rescuers is a website for a fictional animal rescue charity, which is a remake of my first project, which was built using only HTML and CSS. This website is a newer iteration of this original website and as an eCommerce site, it allows the user to create an account, login, logout and edit their profile. The user can learn more about the purpose of the site on the home page, and can buy products from the charity to support their work. There is a list of products available, which the user is able to sort and filter. Once the user has decided what they wish to purchase, they are able to check their bag and make any required amendments to quantities of products or remove anything they no longer want. Once the user is happy and ready to purchase, they can manually input payment details, or use the ones they already have saved to their profile. The user can then pay using Stripe, and once their payment has been accepted, they will receive a confirmation email with their order number and a thankyou. 

![Multi Screen Image]()

## [Live Site]()

## Contents

- [The Rescuers](#the-rescuers)
- [UX Design](#ux-design)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
    - [User Stories](#user-stories)
  - [Skeleton Plane](#skeleton-plane)
    - [Site Flow](#site-flow)
    - [Database Schema](#database-schema)
  - [Surface Plane](#surface-plane)
    - [Colour Scheme](#colour-scheme)
- [Agile Development Process](#agile-development-process)
- [Current Features](#current-features)
  - [Base Features](#base-features)
    - [Title](#title)
    - [Navbar (Logged out)](#navbar-logged-out)
    - [Navbar (Logged in)](##navbar-logged-in)
    - [Footer](#footer)
  - [Home Page](#home-page)
    - [Main Section](#main-section)
    - [Article Section](#article-section)
  - [Login Page](#login-page)
  - [Signup Page](#signup-page)
  - [Article Page](#article-page)
  - [Health Hub](#health-hub)
    - [Update Stats](#update-stats)
    - [Health Hub History](#health-hub-history)
    - [Edit Stats](#edit-stats)
    - [Delete Stats](#delete-stats)
    - [Health Hub Tracker](#health-hub-tracker)
- [Future Development](#future-development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Languages Used](#languages-used)
- [Technologies Used](#technologies-used)
- [Honourable Mentions](#honourable-mentions)
- [Credits](#credits)

## UX Design

### Strategy Plane
When creating a functional, informative website, a developer must consider all planes of development.

- Site Goal
	- The site goal is to allow users to learn about the charity and support the charity by making donations or purchasing pet products to support them.

- Target Audience
	- The target audience is primarily animal lovers, who wish to support charities.

- User Requirements
	- The User must be able to learn about the site and its' purpose.
	- The User must be able to sign up and log in.
	- The User must be able to log out.
	- The User must be able to view, add, edit and delete their reviews, as well as viewing others.
	- The User must be able to view products.
	- The User must be able to select the products they want to have.
	- The User must be able to pay for the products they want.
	- The User must be able to receive an order confirmation email once they have purchased a product.
	

| Opportunity                                            | Importance | Viability/Feasibility |
| ------------------------------------------------------ | ---------- | --------------------- |
| Home page- Content                                     | 5          | 5                     |
| Nav Bar                                       	 | 5          | 5                     |
| Review Page- Add a review                              | 4          | 4                     |
| Review Page- Edit a review                             | 4          | 4                     |
| Review Page- Delete a review                    	 | 4          | 4                     |
| Featured Residents Page                                | 4          | 4
| Products Page         				 | 5          | 5                     |
| Products Page - Price details        			 | 5          | 4                     |
| Products Page - Review details                 	 | 4          | 4                     |
| Product sort function                         	 | 3          | 4                     |
| Product filter function         			 | 3          | 4                     |
| Product detail page      				 | 4          | 4                     |
| Bag icon link in header         			 | 4          | 5                     |
| Adjust quantity buttons    				 | 4          | 4                     |
| Remove item button     				 | 4          | 4                     |
| Bag icon label                        		 | 3          | 4                     |
| Details of each product showing in bag		 | 4	      |	4		      |
| Checkout link from bag				 | 5          | 5                     |
| Payment details form					 | 5          | 5                     |
| Use saved payment details checkbox			 | 4          | 4                     |
| Stripe						 | 5          | 4                     |
| Email setup						 | 4          | 5                     |
| Add user profile					 | 4          | 4                     |
| Login functionality					 | 5          | 5                     |
| Logout functionality					 | 5          | 5                     |
| Edit profile details					 | 4          | 4                     |
| ----------------------------------------               | ----       | ----                  |
| Totals:25                                              | 110        | 113                   |


The viability score is higher than the importance score, so I should be able to implement all of the above features. These scores were based on my skill level at the beginning of the project.

### Scope Plane
Assessing the scope of a website is based on the information gathered from forumlating a strategy. Using the target audience and the established website goals, the website requirements were set out.
- Content Requirements:
	- Login Page
	- Logout Page
	- Sign up Page
	- Home Page
	- Reviews Page
	- Products app
	- Shopping Bag app
	- Profile app
	- Checkout app

### Structure Plane
The requirements listed above were then organised and structured into different apps, all of which can be reused for future projects:
- Home app (including reviews page)
- Products app
- Accounts app (login/Signup functionality)
- Profile app (storing personal data, order data etc.)
- Bag app
- Checkout app (accessible from bag)

#### User Stories
User Stories were then created to guide the development process. Once I had established a list, I organised them into apps and noted which feature would serve to achieve the user story. These are listed below and were logged as Issues, sorted into Milestones and completed on my project board in Github.

Home
- As a new user...
	- I want to see what the purpose of the site is from the home page.
	- I want to be able to navigate to each part of the site easily.
- As a current user...
	- I want to easily return to the part of the site I require.
	- I want to easily leave a review for the product I choose.
	- I want to easily edit a review for the product I choose.
	- I want to easily delete a review for the product I choose.
  - I want to be able to see the residents of the shelter, and who I will be helping when I buy products.

Products
- As a new user...
	- I want to easily see the list of products.
- As a current user...
	- I want to be able to easily see the price of the products I choose.
	- I want to be able to easily see the reviews of the products I choose.
	- I want to be able to sort the products to suit my needs.
	- I want to be able to filter the products to suit my needs.
	- I want to be able to select the products I require and add them to my bag.

Bag
- As a new user...
	- I want to easily access my bag.
- As a current user...
	- I want to be able to adjust quantities of items in my bag.
	- I want to be able to remove items from my bag.
	- I want to be able to see at a glance how many items I have in my bag.
	- I want to be able to see the details of the products in my bag.

Checkout
- As a new user...
	- I want to be able to easily access the checkout area.
- As a current user...
	- I want to be able to add my details to the payment screen.
	- I want to be able to use my existing payment details from my profile
	- I want to be able to pay using Stripe.
	- I want to receive a confirmation email once my payment has been accepted.

Profile
- As a new user...
	- I want to easily create my profile.
- As a current user...
	- I want to be able to log in to my account.
	- I want to be able to log out of my account.
	- I want to be able to see and edit my account details when I want.


I decided to remove the below user stories from my development using the agile process:


### Skeleton Plane
A wireframe for the website was produced using a desktop version of Balsamiq in order to provide a clear image of what the website should look like.
![Home page]()
![Reviews page]()
![Login]()
![Signup]()
![Products page]()
![Bag page]()
![Checkout page]()
![Profile page]()

#### Site Flow
Using Balsamiq, I then created a flow map showing what I would visualise as the user's journey through the website.
![Link to Site map]()

#### Database Schema
I created a visual representation of my databases in [Lucid Chart](https://www.lucidchart.com/).
![Database Schema]()
- Health Stats
  - The Health Stats model is designed for the user to be able to store their weight, run distance and run time using the update stats form.
  - The user and date fields are stored on each instance automatically, the date being registered as the current date/time, and the user being registered as the current logged in user. I decided to set the date field to 'auto_now_add = True' so that the initial date would be registered, however it would not be overwritten once edited, as I felt it was important to keep the original date of registering the data.
  - The weight and run distance fields are both decimal fields, with a max digits limitation of 5 and 2 decimal places.
  - The run time field is a duration field. This was originally created as a time field, however this did not work as expected. If a user input the a time of 1:00, this would register as a time of 1am. I then changed the field to a duration field and this fixed the issue and worked as expected.
- Article
  - The article model is designed to be able to store articles for the website, and display them in a list on the homepage, with the full content of each article available in the subsequent article pages. This model can only be added to via the admin panel using the admin login, so that the site admin can control the information available to all users.
  - The title and topic fields are set as character fields because they should only include text.
  - The featured image field is set as a cloudinary field because I am using Cloudinary to host my images.
  - The content field is set as a text field because this is where the main content of the article is held.

### Surface Plane

#### Colour Scheme
I used [Coolors](https://coolors.co/) to establish a colour scheme to use for this project.
Coolors generates complimentary colour schemes based on the colour you initially choose. I began by choosing an earthy green colour 'tea-green' which is similar to the colour scheme of my original static project, and then allowed the program to generate complimentary colours.
The full colour scheme is listed in my base.css file.

## Agile Development Process
I used Github's issues functionality, and organised them into milestones, which can be found [here](). I also organised my issues using my project board, found [here](), moving them between in progress and completed as and when. 

## **Current Features**

### Base Features
The below features are part of my base template, and as such are included on all pages.

#### **Title**
The title of the website, I used the bootstrap display class to clearly display this as the website's title, ensuring it is prominent on each page.

![Title](readme/images/title.PNG)

#### **Navbar (Logged Out)**
When accessing the site on the desktop, the navbar is located next to the title, following the blue and white scheme.

![Navbar Desktop](readme/images/navbar.PNG)

On a mobile view, this is changed to a burger menu.

![Navbar Mobile](readme/images/navbar_mobile.PNG)

#### **Navbar (Logged In)**
When logged in as a user on the desktop, the navbar is located next to the title, following the blue and white scheme.
When logged in, the login function changes to logout, and the sign up link is removed and replaced with 'My Health' which allows access to the health hub.

![Navbar Desktop Logged In](readme/images/navbar_logged_in.PNG)

On a mobile view, this is changed to a burger menu.

![Navbar Mobile Logged In](readme/images/navbar_mobile_logged_in.PNG)

#### **Footer**
The footer is located at the bottom of the page. It is fixed there so is always visible to the user wherever they are on the page. It features my name, alongside a Github icon which allows the user to navigate to my Github to view other projects. On the opposite side of the footer, I have included a link to the top of the page the user is on, which allows for easy navigation on the longer pages on mobile view.

![Footer](readme/images/footer.PNG)

### **Home Page**
The home page is the landing page for the website, and serves to tell the user what the website is about. It includes the main section, which explains the purpose of the site, underneath a large image of a person running, which introduces the theme of health. Underneath this, there are the articles which have been loaded into the Articles model. Whenever a new article is added, it will automatically display the title, featured image and topic which is taken from the Articles model. The admin user has the ability to add a new article.

#### **Main Section**
The main section consists of a large welcome image and the purpose of the website underneath it.

![Main Section](readme/images/home_main_section.PNG)

#### **Article Section**
The article section shows the user an introduction to each article that is available to read, alongside a link to the article and the article's featured image.

![Article Section](readme/images/home_article_feature.PNG)

### **Login Page**
The login page features a login form using AllAuth and formatted with the crispy forms package.

![Login Form](readme/images/login_form.PNG)

Once the user logs in, they are redirected to the home page and a successful message shows.

### **Signup Page**
The Signup page features a signup form using AllAuth and formatted with the crispy forms package.

![Signup Form](readme/images/signup_form.PNG)

### **Article Page**
The Article Detail page allows the user to learn more about health and fitness. Once the user clicks 'read more' next to one of the articles on the homepage, they are directed here and are able to read the entire article, and go back to the home page.

![Article Detail](readme/images/article_detail.PNG)

### **Health Hub**
The Health Hub page is specific to the logged in user, and only available once the user is logged in. It includes the details of their latest stats entry displayed in table format. This data is brought through from the health stats model, and if there are no entries, the table will read blank. Below the table are buttons to take the user to the other parts of the Health Hub, or back to the home page. 

![Health Hub](readme/images/health_hub.PNG)

#### **Update Stats**
The update stats form allows the user to add a new instance into the Health Stats model. The User and Date instances are automatically collected and stored, and the user is asked to provide the other stats. It requires all fields to be filled out, and in the formats described on the field labels. Once the form is submitted, the user is redirected to the health hub.

![Update Stats](readme/images/update_stats.PNG)

#### **Health Hub History**
The Health History page shows the user all of their logged data, displayed in table format with the most recent one at the top. On a mobile view, I added a horizontal scroll function to the table, in order to allow the user to view all of their data easily. The table has buttons to allows the user to edit and delete each entry in the final two columns. These are colour coded to emphasise the functionality- red for delete and blue for edit.
If the user has logged stats, the button for the weight track will also show to enable the user to track their weight.

![Health Hub History](readme/images/health_history.PNG)

#### **Edit Stats**
If the user clicks the edit button on an entry on the health history table, they are presented with a form, with the current values of that entry already filled out. The user is then able to edit the details they wish and and update the entry. Once the form is submitted, the user is redirected to the health history page.

![Edit Stats](readme/images/edit_form.PNG)

#### **Delete Stats**
If the user clicks the delete button on an entry on the health history table, they are presented with a warning message asking the user to confirm they are happy to delete this entry. The user can confirm, or go back to the previous page. If the user confirms, the entry is deleted and they are redirected to the health history page (minus the deleted entry).

![Delete Stats](readme/images/delete_entry.PNG)

#### **Health Hub Tracker**
The Health Hub Tracker page allows the user to track their weight stats over time in the form of a line graph. The Y axis displays the user's weight stats and the X axis displays the dates that these stats were registered. The date information is automatically gathered whenever the user submits a new entry using the Update Stats form. This provides some basic data visualisation for the user, and is an area which could be further developed to enable a wider variety of tracking options.

![Health Hub Tracker](readme/images/health_tracker.PNG)

## **Future Development**

### Chart Variation
The ability to have multiple different chart types for different stats, and being able to change them in realtime would be a feature to develop in future.

### Stat Choice
The ability for the user to choose which stats to log and track. This would require multiple forms and the logic to choose between them.

### Workout Planner
A workout planner held within the Health Hub which would allow the user to plan their workouts on a calendar, tick them off and register the stats from them. 

## Testing
Details of all testing undertaken can be found [here](TESTING.md).

## Deployment

This project was deployed to Heroku after being developed in the GitPod environment.

Steps to deploy:

- For the live project, ensure that DEBUG = False in settings.py.
- Go to your Heroku project dashboard, and click on the 'Deploy' tab.
- Click on the Github icon 'connect to GitHub'.
- Login to your GitHub account if needed, then search for the repository you want to connect the site to.
- When it shows up below, click 'connect'.
- Next to 'Automatic deploys' choose the branch you'd like to deploy from. In most cases this will be 'main'.
- Click 'Enable Automatic Deploys' if you would like Heroku to deploy your code everytime you push it to the above branch.
- If you prefer to deploy manually, scroll down to 'Manual deploy', choose your branch, and click 'Deploy Branch'.
- Scroll back to the top, and once it's finished deploying, click 'Open app', on the top right side.

## **Languages used**
- Python
- HTML
- CSS
- Javascript

## **Technologies used**
- Django
- Django AllAuth
- Bootstrap
- Crispy Forms
- Cloudinary (for image hosting)
- Balsamiq
- Unsplash (for images)
- Chart.js
- PostGreSQL

## Honourable Mentions
- Tom Ainsworth for the Readme structure, thanks so much!
- Christian Brown for helping me set up Cloudinary
- Slack
- Stack Overflow
- Daisy Gunn for helping me figure out why signup emails weren't sending
- CI London Community for general support when traversing the Django learning curve!

## Credits
- [Balsamiq](https://balsamiq.com/) for creating the wireframes
- VS Code for the text editor
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - Version 5.1.3, CSS framework for building a responsive front end.
- [Cloudinary](https://cloudinary.com/)
  - Used to store static files and media.
- [GitHub](https://github.com/)
  - Used for version control throughout the build process
  - GitHub Projects used to organise user stories and tasks.
  - Milestones were used to group user stories into sections.
- [Google Fonts](https://fonts.google.com/)
- Cripsy Forms for formatting all of my forms.
- General References
  - Stack Overflow
  - GeeksForGeeks
  - Django docs
  - Bootstrap Docs
  - W3Schools
  - Chart.js docs
- [Unsplash](https://unsplash.com/) for providing the images, specifically:
  - Brian Erickson for the home page image
  - Jenny Hill for the running article image
  - Jose Vazquez for the yoga article image
  - Sushil Ghimire for the Weightlifting article image
- [Lucid Chart](https://www.lucidchart.com/)- used for the creation of the database schema table.