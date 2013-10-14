
module SpaceShip

    def <=>( b )
        a = self
        # Euqal strategy means first wins by definition.
        if ( a == b )
            return 1
        end
        if ( a == "r" )
            if ( b == "s" )
                return 1
            end
            if ( b == "p" )
                return -1
            end
        end
        if ( a == "s" )
            if ( b == "p" )
                return 1
            end
            if ( b == "r" )
                return -1
            end
        end
        if ( a == "p" )
            if ( b == "s" )
                return -1
            end
            if ( b == "r" )
                return 1
            end
            
        end
    
        return -1
    end

end

class String
    include SpaceShip
end

class RockPaperScissors

        # Exceptions this class can raise:
        class NoSuchStrategyError < StandardError ; end
    
        def self.winner(player1, player2)
            # YOUR CODE HERE
            s1 = player1[1].downcase
            s2 = player2[1].downcase
            if ( self.winner_index( s1, s2 ) == 0 )
                return player1
            end
            return player2
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
      
        def self.winner_index( s1, s2 )
            a = [ "r", "p", "s" ]
            i1 = a.index( s1 )
            if ( i1 == nil )
                puts s1
                raise NoSuchStrategyError
            end
            i2 = a.index( s2 )
            if ( i2 == nil )
                puts s2
                raise NoSuchStrategyError
            end
            if ( s1 >= s2 )
                return 0
            else
                return 1
            end
        end

end


puts RockPaperScissors.winner( [ "aaa", "p" ], [ "vvv", "s" ] )




