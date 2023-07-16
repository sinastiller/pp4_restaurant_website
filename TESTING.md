# TESTING FOR HAPPY LEEKS RESTAURANT WEBSITE

![Am I Responsive](media/readme_images/responsive.png)


## Contents
* [Automated Testing](#automatedtesting)
  * [W3C Validator](#W3C-Validator)
  * [PEP8 Validator](#pep8validator)
  * [Responsiveness](#responsivness)
  * [Lighthouse](#lighthouse)
* [Manual Testing](#manualtesting)
* [Bugs](#bugs)
  * [Resolved Bugs](#resolvedbugs)
  * [Unresolved Bugs](#unresolvedbugs)


## [Automated Testing](#automatedtesting)

### [W3C Validator](#W3C-Validator)

[W3C](https://validator.w3.org/) was used to validate all HTML code used in this project. It was also used to validate CSS.

#### HTML

<details>
  <summary>Home Page - No errors</summary>

  ![HTML Validation - Home Page](media/readme_images/index.html.png)
</details>
<details>
  <summary>Menu Page - No errors</summary>
  
  ![HTML Validation - Menu Page](media/readme_images/menu.html.png)
</details>
<details>
  <summary>Login Page - No errors</summary>
  
  ![HTML Validation - Login Page](media/readme_images/login.html.png)
</details>
<details>
  <summary>Signup Page - No errors</summary>
  
  ![HTML Validation - Signup Page](media/readme_images/signup.html.png)
</details>
<details>
  <summary>Bookin Page - No errors</summary>
  
  ![HTML Validation - Booking Page](media/readme_images/table_booking.html.png)
</details>
<details>
  <summary>Manage Booking Page - No errors</summary>
  
  ![HTML Validation - Manage Booking Page](media/readme_images/manage_booking.html.png)
</details>
<details>
  <summary>Update Booking Page - No errors</summary>
  
  ![HTML Validation - Update Booking Page](media/readme_images/edit_booking.html.png)
</details>

<details>
  <summary>Logout Page - No errors</summary>
  
  ![HTML Validation - Update Booking Page](media/readme_images/logout.html.png)
</details>

#### CSS
There were no errors found, when validating CSS.

![CSS Validation](media/readme_images/css_validation.png)

### [PEP8 Validator](#pep8validator)

* To verify that the Python Code is written within the correct structure, I tested it in the Code Institute's ![PEP8 Validator](https://pep8ci.herokuapp.com/). The code was all clear, and no errors were found.

#### restaurant_website
<details>
  <summary>asgi.py - No errors</summary>
  
  ![PEP8 Validation - asgi.py](media/readme_images/restaurant_website_asgi.py.png)
</details>
<details>
  <summary>settings.py - No errors, except "line too long errors"</summary>
  
  ![PEP8 Validation - settings.py](media/readme_images/restaurant_website_settings.py.png)
</details>
<details>
  <summary>urls.py - No errors</summary>
  
  ![PEP8 Validation - urls.py](media/readme_images/restaurant_website_urls.py.png)
</details>
<details>
  <summary>wsgi.py - No errors</summary>
  
  ![PEP8 Validation - wsgi.py](media/readme_images/restaurant_website_wsgi.py.png)
</details>

#### restaurant app
<details>
  <summary>views.py - No errors</summary>
  
  ![PEP8 Validation - views.py](media/readme_images/restaurant_views.py.png)
</details>

#### menu App
<details>
  <summary>admin.py - No errors</summary>
  
  ![PEP8 Validation - admin.py](media/readme_images/menu_admin.py.png)
</details>
<details>
  <summary>models.py - No errors</summary>
  
  ![PEP8 Validation - models.py](media/readme_images/menu_models.py.png)
</details>
<details>
  <summary>urls.py - No errors</summary>
  
  ![PEP8 Validation - urls.py](media/readme_images/menu_urls.py.png)
</details>
<details>
  <summary>views.py - No errors</summary>
  
  ![PEP8 Validation - views.py](media/readme_images/menu_views.py.png)
</details>

#### booking app
<details>
  <summary>admin.py - No errors</summary>
  
  ![PEP8 Validation - admin.py](media/readme_images/booking_admin.py.png)
</details>
<details>
  <summary>forms.py - No errors, except "line too long errors"</summary>
  
  ![PEP8 Validation - forms.py](media/readme_images/booking_forms.py.png)
</details>
<details>
  <summary>models.py - No errors</summary>
  
  ![PEP8 Validation - models.py](media/readme_images/booking_models.py.png)
</details>
<details>
  <summary>urls.py - No errors</summary>
  
  ![PEP8 Validation - urls.py](media/readme_images/booking_urls.py.png)
</details>
<details>
  <summary>views.py - No errors</summary>
  
  ![PEP8 Validation - views.py](media/readme_images/booking_views.py.png)
</details>


### [Responsiveness](#responsivness)

The website was tested on a Windows Laptop and while in the inspect-mode on Google Chrome also tested on different available devices. It is fully responsive.

### [Lighthouse](#lighthouse)
Lighthouse was used to test the overall performance and accessibility, which both mentioned returned a very high rating.
<details>
  <summary>Home Page</summary>
  
  ![Lighthouse Testing - Home Page](media/readme_images/index.html_lighthouse.png)
</details>
<details>
  <summary>Menu Page</summary>
  
  ![Lighthouse Testing - Menu Page](media/readme_images/menu.html_lighthouse.png)
</details>
<details>
  <summary>Signup Page</summary>
  
  ![Lighthouse Testing - Signup Page](media/readme_images/signup.html_lighthouse.png)
</details>
<details>
  <summary>Login Page</summary>
  
  ![Lighthouse Testing - Login Page](media/readme_images/login.html_lighthouse.png)
</details>
<details>
  <summary>Booking Page</summary>
  
  ![Lighthouse Testing - Booking Page](media/readme_images/table_booking.html_lighthouse.png)
</details>
<details>
  <summary>Manage Booking Page</summary>
  
  ![Lighthouse Testing - Manage Booking Page](media/readme_images/manage_booking.html_lighthouse.png)
</details>
<details>
  <summary>Update Booking Page</summary>
  
  ![Lighthouse Testing - Update Booking Page](media/readme_images/edit_booking.html_lighthouse.png)
</details>
<details>
  <summary>Logout Page</summary>
  
  ![Lighthouse Testing - Logout Page](media/readme_images/logout.html_lighthouse.png)
</details>



## [Manual Testing](#manualtesting)

### Home Page
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Homepage | Display | Hompepage is displayed when url is passed intow browser | PASS
Block Title | Display | Vegan Cafe 🌱 should be displayed when on homepage | PASS
Nabvar | Display | When user is not logged, only links to "Home", "Menu", "My Account" should be visible | PASS
Navbar Dropdown | Display | When user is not logged in, only links to "Sign Up" and "Login" should be visible | PASS
About Section | Display | Should be displayed below navbar | PASS
Gallery Section | Display | Should be displayed below about section | PASS
Essential Information Section| Display | Should be displayed below gallery section | PASS
Footer | Display | Should only be visible at the bottom of the webpage | PASS
Footer | Links | Social media links should open a blank page to each their social media pages | PASS
Navbar | Links | "Menu" Link should open menu.html | PASS
Navbar | Links | "My Account" should display a dropdown | PASS
Navbar | Links | "Sign Up" should open signup.html | PASS
Navbar | Links | "Login" should open login.html | PASS

### Menu Page
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---

## [Bugs](#bugs)

### [Resolved Bugs](#resolvedbugs)

Footer was visible while scrolling up and down the webpage. Taking off the class "footer-bottom" and passing it a margin and padding of 0 made the footer stick to the bottom of the webpage.

### [Unresolved Bugs](#unresolvedbugs)
- Navlinks should be active to show user which site they are currently on. I did not find out how to display this using bootstrap. 
- When displaying the existing bookings the name that appears on the booking is the actual username and not the name that was stated on the booking form.
- When asked to enter the date for the booking, also past dates are possible to be entered.