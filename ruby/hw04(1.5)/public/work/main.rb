

require_relative '../lib/oracle_of_bacon.rb'
require 'nokogiri'

a = '38b' + '99c' + 'e9' + 'ec87'



10.times do
   puts ""
end


oob = OracleOfBacon.new( a )

# connect Laurence Olivier to Kevin Bacon
oob.from = 'Laurence Olivier'
puts "find_connections output: "
puts oob.find_connections

puts "response.type: "
puts oob.response.type      # => :graph

puts "response.data: "
puts oob.response.data      # => ['Kevin Bacon', 'The Big Picture (1989)', 'Eddie Albert (I)', 'Carrie (1952)', 'Laurence Olivier']


puts ""
puts ""
puts ""
puts "Secoond test: "

# #connect Carrie Fisher to Ian McKellen
oob.from = 'Carrie Fisher'
oob.to = 'Ian McKellen'
puts "find_connections output: "
puts oob.find_connections

puts "response.data: "
puts oob.response.data      # => ['Ian McKellen', 'Doogal (2006)', ...etc]



puts ""
puts ""
puts ""
puts "Third test: "

# #with multiple matches
oob.to = 'Anthony Perkins'
puts "find_connections output"
oob.find_connections

puts "response.type: "
puts oob.response.type      # => :spellcheck

puts "response.data: "
puts oob.response.data      # => ['Anthony Perkins (I)', ...33 more variations of the name]



puts ""
puts ""
puts ""
puts "Fourth test: "

#with bad key
oob = OracleOfBacon.new('known_bad_key')
puts "find_connections output: "
oob.find_connections
puts "response.type: "
puts oob.response.type      # => :error
puts "response.data: "
puts oob.response.data      # => 'Unauthorized access'






