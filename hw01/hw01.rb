
# Sum of all array values
def sum( input )
    s = 0
    input.each do |i|
        s += i
    end
    return s
end

def max_2_sum( input )
    i = input.sort.reverse
    s = (i[0] ? i[0] : 0) + (i[1] ? i[1] : 0)
end

def sum_to_n?( input, n )
    if ( input.length < 1 )
        return ( n == 0)
    end
    if ( input.length < 2 )
        return ( n == 2 * input[0] )
    end
    for i in 0..(input.length-2)
        for j in (i+1)..(input.length-1)
            s = input[i] + input[j]
            if ( s == n )
                return true
            end
        end
    end
    return false
end

#if (__FILE__ == $0)
    # Just sum
    puts "sum check"
    puts sum( [ 1, 2, 3 ] )
    # Sum two largest values.
    puts "max_2_sum test"
    puts max_2_sum( [1, 2, 5, 8, 2, 9] )
    puts max_2_sum( [2] )
    # Sum_to_n? test
    puts "sum_to_n test"
    puts sum_to_n?( [ 1, 2, 3, 4, 5], 3 )
    puts sum_to_n?( [23], 46 )

    #[1, 2].each do |i|
    #    puts i
    #end
#end


