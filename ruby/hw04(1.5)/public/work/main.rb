

require_relative './oracle_of_bacon.rb'
require 'nokogiri'

a = '38b' + '99c' + 'e9' + 'ec87'

oob = OracleOfBacon.new( a )

# connect Laurence Olivier to Kevin Bacon
oob.from = 'Laurence Olivier'
oob.find_connections
oob.response.type      # => :graph
oob.response.data      # => ['Kevin Bacon', 'The Big Picture (1989)', 'Eddie Albert (I)', 'Carrie (1952)', 'Laurence Olivier']


# #connect Carrie Fisher to Ian McKellen
# oob.from = 'Carrie Fisher'
# oob.to = 'Ian McKellen'
# oob.find_connections
# oob.response.data      => ['Ian McKellen', 'Doogal (2006)', ...etc]

# #with multiple matches
# oob.to = 'Anthony Perkins'
# oob.find_connections
# oob.response.type      => :spellcheck
# oob.response.data      => ['Anthony Perkins (I)', ...33 more variations of the name]
# #with bad key
# oob = OracleOfBacon.new('known_bad_key')
# oob.find_connections
# oob.response.type      => :error
# oob.response.data      => 'Unauthorized access'






