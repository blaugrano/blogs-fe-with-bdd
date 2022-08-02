Feature: Test navigation between pages
  Scenario: Homepage can go to Blog
    Given I am on the home page
    When I click on "Go to blog" link
    Then I am on the blog page