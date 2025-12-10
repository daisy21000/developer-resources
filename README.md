# Developer Toolkit

<img width="1918" height="870" alt="Developer Toolkit Home Page" src="https://github.com/user-attachments/assets/c7476565-dd61-419f-b9ce-416f9d0d22e8" />

<p align="center">
  <a href="https://developer-toolkit-1de11126e2a2.herokuapp.com/" target="_blank">Live Project</a>
</p>

## Table of Contents

- [Developer Toolkit](#developer-toolkit)

- [Table of Contents](#table-of-contents)

- [Introduction](#introduction)

- [UX Design](#ux-design)

- [Agile](#agile)

- [Features](#features)

- [Built With](#built-with)

- [Deployment](#deployment)

- [Testing and Validation](#testing-and-validation)

- [AI Implementation](#ai-implementation)

- [Credits](#credits)

## Introduction

Developer Toolkit is a web application built with Django to assist developers with helpful resources. This project has been built with HTML, CSS, JavaScript and Bootstrap 5 for the front-end and Python and Django for the back-end. Users are able to see resources as well as being able create, update and delete their own.

## UX Design

### External User's Goal

The user seeks resources to aid in web development with the ability to log in and add their own and favourite them for easy access. The user expects the website to be organised and responsive for all screen sizes.

### Site Owner's Goal

The site owner wants to create a website for developers to access helpful resources shared by fellow developers to aid them in their work. The information will be stored in a database and curated to ensure that all the content is relevant and appropriate.

### User Stories

The user stories for the project, along with acceptance criteria and tasks, can be found on the <a target="_blank" href="https://github.com/users/daisy21000/projects/8/views/1">project board</a>.

### Colours

I wanted a minimalistic design, hence I chose simple colours with a light grey for the background and a black for the text, the rest being button colours to make them stand out.

<details>
<summary>Colour palette</summary>
<img width="1600" height="1200" alt="palette" src="https://github.com/user-attachments/assets/343d1a38-2bc0-48dc-bfb3-b890d3098ac2" />
</details>

### Fonts

I used "Monserrat" for the body font as it is very readable and clean, and "Roboto Mono" for the heading font to give the website a unique look.

### Wireframes

The wireframes for the website were created using Balsamiq to map out the layout of the website and to visualize what it would look like. These wireframes served as a guide for the foundation of the website, ensuring the content was laid out in an organised way.

<details>
<summary>Home Page</summary>
<img width="839" height="575" alt="Screenshot 2025-12-09 130232" src="https://github.com/user-attachments/assets/393904e2-1509-4aff-85fb-4bd4430465ac" />
</details>

<details>
<summary>Category Detail</summary>
<img width="836" height="500" alt="Screenshot 2025-12-09 130258" src="https://github.com/user-attachments/assets/2a49badc-9b7d-4951-97c1-771828e3bed8" />
</details>

<details>
<summary>Resource Modal</summary>
<img width="838" height="500" alt="Screenshot 2025-12-09 130532" src="https://github.com/user-attachments/assets/68869281-747f-401d-b17f-cc4126e97c0d" />
</details>

<details>
<summary>Search Results</summary>
<img width="835" height="501" alt="Screenshot 2025-12-09 130521" src="https://github.com/user-attachments/assets/60a0afed-e361-46ef-af49-b36362fc79fe" />
</details>

<details>
<summary>Favourites</summary>
<img width="837" height="501" alt="Screenshot 2025-12-09 130335" src="https://github.com/user-attachments/assets/7f972265-20f2-4935-8751-b9879406d714" />
</details>

<details>
<summary>Add Resource</summary>
<img width="837" height="498" alt="Screenshot 2025-12-09 130314" src="https://github.com/user-attachments/assets/e339693a-c678-4374-8b82-3269602ec470" />
</details>

<details>
<summary>Suggest Category</summary>
<img width="840" height="500" alt="Screenshot 2025-12-09 130547" src="https://github.com/user-attachments/assets/0cdc67e2-3b38-4f8a-9f81-e862ae78b6ec" />
</details>

<details>
<summary>Login</summary>
<img width="838" height="502" alt="Screenshot 2025-12-09 130409" src="https://github.com/user-attachments/assets/34e45ddd-6a25-4ba5-bd35-42c4ec9c7af8" />
</details>

<details>
<summary>Register</summary>
<img width="838" height="502" alt="Screenshot 2025-12-09 130431" src="https://github.com/user-attachments/assets/fad4a4c0-40ec-4b9c-bf40-3ea703f8fbb2" />
</details>

<details>
<summary>Logout</summary>
<img width="837" height="499" alt="Screenshot 2025-12-09 130457" src="https://github.com/user-attachments/assets/917e606b-8af4-4efb-9f22-8303db3a62d8" />
</details>

## Agile

This project was built following the Agile methodology throughout. Using the MoSCoW prioritisaion, the most essential features were first delivered to create the MVP. After that, the rest of the features were worked on based on their importance. The user stories were managed through a [GitHub Project Board](https://github.com/users/daisy21000/projects/8) to keep track of the user stories and the current progress. Following the Agile methodology greatly enhaced development and allowed all important work to be done in a timely manner.

The user stories were labelled based on their importance:

- **Must Have** for important features that are essential for the project's MVP
- **Should Have** for important features that are not essential for the project's MVP but improve user experience
- **Could Have** for optional features that would enhance the project but should only be done if time allows

The project board contains all the user stories, as well as their acceptance criteria and tasks. You can find the project board here: [Capstone Project Board](https://github.com/users/daisy21000/projects/8)

## Features

Developer Toolkit offers ways for developers to share resources. Here are some key features:

### User Authentication

Users can login and register to the website to gain access to certain features.

<details>
<summary>Login Page</summary>
<img width="1917" height="869" alt="Login Page" src="https://github.com/user-attachments/assets/e8ed80a5-5410-4421-8f74-af12c85d7cb0" />
</details>

<details>
<summary>Register Page</summary>
<img width="1903" height="865" alt="Register Page" src="https://github.com/user-attachments/assets/ec49015e-3d9d-406f-9ac7-ec6bfb401886" />
</details>

### View Resources By Category

Through the list of categories in the home page, the user can find resources related to that category. When the resource is clicked, it reveals a modal with more information regarding the resource. The resources can also be sorted.

<details>
<summary>Category list in Home Page</summary>
<img width="1899" height="789" alt="Category list in Home Page" src="https://github.com/user-attachments/assets/7bce078b-1a1d-4afe-8fe9-eebe01978741" />
</details>

<details>
<summary>List of Resources in Category</summary>
<img width="1917" height="869" alt="List of Resources in Category" src="https://github.com/user-attachments/assets/56601c81-bde2-482e-8e1b-6c490c1f38f6" />
</details>

<details>
<summary>Resource Modal</summary>
<img width="1918" height="868" alt="Resource Modal" src="https://github.com/user-attachments/assets/72e62d00-8117-4528-ba02-2512581fb86c" />
</details>

<details>
<summary>Resource Sorting</summary>
<img width="1900" height="776" alt="Resource Sorting" src="https://github.com/user-attachments/assets/d22198d7-0243-41d7-8e24-78efee6745e6" />
</details>

### Add Resource

Logged-in users can add resources to the website to help contribute. After filling in the form, if valid, the user recieves a confirmation message.

<details>
<summary>Add Resource Form</summary>
<img width="1899" height="866" alt="Add Resource Form" src="https://github.com/user-attachments/assets/c9c1cf11-e296-4659-99da-9865c24ae1dc" />
</details>

<details>
<summary>Add Resource Success Message</summary>
<img width="1901" height="798" alt="Add Resource Success Message" src="https://github.com/user-attachments/assets/cd750eef-1441-4e26-8a44-3d2d7354a10e" />
</details>

### Edit Resource

Logged-in users can edit their own resources using the edit button on the resource. After filling in the form, if valid, the user recieves a confirmation message.

<details>
<summary>Edit Resource Button</summary>
<img width="1917" height="867" alt="Edit Resource Button" src="https://github.com/user-attachments/assets/154ea397-4478-4f19-b99e-63ab1e17c793" />
</details>

<details>
<summary>Edit Resource Form</summary>
<img width="1899" height="870" alt="Edit Resource Form" src="https://github.com/user-attachments/assets/353e1d0c-2f9b-4810-a42a-e9ce92524396" />
</details>

<details>
<summary>Edit Resource Success Message</summary>
<img width="1900" height="868" alt="Edit Resource Success Message" src="https://github.com/user-attachments/assets/f3745da8-bbe3-4aa1-9574-76f40f34c443" />
</details>

### Delete Resource

Logged-in users can delete their own resources using the delete button on the resource. When clicked, a modal appears for confirmation. After confirming, the user recieves a success message.

<details>
<summary>Delete Resource Button</summary>
<img width="1917" height="867" alt="Delete Resource Button" src="https://github.com/user-attachments/assets/154ea397-4478-4f19-b99e-63ab1e17c793" />
</details>

<details>
<summary>Delete Confirmation Modal</summary>
<img width="1917" height="867" alt="Delete Confirmation Modal" src="https://github.com/user-attachments/assets/0bdb139d-7ece-4c9f-8af2-739c808e8fb1" />
</details>

<details>
<summary>Delete Success Message</summary>
<img width="1914" height="864" alt="Delete Success Message" src="https://github.com/user-attachments/assets/667a2c46-77fd-42c5-8ea4-07704ce4c5f2" />
</details>

### Favourite Resources

Logged-in users can favourite resources and find them in the favourites page. The resources in the favourites page can also be sorted. The resources have a favourite button that toggles favourite status. When clicked, the user recieves a success message.

<details>
<summary>Favourite Resource Button</summary>
<img width="1917" height="867" alt="Favourite Resource Button" src="https://github.com/user-attachments/assets/154ea397-4478-4f19-b99e-63ab1e17c793" />
</details>

<details>
<summary>Favourite Resource Success Message</summary>
<img width="1915" height="866" alt="Favourite Resource Success Message" src="https://github.com/user-attachments/assets/142dddcb-09fd-463d-8f66-76dd6bf38cc4" />
</details>

<details>
<summary>Favourite Resources Page</summary>
<img width="1918" height="867" alt="Favourite Resources Page" src="https://github.com/user-attachments/assets/1df7cd38-3088-4f28-b2f9-ae1ff0530397" />
</details>

<details>
<summary>Favourite Resources Sorting</summary>
<img width="1898" height="870" alt="Favourite Resources Sorting" src="https://github.com/user-attachments/assets/9c84674d-2173-4767-aeda-cd7d949bcec2" />
</details>

### Suggest Categories

Logged-in users can suggest categories using the form. After submitting the form, if valid, the user recieves a success message.

<details>
<summary>Suggest Category Form</summary>
<img width="1917" height="868" alt="Suggest Category Form" src="https://github.com/user-attachments/assets/de036a72-587d-45e8-a475-29af3f5334d2" />
</details>

<details>
<summary>Suggest Category Success Message</summary>
<img width="1915" height="865" alt="Suggest Category Success Message" src="https://github.com/user-attachments/assets/888fd136-da28-43db-b22b-65e7e3329e20" />
</details>

### Search Resources

Users can search resources using the search bar in the home page and the search page. If any resources match the search query, they show up in the search page. The search can also be sorted and filtered.

<details>
<summary>Home Page Search Bar</summary>
<img width="1899" height="864" alt="Home Page Search Bar" src="https://github.com/user-attachments/assets/ad2b6d58-3dd9-47e0-b45a-9d6c53354320" />
</details>

<details>
<summary>Search Page</summary>
<img width="1916" height="869" alt="Search Page" src="https://github.com/user-attachments/assets/d5a05b1c-8c78-455e-b553-3fb17cbe64b8" />
</details>

<details>
<summary>Search Page Resources</summary>
<img width="1915" height="870" alt="Search Page Resources" src="https://github.com/user-attachments/assets/3886a53b-17ee-4ecf-84b7-5f2750b2aca4" />
</details>

<details>
<summary>Search Sorting and Filtering</summary>
<img width="1898" height="833" alt="Search Sorting and Filtering" src="https://github.com/user-attachments/assets/4908dcee-5ee5-433f-a4fd-9869d1f904dd" />
</details>

### Contact

Users can contact through the contact page to submit any queries. After filling in the form, if valid, the user recieves a confirmation message.

<details>
<summary>Contact Form</summary>
<img width="1900" height="851" alt="Contact Form" src="https://github.com/user-attachments/assets/43760956-101c-4d36-bfc7-8be1dc6b98b8" />
</details>

<details>
<summary>Contact Success Message</summary>
<img width="1897" height="871" alt="Contact Success Message" src="https://github.com/user-attachments/assets/e50438a9-d8b2-457c-8f94-d0ad27c81125" />
</details>

## Built With



## Deployment



## Testing and Validation

I thoroughly tested the website through manual and automated testing as well as external testing and validation.

### External Testing and Validation

#### Lighthouse

I ran lighthouse tests for all pages of the live site. Here are the results:

<details>
<summary>Home Page (Desktop)</summary>
<img width="1276" height="696" alt="Home Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/7a61ee8d-45a5-4087-be75-f01ee9a3866f" />
</details>

<details>
<summary>Home Page (Mobile)</summary>
<img width="1280" height="546" alt="Home Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/2dd123fa-22b0-4ad1-aa32-de7f959675f4" />
</details>

<details>
<summary>Add Resource Page (Desktop)</summary>
<img width="1276" height="543" alt="Add Resource Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/c1ac0692-4549-4e29-a3ae-976d9b15d52b" />
</details>

<details>
<summary>Add Resource Page (Mobile)</summary>
<img width="1277" height="544" alt="Add Resource Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/7178a950-caa5-48cd-84fe-d02bb36c6cdd" />
</details>

<details>
<summary>Category Detail Page (Desktop)</summary>
<img width="1276" height="535" alt="Category Detail Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/a50fb950-436d-4fb2-8458-e2f17f088fe5" />
</details>

<details>
<summary>Category Detail Page (Mobile)</summary>
<img width="1278" height="544" alt="Category Detail Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/c48c8527-7e5d-41b9-b232-3cf62433dd8d" />
</details>

<details>
<summary>Favourites Page (Desktop)</summary>
<img width="1275" height="696" alt="Favourites Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/7c622763-c903-4a83-8154-311a7fca600d" />
</details>

<details>
<summary>Favourites Page (Mobile)</summary>
<img width="1278" height="699" alt="Favourites Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/f4a95a79-f6d0-4ad2-8105-a78d5d052c34" />
</details>

<details>
<summary>Search Page (Desktop)</summary>
<img width="1277" height="533" alt="Search Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/2f049609-1634-4d0b-994f-cf6e887796cb" />
</details>

<details>
<summary>Search Page (Mobile)</summary>
<img width="1273" height="541" alt="Search Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/4429ba4b-cefa-4163-be74-c5b5049ee5f6" />
</details>

<details>
<summary>Suggest Category Page (Desktop)</summary>
<img width="1274" height="540" alt="Suggest Category Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/26a8b2b0-700a-4886-8777-2874f871d7ea" />
</details>

<details>
<summary>Suggest Category Page (Mobile)</summary>
<img width="1275" height="534" alt="Suggest Category Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/1d9f1645-9d73-4dc5-b924-3ce5ba4a4b6f" />
</details>

<details>
<summary>Contact Page (Desktop)</summary>
<img width="1277" height="540" alt="Contact Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/75814a52-d2d8-4335-8c3f-79dc72f31d0a" />
</details>

<details>
<summary>Contact Page (Mobile)</summary>
<img width="1273" height="524" alt="Contact Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/c38c0f84-ef06-42f7-81a5-e6bd9bf9c70a" />
</details>

<details>
<summary>Register Page (Desktop)</summary>
<img width="1275" height="534" alt="Register Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/742f1dbd-9c7c-4b30-b811-dfb7afae1636" />
</details>

<details>
<summary>Register Page (Mobile)</summary>
<img width="1277" height="533" alt="Register Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/4ede1751-c466-4f7b-b6bb-4a79c30a623d" />
</details>

<details>
<summary>Login Page (Desktop)</summary>
<img width="1273" height="522" alt="Login Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/bf102f37-58f5-499e-8226-75d1dd601c0d" />
</details>

<details>
<summary>Login Page (Mobile)</summary>
<img width="1279" height="537" alt="Login Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/b8db18a4-cbd8-43e5-bbca-ec82f1c29c6c" />
</details>

<details>
<summary>Logout Page (Desktop)</summary>
<img width="1275" height="535" alt="Logout Page Lighthouse Report (Desktop)" src="https://github.com/user-attachments/assets/c5949c2a-42f7-4b67-96bb-c030c1f92b75" />
</details>

<details>
<summary>Logout Page (Mobile)</summary>
<img width="1275" height="532" alt="Logout Page Lighthouse Report (Mobile)" src="https://github.com/user-attachments/assets/fbba69fb-e7b7-4f30-b407-8fbca145b18f" />
</details>

#### HTML

I used the [W3C HTML Validator](https://validator.w3.org/) to validate the HTML templates. Here are the results:

<details>
<summary>Home Page</summary>
<img width="1899" height="793" alt="Home Page Validation" src="https://github.com/user-attachments/assets/21a5dfdb-6c2a-498c-a1d6-3324229b1ecf" />
</details>

<details>
<summary>Category Detail Page</summary>
<img width="1885" height="787" alt="Category Detail Page Validation" src="https://github.com/user-attachments/assets/b761cc8d-1a5b-4386-9268-33ada31c648c" />
</details>

<details>
<summary>Add Resource Page</summary>
<img width="1897" height="783" alt="Add Resource Page Validation" src="https://github.com/user-attachments/assets/f494d119-97b1-4ff4-a28e-d3ad0ef43195" />
</details>

<details>
<summary>Favourites Page</summary>
<img width="1901" height="789" alt="Favourites Page Validation" src="https://github.com/user-attachments/assets/316352b0-2062-434c-ba25-850b77c088a4" />
</details>

<details>
<summary>Search Page</summary>
<img width="1887" height="786" alt="Search Page Validation" src="https://github.com/user-attachments/assets/e9359e06-36a1-47c9-a0fb-6138bdd14a19" />
</details>

<details>
<summary>Suggest Category Page</summary>
<img width="1889" height="785" alt="Suggest Category Page Validation" src="https://github.com/user-attachments/assets/3ef85deb-2b30-4d46-a510-901f1c4ba8fc" />
</details>

<details>
<summary>Contact Page</summary>
<img width="1887" height="782" alt="Contact Page Validation" src="https://github.com/user-attachments/assets/8459ec55-bc98-4450-9393-ef6b68196bfc" />
</details>

<details>
<summary>Login Page</summary>
<img width="1900" height="787" alt="Login Page Validation" src="https://github.com/user-attachments/assets/e27f576d-80e1-4cd2-b757-d8d373af896b" />
</details>

<details>
<summary>Register Page</summary>
The errors on this page are due to django-allauth
<img width="1901" height="867" alt="Register Page Validation" src="https://github.com/user-attachments/assets/05283266-90f4-4b59-a403-4a22eb029a22" />
</details>

<details>
<summary>Logout Page</summary>
<img width="1891" height="785" alt="Logout Page Validation" src="https://github.com/user-attachments/assets/abd9f664-1b32-4b50-84ce-de68d8e1a097" />
</details>

#### CSS

I used the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my CSS. Here are the results:

<details>
<summary>CSS Validation</summary>
<img width="1881" height="686" alt="CSS Validation" src="https://github.com/user-attachments/assets/6f64a657-f852-4b40-a6ae-6f7378e72af5" />

The warnings in the CSS are due to CSS variables and prefixes for browser compatibility

<img width="1879" height="855" alt="CSS Validation Warnings" src="https://github.com/user-attachments/assets/e2ccb120-bac4-45e5-ba18-2de009e08e5a" />
</details>

## AI Implementation

I used AI tools such as Copilot throught the creation of the project. The support of AI helped greatly and sped up the development process. Here are  some ways I used AI to help with the project:

### User Stories

AI helped refine user stories and write acceptance criteria and tasks. I used Copilot to help me with this and then modified them to suit the project as some were not relevant. By doing so, it saved me time and helped with giving me ideas for features.

### Development

AI helped speed up development significantly. I used Copilot to help with repetitive tasks and commenting. It greatly helped me create view functionality, I adjusted what Copilot generated to fit the project. If it generated something I was unsure of, I asked it to explain the code and add comments. It also helped with adding docstrings and formating files according to PEP8 standards.

### Debugging

AI helped debug issues I had in my code such as warnings and unintended behaviour. Copilot walked me through the problems and gave solutions which I applied after making minor adjustments. It helped me understand the issues and effectively troubleshoot them.

### Unit Testing

AI helped generate unit tests for the project. It specified different edge cases and created tests to ensure functionality was as expected. I manually updated the tests to ensure they would run without errors, and asked Copilot to fix some bugs in the tests. In the end, all the tests were successful. AI sped up the process of creating unit tests and identifying edge cases.

### Reflection

AI greatly helped me create the project. I have learned the vast benefits of AI through this project, however, there are limitaions to it. There were times where it generated code unsuitable for the project or code with bugs. Therefore, it is always essential to review and understand all code produced by AI. I have made an effort to use AI only to assist me and not to do all the work. Despite the drawbacks and difficulties, AI supported the completion of the project.

## Credits
