# Add a declarative step here for populating the DB with movies.

m = Movie.new()
m.title = "Alladin"
m.rating = "G"
m.release_date = DateTime.parse("25-Nov-1992")
m.save()

m = Movie.new()
m.title = "The Terminator"
m.rating = "R"
m.release_date = DateTime.parse("26-Oct-1984")
m.save

m = Movie.new()
m.title = "When Harry Met Sally"
m.rating = "R"
m.release_date = DateTime.parse("21-Jul-1989")
m.save

m = Movie.new()
m.title = "The Help"
m.rating = "PG-13"
m.release_date = DateTime.parse("10-Aug-2011")
m.save

m = Movie.new()
m.title = "Chocolat"
m.rating = "PG-13"
m_release_date = DateTime.parse("5-Jan-2001")
m.save

m = Movie.new
m.title = "Amelie"
m.rating = "R"
m.release_date = DateTime.parse("25-Apr-2001")
m.save

m = Movie.new
m.title = "2001: A Space Odyssey"
m.rating = "G"
m.release_date = DateTime.parse("6-Apr-1968")
m.save

m = Movie.new
m.title = "The Incredibles"
m.rating = "PG"
m.release_date = DateTime.parse("5-Nov-2004")
m.save

m = Movie.new
m.title = "Raiders of the Lost Ark"
m.rating = "PG"
m.release_date = DateTime.parse("12-Jun-1981")
m.save

m = Movie.new
m.title = "Chicken Run"
m.rating = "G"
m.release_date = DateTime.parse("21-Jun-2000")
m.save



Given /the following movies exist/ do |movies_table|
  #puts "________________________________________"
  #puts movies_table
  #puts "________________________________________"
  movies_table.hashes.each do |movie|
    # each returned element will be a hash whose key is the table header.
    # you should arrange to add that movie to the database here.
  end
  #flunk "Unimplemented"
end

# Make sure that one string (regexp) occurs before or after another one
#   on the same page

Then /I should see "(.*)" before "(.*)"/ do |e1, e2|
  #  ensure that that e1 occurs before e2.
  #  page.body is the entire content of the page as a string.
  flunk "Unimplemented"
end

# Make it easier to express checking or unchecking several boxes at once
#  "When I uncheck the following ratings: PG, G, R"
#  "When I check the following ratings: G"

When /I (un)?check the following ratings: (.*)/ do |uncheck, rating_list|
  # HINT: use String#split to split up the rating_list, then
  #   iterate over the ratings and reuse the "When I check..." or
  #   "When I uncheck..." steps in lines 89-95 of web_steps.rb
end

Then /I should see all the movies/ do
  # Make sure that all the movies in the app are visible in the table
end
