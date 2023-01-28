# Testing

[Return to README.md](README.md)

- [Bugs and Fixes During the Development Process](#bugs-and-fixes-during-the-development-process)
- [Lighthouse](#lighthouse)
  - [Mobile](#mobile)
  - [Desktop](#desktop)
- [Validators](#validators)
  - [HTML](#html)
  - [CSS](#css)
  - [Javascript](#javascript)
  - [Python](#python)
- [User Stories](#user-stories)

## Bugs and Fixes During the Development Process
- Content Wrapper
    - Issue - Content Wrapper was not covering entire screen on screens with low content.
    - Cause - Height was set to 100% (of content).
    - Solution - Added min-height of 100vw to content wrapper.
- Profile Display
    - Issue - Profile URL wasn't displaying correctly.
    - Cause - The profile did not have a slug field in the model.
    - Solution - I added in a slug field to the profile model, which fixed the issue.
- Profile formatting
    - Issue - Order history wasn't displaying correctly on smaller screens
    - Cause - The table was reponsive up until small screens, but was still too big.
    - Solution - I amended the CSS to display as a list instead of a table on small screens.
- Emails
    - Issue - Emails weren't sending correctly.
    - Cause - Email templates weren't saved in the correct location.
    - Solution - Email templates moved to the templates folder in root directory.
- Burger Menu
    - Issue - Burger Menu not working on screens with scripts.
    - Cause - Hadn't added block.super into postloadjs
    - Solution - Added block.super, which fixed the issue.
- Home Images
    - Issue - Images on the home page were not displaying.
    - Cause - There was an extra slash in front of the image url.
    - Solution - I removed this slash and the images displayed.
- Checkout
    - Issue - Order was not being created after successful payment.
    - Cause - The JSON data was not coming through to the order_success view in the correct format.
    - Solution - I added this code to the order_success view in order to decode the JSON before using it.  my_json = request2.decode('utf8').replace("'", '"')

## Lighthouse

### Desktop

![Lighthouse Desktop Score](readme/testing/lighthouse_desktop.PNG)

When I first tested, my accessibility score was quite low, because I had forgotten to add alt tags to my links, which wouldn't have allowed screen-readers to pick them up efficiently. I added these in and re-ran the lighthouse report, which displayed an accessibility score of 100.

### Mobile

![Lighthouse Mobile Score](readme/testing/lighthouse_mobile.PNG)


## Browser Compatability

Google Chrome, Microsoft Edge, Mozilla Firefox and Safari all display content and images correctly and all links work and open in new window.
This was tested on a laptop, PC, iPad, Iphone SE, Galaxy S8, Pixel 6 and a Motorola G9.

## Validators

### HTML

![Home HTML validation](readme/testing/html_checker_home.PNG)

![Reviews HTML validation](readme/testing/html_checker_reviews.PNG)

There are some warnings regarding the javscript in the html checker, however they don't affect the usability of the site and don't present any errors.

### CSS

No errors or warnings were found for my custom CSS.

### JavaScript

There are 2 scripts in my files, one located in base.html which is my function for setting the timeout of messages. The other is my chart.js script which was based on the example provided in the chart.js [documentation](https://www.chartjs.org/docs/latest/).

When posting each script into the [javascript validator](https://jsvalidator.com/)- the only errors found were as a consequence of using django's template language.

### Python

![Pep8online Testing](readme/testing/python_checker.PNG)

[Python Checker](https://www.pythonchecker.com) was used to test all python files. All efforts were made to make all code pep8 compliant, with the exception of the settings.py file, which Django state in their docs is okay to ignore should it make the code uglier or harder to read.

## User Stories

### As a user, I want to be able to learn about health and fitness.
- On the home page the user can read articles about health and fitness. Whenever the admin adds a new article, this will automatically be updated on the home page.

### As a user I want to be able to sign up to access the website’s features.
- There is signup functionality clearly shown from the navbar, and the user is able to create a user account using their email to confirm.

### As a user I want to be able to Log in to access my details privately.
- There is login functionality clearly shown from the navbar, and will allow a previously signed up user to log in as themselves. This provides access to the health hub section of the website, where the user can track their health stats.

### As a user I want to be able to logout to protect my data.
- There is logout functionality clearly shown from the navbar when the user is logged in. If the user has not logged in, this will not show as an option.

### As a user I want to be able to view my stats.
- Once the user has logged in, they can access the health hub section using 'My Health' from the navbar. From here, they are shown their most recent stats and have the ability to view all of their stats within a table.

### As a user I want to be able to edit my stats.
- When viewing their stats history in table format, the user is able to click the 'edit' button next to the stat they wish to edit. They are then presented with a form, in which they can change any of the stats that they wish. Once they confirm, the entry will be edited and they will be redirected.

### As a user I want to be able to delete my stats.
- When viewing their stats history in table format, the user is able to click the 'delete' button next to the stat they wish to delete. They are then taken to another screen asking the user to confirm that they are happy to delete this entry. Once they confirm, the entry will be deleted and they will be redirected.

### As a user I want to be able to see how my weight changes over time in graph format.
- The user can access and see their weight stats on a tracker using the weight tracker page. This allows the user to track their weight over time, with the weight being shown in the form of a line graph. Along the bottom, the dates of each weight entry are registered.


## Manual Testing

### Forms
- Signup form
    - When trying to submit a blank form, user is provided with an error message asking them to fill out the form.
    - When trying to use something other than an email address in the email field, the user is provided with an error message advising them to provide an email in the correct format.
    - When trying to use an existing username, the user is provided with an error message asking them to use a different username.
    - When trying to leave the username blank, the user is provided with an error message asking them to provide a username.
    - When trying to leave the password blank, the user is provided with an error message asking them to provide a password.
    - When trying to leave the confirm password blank, the user is provided with an error message asking them to confirm their password.
    - When trying to use a different password in the confirm password field, the user is provided with an error message asking them to use the same password as the password field.
    - When trying to use a short password, the user is provided with an error message asking them to create a longer password.
- Login form
    - When trying to submit a blank form, user is provided with an error message asking them to fill out the form.
    - When trying to submit incorrect details on the form, the user is provided with an error message asking them to provide correct details.
- Update form
    - When trying to submit a blank form, user is provided with an error message asking them to fill out the form.

### Links
All external links work correctly and the Github/Facebook links open in a new tab, to avoid the user leaving the website.

[Return to README.md](README.md)