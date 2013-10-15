class Dessert
    def initialize(name, calories)
        # your code here
        @name    = name
        @calories = calories
    end
    
    def healthy?
        # your code here
        return ( @calories < 200 )
    end
    
    def delicious?
        # your code here
        true
    end
  
    def name
        return @name
    end
    def name=( stri )
        @name = stri
    end
    
    def calories
        return @calories
    end
    def calories=( val )
        @calories = val
    end
end

class JellyBean < Dessert
    def initialize(flavor)
        # your code here
        super( flavor + " jelly bean", 5 )
        @flavor = flavor
    end
    
    def flavor
        return @flavor
    end
    def flavor=( arg )
        @flavor = arg
        @name = flavor + " jelly bean"
    end
    
    def delicious?
        if ( @flavor == "licorice" )
            return false
        end
        return true
    end
    
end


