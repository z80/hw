

class BookInStock
  def initialize( isbn, price )
    if ( ( !isbn ) || 
         ( isbn.length < 1 ) || 
         ( isbn == "" ) || 
         ( !price ) || 
         ( price <= 0 ) )
      raise ArgumentError
    end
    @isbn  = isbn
    @price = price
  end

  def isbn()
    return @isbn
  end

  def isbn=( arg )
    @isbn = arg
  end

  def price()
    return @price
  end

  def price=( arg )
    @price = arg
  end

  def price_as_string()
    return "$%3.2f" % [ @price ]
  end
end

# Tests:
a = BookInStock.new( "a", 10 )
a.price = 123
a.isbn = "321"
puts a.price
puts a.isbn
puts a.price_as_string
