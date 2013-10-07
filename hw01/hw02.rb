
def hello( name )
  return "Hello, " + name
end

def starts_with_consonant?( s )
  if (s.length < 1)
    return false
  end
  res = s.match( /^[^AEIOU].+$/i )
  if ( !res )
    return false
  end
  if ( res.size() > 0 )
      return true
  end
  return false
end

def binary_multiple_of_4?( s )
  res = s.match( /[01]*/ )
  if ( !res )
    return false
  end
  # Should ensure there are ones in the number.
  res = s.match( /1/ )
  if ( !res )
    return false
  end
  # If it is divided by 4 least two digits are zeros.
  res = s.match( /^[01]+00$/ )
  if ( !res )
    return false
  end
  if ( res.size() > 0 )
    return true
  end
  return false
end



# tests ....
#puts "Tests: "
#puts hello( "dasda" )
#puts "Consonant test: "
#puts starts_with_consonant?( "bBfds" )
#puts "binary multiple of 4 test: "
#puts binary_multiple_of_4?( "0000" )

