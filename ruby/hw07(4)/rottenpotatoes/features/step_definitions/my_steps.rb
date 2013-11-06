
Given(/^the following movies exist:$/) do |table|
  # table is a Cucumber::Ast::Table
  m = Movie.new
  m.title = "Star Wars"
  m.rating = "PG"
  m.director = "George Lucas"
  m.release_date = Date.parse( "1977-05-25" )
  m.save!

  m = Movie.new
  m.title = "Blade Runner"
  m.rating = "PG"
  m.director = "Ridley Scott"
  m.release_date = Date.parse( "1982-06-25" )
  m.save!

  m = Movie.new
  m.title = "Alien"
  m.rating = "R"
  m.release_date = Date.parse( "1979-05-25" )
  m.save!

  m = Movie.new
  m.title = "THX-1138"
  m.rating = "R"
  m.director = "George Lucas"
  m.release_date = Date.parse( "1971-03-11" )
  m.save!

  #pending # express the regexp above with the code you wish you had
end

When /I go to the edit page for \"Alien\"/ do
  visit "/movies"
  lnk = page.body.match( /a href=\"(.+)\">More about Alien<\/a/i )[1]
  puts "+++++++++++++++++++++++++"
  puts "Alien link is: "
  puts lnk
  puts "+++++++++++++++++++++++++"
  visit lnk
  lnk = page.body.match( /a href=\"(.+)\">Edit<\/a/i )[1]
  visit lnk
  puts page.body
end

And  /I fill in \"Director\" with \"Ridley Scott\"/ do

end

Then(/^the director of "(.*?)" should be "(.*?)"$/) do |arg1, arg2|
  pending # express the regexp above with the code you wish you had
end





