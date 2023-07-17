# HAPPY LEEKS RESTAURANT
Happy Leeks is a vegan Cafe based in Dublin that welcomes all people and serves delicious brunch items to customers. The goal is to create a nurturing space where people can connect, explore sustainable living, and indulge in mouthwatering dishes.
The website includes a Menu, Reservation options and account creations for the individual user. 

![Am I responsive image](media/readme_images/responsive.png)

Link to deployed website : [Happy Leeks](https://restaurant-website-ee029a10692a.herokuapp.com/)

## Contents

* [User Experience](#user-experience)
    * [User Stories](#user-stories)

* [Design](#design)
    * [Colour Scheme](#colourscheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Wireframes](#wireframes)

* [Features](#features)
    * [General Features](#general-features)
    * [Future Considerations](#future-considerations)
    * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)

* [Deployment & Local Development](#deployment&localdevelopment)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

---

## [**User Experience**](#user-experience)

Happy Leeks should invite peole to visit the cafe. The reservation system makes it possibe for the customer to book a table in advance.

### [User Stories](#user-stories)

#### User
- As a site user I can visit the restaurant's landing page so that I can find information about the restaurant.
- As a site user I can view the menu so that I know what food the restaurant has to offer.
- As a site user I can register an account so that I can book a table for one or more guests at a particular time and date.
- As a logged in user I can make a booking so that I can book a table/multiple tables for one or more guests at a specific date and time, view and update my existing booking/s or delete any existing booking.
- As a logged-in user I can see my login status so that I know that I am logged in.
- As a site user I can find links to their social media so that I can follow the restaurant on social media.
- As a site user I can view essential information so that I can find out about the address, business hours, phone number and other important information.
- As a site user I can view photos so that I get a feel of the atmosphere and what style of food is served in the restaurant.

#### Admin
- As an admin I can manage items on the menu so that I can create, view, update and delete any items.
- As an admin I can manage the bookings so that I can create, view, update and delete any bookings and avoid any double bookings.


## [**Design**](#design)

### [Colour Scheme](#colour-scheme)
This website uses a palette of lighter gray and blue tones, as well as light and dark green and light pink tones. It also uses some variants of the same colour scheme belonging to their colour family. It was created by using [Coolors](https://coolors.co/).
![Colour Palette](media/readme_images/colour_palette.png)

### [Typography](#typography)
I have imported the following Google Fonts:
* Playfair Display 400, 500 for headings on the website.
* Open Sans 300, 400, 600 for the body text on the website.

### [Imagery](#imagery)
Imagery is used regarding restaurant environment and food content on the website. They are taken from various websites, which are credited down below in the [Credits](#credits) section.

### [Wireframes](#wireframes)
I have used [Figma](https://www.figma.com/) to create the wireframes. Each wireframe stands for the individual .html pages. Boxes with an X-line stand for an image. Subject is to change during the production of this website.

#### Home Page
![Wireframe - Home Page](media/readme_images/landingpage_wireframe.png)

#### Login Page
![Wireframe - Login Page](media/readme_images/login_wireframe.png)

#### Logged in user
![Wireframe - Home Page](media/readme_images/loggedin_wireframe.png)

#### Signup Page
![Wireframe - Signup Page](media/readme_images/signup_wireframe.png)

#### Menu Page
![Wireframe - Menu Page](media/readme_images/menu_wireframe.png)

#### Booking Page
![Wireframe - Booking Page](media/readme_images/booking_wireframe.png)

#### Manage Booking
![Wireframe - Manage Booking Page](media/readme_images/editbooking_wireframe.png)


## [**Features**](#features)

### [General features](#general-features)
The webpage consists of a Homepage, Menu page, Booking page, Manage Booking page, Login page, Signup page and Logout page.

All of these pages contain:
* A responsive navigation bar:
    * The name of the restaurant is positioned on the left-hand side with the logo on the right of it. Both link to Home Page.
    * The other navigation links are located on the right-hand side.
    * The colour is a shade of light green. 
    ![Navbar - not logged in](media/readme_images/navbar1_not%20registered.png)
    * When user is not logged in, the dropdown menu links include link to Sign Up and Login.
    ![Navbar - not logged in](media/readme_images/navbar2_not%20registered.png)
    * When user is loggged in, the link to Book a Table appears in the navbar as well as links to Manage Booking and Logout on the dropdown menu.
    ![Navbar - logged in](media/readme_images/navbar1_loggedin.png)
    ![Navbar - logged in](media/readme_images/navbar2_loggedin.png)
    * When hovered over navbar links' colour changes to a darker shade.

* A responsive footer :
    * The footer contains the social media icons of Facebook, Instagram, Twitter, and Pinterest, which open all in a new tab when clicked on.
    * It also contains the copyright with the current year.
    ![Footer](media/readme_images/footer.png)

#### Home Page

The Homepage is the landing page of the website, where a user lands first when opening the url. It contains the navbar at the top and footer at the bottom. Between the user can find a small about section with an image of the interior of the restaurant, a gallery section to view some of the dishes, the decoration and atmosphere of the restaurant. Below is the essential information section, where the user can find the location, opening times and contact details.
* About Section
    ![About Section](media/readme_images/about_section.png)
* Gallery Section
    ![Gallery Section](media/readme_images/gallery_section.png)
* Essential Information Section
![Essential Information Section](media/readme_images/essentialinfo_section.png)

#### Menu Page
The Menu page can be reached from the landing page. It contains the navbar at the top and footer at the bottom. The menu contains four categories (COOL CRAVINGS, HOT 'N' TASTY TREATS, SIP & SAVOUR, SWEET SURRENDERS). At the top of each menu card the user can find the food category, with the individual menu items listed below including a small description of the item and the price.
![Menu Page](media/readme_images/menu.png)

#### Signup Page
The Signup page can be reached via the dropdown link from the navbar. It contains the navbar at the top and footer at the bottom. The user will be prompted with a Signup form, to enter their username, email(optional), password and confirm password. If they have already an account, they can reach the Login page via the link just at the top of the Signup form. Only valid input is allowed and user must click Signup button to proceed with registering. Once completed the user will be redirected to the landing page and a message will pop up that user has signed up successfully.
![Signup Page](media/readme_images/signup.png)

#### Login Page
The Login page can be reached via the dropdown link from the navbar. It contains the navbar at the top and footer at the bottom. The user will be prompted with a Login form, to enter their username and password, which they have created an account with. If they have not yet created an account the can reach the Signup page via the link just at the top of the Login form. As only valid input is allowed, a message will pop up that login was unsuccessful if user has entered incorrect details. User must click Log In button to log in. Once completed the user will be redirected to the landing page and message will pop up that user is logged in.
![Login Page](media/readme_images/login.png)

#### Booking Page
The Booking page can be reached via the navbar once the user has logged in. It contains the navbar at the top and footer at the bottom. The user will be prompted with a Booking form, to select the number of guests, their name, phone number, preferred date and time. To fullfill the booking they have to confirm by clicking the "Make reservation" button. If there was any non-valid input, a message will pop up that booking was unsuccessful and the user will be asked to re-enter the details before they can proceed. Once booking is complete the user will be redirected to the Manage Booking page and a message will pop up that booking was successful.
![Booking Page](media/readme_images/make_booking.png)

#### Manage Booking Page
The Manage Booking page can be reached via the dropdown menu once the user has logged in. It contains the navbar at the top and footer at the bottom. It displays any existing bookings to the user, that were made by them. Information containing the booking name, date & time of booking and the number of the attending guests. The user has also the possibilty to update and delete their booking. 
![Manage Booking](media/readme_images/manage_booking.png)

By clicking on "Edit", the user lands on edit_booking.html where they can updated their booking. It is the same booking form used for booking a table, but with details already filled in, from when the booking was made. The user is able to make any adjustments and once happy can confirm their booking by "Update Reservation". If there was any non-valid input, a message will pop up that update was unsuccessful and the user will be asked to re-enter the details. 
![Edit Booking](media/readme_images/edit_booking.png)
If all valid a modal will pop up for the user to confirm their request. 
![Edit Modal](media/readme_images/update_modal.png)
Once accepted, user will be redirected to Manage Booking page and a message will pop up that update was successfull. They now can view their updated booking.

If they choose to delete an existing booking, they can do so by clicking on "Delete". A modal will pop up to assure them of their action. Once booking is deleted a message will pop up confirming the deleted booking. 
![Delete Modal](media/readme_images/delete_modal.png)

#### Logout Page
The Logout Booking page can be reached via the dropdown menu once the user has logged in. It contains the navbar at the top and footer at the bottom. The user is asked to confirm if they want to sign out. If user proceeds, they will be directed to the landing page. A message will pop up to let them know that they have logged out successfully.
![Logout Page](media/readme_images/logout.png)

### [Future Considerations](#future-considerations)
Future features that could be implemented on the website could include being able to add reviews and view reviews of other customers. Another implementation could be an online ordering system.

### [Accessibility](#accessibility)
For better accessibility  I added alt-labels to all my images for vision-impaired users. Accessibilty was also tested on lighthouse, which reached a very high score on every testing.

## [**Technologies Used**](#technologies-used)

### [Languages Used](#languages-used)
* *HTML*
* *Python*
* *CSS*
* *JavaScript*

### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Django](https://www.djangoproject.com/) - Main python framework used for this project.
- [ElephantSQL](https://www.elephantsql.com/) - Stores database for this project.
- [Heroku](https://heroku.com/) - Cloud-based platform used to deploy this project.
- [Bootstrap 5.3](https://getbootstrap.com/) - CSS styling used for decorating HTML content.
- [Github](https://github.com/) - Used for version control and agile development progress.
- [Gitpod](https://www.gitpod.io/) - Used as cloud-development platform.
- [Google Fonts](https://fonts.google.com/) - Used for imported fonts for this project.
- [Am I responsive](https://ui.dev/amiresponsive) - Used to check if website is fully responsive.
- [PEP8](https://pep8ci.herokuapp.com/#) - Used to validate python code.
- [W3C](https://validator.w3.org/) - Used to validate HTML and CSS.
- [Favicon](https://favicon.io/favicon-generator/) - Used to create Favicon for this project.
- [Cloudinary](https://cloudinary.com/) - Used to store website images of this project on a cloud-platform.
- [Figma](https://www.figma.com/) - Used to design wireframes.
- [Font Awesome](https://fontawesome.com/) - Used for icons.
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Tiny JPG](https://tinyjpg.com/) - Used to convert images.
- [Cloud Convert](https://cloudconvert.com/jpg-to-webp) - Used to convert images.


## [**Deployment & Local Development**](#deployment--local-development)

This project was created by using Gitpod. I used the pre-built template from [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template).
The following commands were used:
* **git add .** - to add all the changes.
* **git commit -m "..."** - to commit all the changes to the local repository.
* **git push** - to push the committed changes to the GitHub repository.

### [Deployment](#deployment)
#### In the Terminal:
1. Install Django and gunicorn.(pip3 install 'django<4' gunicorn)
2. Install supporting libraries.(pip3 install dj_database_url==0.5.0 psycopg2)
3. Install Cloudinary Libraries. (pip3 install dj3-cloudinary-storage)
4. Create requirements file.(pip3 freeze --local > requirements.txt)
5. Create Project.(django-admin startproject PROJ_NAME .)
6. Create App.(python3 manage.py startapp APP_NAME)
#### In settings.py:
7. Add to installed apps.('APP_NAME')
#### In the Terminal
8. Migrate Changes.(python3 manage.py migrate)
9. Run Server to Test.(python3 manage.py runserver)
#### On elephantsql.com:
10. Log in to your ElephantSQL account.
11. Click “Create New Instance”.
12. Set up your plan.
13. Click “Select Region”.
14. Click “Review”.
15. Return to the ElephantSQL dashboard and click on the database instance name for this project.
16. Copy your ElephantSQL database URL using the Copy icon. It will start with postgres:// .
#### On heroku.com:
17. Create new Heroku App.
18. Open the settings tab.
19. Click Reveal Config Vars.
20. Add a Config Var called DATABASE_URL and add ElephantSQL database url.
#### In the terminal:
21. Create new env.py file on top level directory.
#### In env.py:
22. Import os library.
23. Set environment variables.
24. Add in secret key.
#### On heroku.com:
25. Add Secret Key to Config Vars, (SECRET_KEY)
#### In settings.py:
26. Reference env.py.
27. Remove the insecure secret key and replace.(os.environ.get('SECRET_KEY'))
28. Comment out the old DataBases Section.
29. Add new DATABASES Section. (dj_database_url.parse(os.environ.get("DATABASE_URL")))
#### In the terminal:
30. Save all files and Make Migrations.
#### On cloudinary.com:
31. Copy your CLOUDINARY_URL from Clouinary Dashboard.
#### In env.py:
32. Add Cloudinary URL to env.py.
#### On heroku.com:
33. Add Cloudinary URL to Heroku Config Vars.(CLOUDINARY_URL)
34. Add DISABLE_COLLECTSTATIC to Heroku Config Vars. (value = 1)
#### In settings.py:
35. Add Cloudinary Libraries to installed apps. ('cloudinary_storage', 'cloudinary',)
36. Tell Django to use Cloudinary to store media and static files.
37. Link file to the templates directory in Heroku.(TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates'))
38. Change the templates directory to TEMPLATES_DIR.
39. Add Heroku Hostname to ALLOWED_HOSTS. ("PROJ_NAME.herokuapp.com", "localhost")
#### In the terminal:
40. Create a Procfile on the top level directory.
#### In Procfile:
41. Add web: gunicorn PROJ_NAME.wsgi.
#### Final deployment:
42. Set DEBUG = False in the settings.py
43. On Heroku select "GitHub" as Deploment Method and connect to your GitHub and the repository you want to upload.
44. Choose between automatic/manual deploy option. 
45. After app was successfully deployed, click the "View" button to view the deployed live site.


### [Local Development](#local-development)

* #### [How to Fork](#how-to-fork)
1. Navigate to [project repository](https://github.com/sinastiller/pp4_restaurant_website).
2. Click on "Fork" in the top right corner.
3. Under "Owner," select the dropdown menu and click on owner for the forked repository.
4. To change the name of repo, enter a new name.
5. Enter description(optional).
6. Choose which branches to include.
7. Click "Create Fork".

* #### [How to Clone](#how-to-clone)
1. Navigate to [project repository](https://github.com/sinastiller/pp4_restaurant_website).
2. Click on the button Code next to the Gitpod button.
3. Choose between HTTPS, SSH and GitHub CLI and copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.

## [**Testing**](#testing)

Please find the carried out testing on [TESTING.md](TESTING.md).


## [**Credits**](#credits)

### [Code Used](#code-used)
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [W3Schools](https://www.w3schools.com/)
- [Stackoverflow](https://stackoverflow.com/)
- [Hello Django Walkthorugh Project](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925)
- [I think therefore I blog Walkthorugh Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - used as reference when creating account authorisation.
- [Kayla's Bed and Breakfast](https://github.com/Kaylaesmith1/bed-and-breakfast) - used for general reference, ideas and logic throughout the project.
- [Youtube](https://www.youtube.com/playlist?list=PLBTOBXTz1YFZK0moSgoZq93V_AdvrUGSj) - used as a reference when creating the menu.
- [Django Tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78) - used as reference for creating set times on the booking form.
- [Grace's Repository](https://github.com/GeorgianF/Grace-P4-CI) - used as reference for update and delete modal
- [Kera Cudmore's sample readme](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md#code-used) - used when creating README.md and TESTING.md


### [Content](#content)
The Menu content was created from [KYND Cafe](https://www.kyndcommunity.com/pages/kyndcafe), [Cafe Organic](https://cafeorganic.co/), and my own creations.

### [Media](#media)
The images were downloaded from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/).

### [Acknowledgements](#acknowledgements)
I would like to express my sincere gratitude to my mentor, Jubril Akolade, for his invaluable guidance, unwavering support, and endless patience throughout the entire project. 

Additionally, I would like to extend a special thanks to the Tutoring Team at Code Institute, who provided continuous assistance whenever I encountered challenges, as well as the exceptional Slack Community, whose members were always ready to lend a helping hand. 

I am truly grateful to all of you for your invaluable guidance and support throughout this project!