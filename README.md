# HAPPY LEEKS RESTAURANT
Happy Leeks is a vegan Cafe based in Dublin that welcomes all people and serves delicious brunch items to customers. The goal is to create a nurturing space where people can connect, explore sustainable living, and indulge in mouthwatering dishes.
The website includes a Menu, Reservation options and account creations for the individual user. 

![Am I responsive image](media/readme_images/responsive.png)

Link to deployed website : [Happy Leeks](https://8000-sinastiller-pp4restaura-4dmd1gro0s9.ws-eu101.gitpod.io/)

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

Happy Leeks should invite peole to visit the cafe. The reservation system makes it possibe for the customer to book a table in addvance.

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
I have used [Figma](https://www.figma.com/) to create the wireframes. Each wireframe stands for the .html pages. Boxes with an X-line stand for an image. Subject is to change during the production of this website.

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



## **Features**

### General features

### Future Considerations

### Accessibility


## **Technologies Used**

### Languages Used

### Frameworks, Libraries & Programs Used
- Django
- PostgreeSQL
- Heroku
- Google Fonts
- Am I responsive https://ui.dev/amiresponsive
- Bootstrap
- Github
- Gitpod
- pep8 https://pep8ci.herokuapp.com/#
- https://jigsaw.w3.org/css-validator/
- https://validator.w3.org/
- https://favicon.io/favicon-generator/
- cloudinary
- figma
- font awesome
- coolors
- https://tinyjpg.com/
- https://cloudconvert.com/jpg-to-webp
- https://django-allauth.readthedocs.io/en/latest/


## **Deployment & Local Development**
## Deployment
This project was created by using Gitpod. I used the pre-built template from [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template).
The following commands were used:
* **git add .** - to add all the changes.
* **git commit -m "..."** - to commit all the changes to the local repository.
* **git push** - to push the committed changes to the GitHub repository.

### **Deployment to HerokuApp**
1. Create a list of requirements, commit and push to GitHub.
2. Create Account with Heroku.
3. On the Heroku Dashboard, select "create new app".
4. Give the app a name (it must be unique, as each app name can only exist once) and choose your current region.
5. Click "Create App".
6. On the "Settings" Tab, scroll to Config Vars.
7. Create a Config Var.
8. In the "KEY" field enter CREDS and for the "VALUE" field copy the creds.json link from your file and click "Add".
9. In the "KEY" field enter PORT and for the "VALUE" field enter 8000 and click "Add".
10. Add Buildpacks.
11. Choose the first one to be python and press "save".
12. Choose the second one to be nodejs and press "save".
13. Move to "Deploy" Tab.
14. Select "GitHub" as Deploment Methond and connect to your GitHub and the repository you want to upload.
15. Choose between automatic/manual deploy option.
16. After app was successfully deployed, click the "View" button to connect to webpage.


### Deployment

### Local Development

* #### How to Fork

* #### How to Clone


## **Testing**

Please find the carried out testing on [TESTING.md](TESTING.md).


## **Credits**

### Code Used
- https://www.youtube.com/playlist?list=PLBTOBXTz1YFZK0moSgoZq93V_AdvrUGSj - creating menu
- Hello Django
- I think therefore i blog
- https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78 --> for time.choices
- https://github.com/GeorgianF/Grace-P4-CI for update and delete modal
- https://github.com/Kaylaesmith1/bed-and-breakfast for reference throughout the project
- https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md#code-used
- stackoverflow 
- W3Schools
- django documentation
- Bootstrap 


### Content
- Menu from https://www.kyndcommunity.com/pages/kyndcafe, https://cafeorganic.co/

### Media
- unsplash
- pexels
### Acknowledgements
