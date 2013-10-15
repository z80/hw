

class RockPaperScissors

        # Exceptions this class can raise:
        class NoSuchStrategyError < StandardError ; end
    
        def self.winner(player1, player2)
            # YOUR CODE HERE
            s1 = player1[1].downcase
            s2 = player2[1].downcase

            # Check input values validity
            a = [ "r", "p", "s" ]
            i1 = a.index( s1 )
            if ( i1 == nil )
                #puts s1
                raise NoSuchStrategyError.new( "Strategy must be one of R,P,S" )
            end
            i2 = a.index( s2 )
            if ( i2 == nil )
                #puts s2
                raise NoSuchStrategyError.new( "Strategy must be one of R,P,S" )
            end

            if ( s1 == s2 )
                return player1
            end
            if ( s1 == "r" )
                if ( s2 == "s" )
                    return player1
                end
                if ( s2 == "p" )
                    return player2
                end
            end
            if ( s1 == "s" )
                if ( s2 == "r" )
                    return player2
                end
                if ( s2 == "p" )
                    return player1
                end
            end
            if ( s1 == "p" )
                if ( s2 == "r" )
                    return player1
                end
                if ( s2 == "s" )
                    return player2
                end
            end
        end

        def self.tournament_winner( tournament )
            # YOUR CODE HERE
            s1 = tournament[0]
            s2 = tournament[1]
            # check if both are final candidates.
            if ( ( s1[0].is_a? String ) && ( s2[0].is_a? String ) )
                return winner( s1, s2 )
            end
            # Else these are branches of tournament.
            # It's necessary to iterate the same function th them both 
            # And take a winner afterwards.
            s1 = tournament_winner( s1 )
            s2 = tournament_winner( s2 )
            return winner( s1, s2 )
        end
end

puts RockPaperScissors.winner( [ "first", "p" ], [ "second", "s" ] )
puts RockPaperScissors.winner( [ "first", "s" ], [ "second", "R" ] )
puts "tournament: "
puts RockPaperScissors.tournament_winner( [ [ "aaa", "p" ], [ "vvv", "s" ] ] )

puts "---------------"
RockPaperScissors.winner( ['Armando','R'], ['Dave', 'w'] )





