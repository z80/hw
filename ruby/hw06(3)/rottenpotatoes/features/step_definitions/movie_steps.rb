
#require 'debug'

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
  visit( '/movies' )
  #puts rating_list
  #puts Capybara.page.body
  ratings = rating_list.split(%r{,\s*})
  if uncheck
    ratings.each do |r|
      step "I uncheck \"ratings_#{r}\""
    end
  else
    ratings.each do |r|
      puts r
      step "I check \"ratings_#{r}\""
    end
  end  
end

Then /I should see all the movies/ do
  # Make sure that all the movies in the app are visible in the table
  a = Movie.all
  cnt = 0
  a.each do
     cnt += 1
  end
  rows = page.body.downcase.scan( "<tr>" ).size - 1
  puts cnt
  puts rows
  cnt.should == rows
end






When /I press 'submit'/ do
    click_button( 'ratings_submit' )
end

Then /movies with ratings PG and R are visible/ do
    a = Movie.find_all_by_rating( "PG" )
    a.each do |movie|
        page.should have_content( movie.title )
    end
    a = Movie.find_all_by_rating( "R" )
    a.each do |movie|
        page.should have_content( movie.title )
    end
end

And /movies with other ratings are not visible/ do
    a = Movie.all
    a.each do |movie|
        if ( movie.rating != "PG" ) && ( movie.rating != "R" )
          page.should_not have_content( movie.title )
	end
    end
end

Given /all ratings are selected/ do
  visit( '/movies' )
  ratings = Movie.find( :all, :select=>"DISTINCT movies.rating", :order=>"movies.rating" )
  #puts ratings

  ratings.each do |m|
    step "I check \"ratings_#{m.rating}\""
  end
end

When /I click 'submit' search from the homepage/ do
  click_button( 'ratings_submit' )
end

#Then /I should see all the movies in movie_steps.rb/ do

#end



