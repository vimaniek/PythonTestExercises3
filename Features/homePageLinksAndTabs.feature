# Created by Mariusz at 6/20/2018
Feature: Home page links and tabs
  I need to be sure, that following features of a home page (http://demoqa.com/) work properly:

  1. Clicking on a pictures below "Unique & Clean", "Customer Support" and "Very Flexible"
  captions redirect to http://demoqa.com/wp-content/uploads/2014/08/pattern-14.png page.

  2. Clicking on each of a tabs from Tab 1 to Tab 5 show corresponding content from 1 to 5
  i.e. clicking on the Tab 1 results opening a sub-page which title is Content 1 Title.

  Background:
    Given I am on a http://demoqa.com/ page

  @Regression
  Scenario Outline: click on a picture below label
    When I click on a picture below <labelName> label
    Then I will be redirect to http://demoqa.com/wp-content/uploads/2014/08/pattern-14.png page

    Examples:
      | labelName          |
      | "Unique & Clean"   |
      | "Customer Support" |
      | "Very Flexible"    |

  @SmokeTest @BoomTest
  Scenario Outline:
    When I click on the "Tab <tabNumber>" button
    Then A sub-page opens with the title "<contentTitle>"

    Examples:
      | tabNumber | contentTitle    |
      | 1         | Content 1 Title |
      | 2         | Content 2 Title |
      | 3         | Content 3 Title |
      | 4         | Content 4 Title |
      | 5         | Content 5 Title |
