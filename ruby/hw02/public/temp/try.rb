module FunWithStrings
  def palindrome?
    # your code here
    stri = self
    stri = stri.gsub( /\W/i, "" ).downcase
    invStri = stri.reverse
    return (stri == invStri)
  end
  
  def count_words
    # your code here
    stri = self
    h = Hash.new( 0 )
    stri.split( /\W+/i ).each do |word|
      h[ word ] += 1
    end
    return h
  end
  
    def anagram_groups
        # your code here
        strings = self
        res = Array.new()
        involved = Array.new()
        strings.each do |s|
            involved << false
        end
        
        strings.each_index do | i |
            if ( ( !involved[i] ) && (strings[i].length > 0) )
                s1 = strings[i]
                res << [ s1 ]
                index = res.length - 1
                involved[ i ] = true
                sa = s1.downcase
                strings.each_index do | j |
                    if ( ( j > i ) && ( !involved[j] ) )
                        s2 = strings[j]
                        # Check strings to be anagrams
                        match = true
                        if ( s1.length == s2.length )
                            sb = s2.downcase
                            sa.each_char do |ch|
                                t1 = sa.gsub( ch, "" )
                                t2 = sb.gsub( ch, "" )
                                if ( t1.length != t2.length )
                                    match = false
                                    break
                                end
                            end
                        else
                            match = false
                        end
                        if ( match )
                            res[index] << s2
                            involved[ j ] = true
                        end
                    end
                end
            end
        end
        
        return res
    end
end
# make all the above functions available as instance methods on Strings:

class String
  include FunWithStrings
end

class Array
    include FunWithStrings
end

res = [ "aa", "aa", "bb", "asda", "Me", "Aa", "Em" ].anagram_groups
puts res.length
res.each do |a|
    puts "output "
    a.each do |s|
        puts s
    end
end
puts "--------------"
res = [].anagram_groups
puts res.length
puts "--------------"
res = "scream cars for four scar creams".anagram_groups
res.each do |a|
    puts "output "
    a.each do |s|
        puts s
    end
end

