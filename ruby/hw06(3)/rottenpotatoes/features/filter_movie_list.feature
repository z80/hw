Feature: display list of movies filtered by MPAA rating
 
  As a concerned parent
  So that I can quickly browse movies appropriate for my family
  I want to see movies matching only certain MPAA ratings

Background: movies have been added to database

  Given the following movies exist:
  | title                   | rating | release_date |
  | Aladdin                 | G      | 25-Nov-1992  |
  | The Terminator          | R      | 26-Oct-1984  |
  | When Harry Met Sally    | R      | 21-Jul-1989  |
  | The Help                | PG-13  | 10-Aug-2011  |
  | Chocolat                | PG-13  | 5-Jan-2001   |
  | Amelie                  | R      | 25-Apr-2001  |
  | 2001: A Space Odyssey   | G      | 6-Apr-1968   |
  | The Incredibles         | PG     | 5-Nov-2004   |
  | Raiders of the Lost Ark | PG     | 12-Jun-1981  |
  | Chicken Run             | G      | 21-Jun-2000  |

  And  I am on the RottenPotatoes home page

Scenario: restrict to movies with 'PG' or 'R' ratings
  #Given I am on /movies
  # enter step(s) to check the 'PG' and 'R' checkboxes
  When I check the following ratings: PG, R
  # enter step(s) to uncheck all other checkboxes
  And I uncheck the following ratings: G, PG-13
  # enter step to "submit" the search form on the homepage
  When I press 'submit'
  # enter step(s) to ensure that PG and R movies are visible
  Then movies with ratings PG and R are visible
  # enter step(s) to ensure that other movies are not visible
  And movies with other ratings are not visible

Scenario: all ratings selected
  # see assignment
  Given all ratings are selected
  When I click 'submit' search from the homepage
  Then I should see all the movies in movie_steps.rb


Scenario: movies are sorted alphabetically
    Given I visit movie page
    And I select all ratings
    And I press 'submit'
    When I click sort by name
    Then I should see movies sorted alphabetically

Scenario: movies are sorted by date
    Given I visit movie page
    And I select all ratings
    And I press 'submit'
    When I click sort by date
    Then I should see movies sorted by release date



