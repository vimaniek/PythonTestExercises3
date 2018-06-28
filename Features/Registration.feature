# Created by Mariusz at 6/25/2018
Feature: Registration
  Check if registration form is working properly, by filling in the form with warious data:

  Here should be better explanation of requirements for registration form

  Background:
    Given Go to a registration form by clicking on registration button on the home page.

  @NewOne
  Scenario Outline: Fill in form with given data
    Given Fill fields with <givenDataNumber> set of data
      | first_name | last_name    | phone_number | username | email              | about_yourself             | password     | confirm_password | annotation                      |
      | Mariuszek  | Nazarkiewicz | 66666666666  | barabasz | zielonka@gmail.com | tekscik                    | haselko@#$88 | haselko@#$88     | Error: Username already exists  |
      | ziomal     | ziomalczyk   | 55566655566  | barabara | karczoch@gmail.com | what do you expect to read | haselko@#$88 | haselko@#$88     | Thank you for your registration |

    When Fill "first_name" field with given data
    And Fill "last_name" field with given data
    And Select martial status
    And Select chosen hobbies
    And Select country
    And Select date of birth
    And Fill "phone_number" field with given data
    And Fill "username" field with given data
    And Fill "email" field with given data
    And Upload profile picture
    And Fill "about_yourself" field with given data
    And Fill "password" field with given data
    And Fill "confirm_password" field with given data
    And Click the "Submit" button

    Then "annotation" will appear

    Examples:
      | givenDataNumber |
      | 0               |
      | 1               |