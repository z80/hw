

require 'debugger'              # optional, may be helpful
require 'open-uri'              # allows open('http://...') to return body
require 'cgi'                   # for escaping URIs
require 'nokogiri'              # XML parser
require 'active_model'          # for validations

class OracleOfBacon

  class InvalidError < RuntimeError ; end
  class NetworkError < RuntimeError ; end
  class InvalidKeyError < RuntimeError ; end

  #attr_accessor :from, :to
  def from
      return @from
  end
  def from=( arg )
    @from = arg
    @to ||= 'Kevin Bacon'
  end
  def to
    return @to
  end
  def to=( arg )
    @to = arg
    @from ||= 'Kevin Bacon'
  end

  attr_reader :api_key, :response, :uri
  
  include ActiveModel::Validations
  #validates_presence_of :from
  #validates_presence_of :to
  #validates_presence_of :api_key
  #validate :from_does_not_equal_to
  def valid?
    if ( !@from )
        return false
    end
    if ( !@to )
      return false
    end
    if ( !@api_key )
      return false
    end
    if ( !from_does_not_equal_to )
      return false
    end
    return true
  end

  def from_does_not_equal_to
    # YOUR CODE HERE
    return ( @from != @to )
  end

  def initialize(api_key='')
    # your code here
    @api_key = api_key
  end

  def find_connections
    puts "HERE 1"
    #if ( !make_uri_from_arguments )
    #    puts "HERE 2"
    #    #@response = Response.new( "<error></error>" )
    #     return false
    #end
    make_uri_from_arguments
    #puts "Generated URI is: \"#{@uri}\""
    begin
      xml = URI.parse( @uri ).read
      #puts "++++++++++++++++++"
      #puts xml
      #puts "++++++++++++++++++"
    # Timeout::Error, 
    rescue Errno::EINVAL, Errno::ECONNRESET, EOFError,
      Net::HTTPBadResponse, Net::HTTPHeaderSyntaxError,
      Net::ProtocolError, Timeout::Error => e

      # convert all of these into a generic OracleOfBacon::NetworkError,
      #  but keep the original error message
      # your code here
      #@response = Response.new( "<error></error>" )
      raise NetworkError, e
    end
    # your code here: create the OracleOfBacon::Response object
    # extract data from 'xml' variable
    @response = Response.new( xml )
  end

  def make_uri_from_arguments
    # your code here: set the @uri attribute to properly-escaped URI
    #   constructed from the @from, @to, @api_key arguments
    # http://oracleofbacon.org/cgi-bin/xml?p=my_key&a=Kevin+Bacon&b=Laurence+Olivier
    p = CGI.escape( @api_key )
    a = CGI.escape( @from.to_s )
    b = CGI.escape( @to.to_s )
    @uri = %Q{http://oracleofbacon.org/cgi-bin/xml?p=#{p}&a=#{a}&b=#{b}}
    if ( !from_does_not_equal_to )
        return false
    end
    return true
  end
      
  class Response
    attr_reader :type, :data
    # create a Response object from a string of XML markup.
    def initialize(xml)
      #puts "________________________________________"
      #puts xml
      #puts "________________________________________"
      @doc = Nokogiri::XML(xml)
      parse_response
    end

    private

    def parse_response
      @type = :error
      @data = 'Unauthorized access'

      if ! @doc.xpath('//error').empty?
        parse_error_response
      # your code here: 'elsif' clauses to handle other responses
      # for responses not matching the 3 basic types, the Response
      # object should have type 'unknown' and data 'unknown response'         
      else
        actors = @doc.xpath('//actor')
        movies = @doc.xpath('//movie')
        spellcheck = @doc.xpath('//spellcheck')
        if !actors.empty? && !movies.empty?
          @type = :graph
          @data = []
          movies.each do |m|
            @data << m.text
          end
          aa = []
	  actors.each do |a|
	     aa << a.text
	  end
	  aa = aa.zip( @data )
	  @data = aa.flatten()
	  @data = @data.delete_if { |a| a == nil }
        elsif !spellcheck.empty?
          @type = :spellcheck
          arr = @doc.xpath( '//match' )
          @data = []
          arr.each do |a|
            @data << a.text
          end
	else
	  @type = :unknown
	  @data = "unknown" #@doc.xpath( "/other" ).attribute( "name" )
        end
      end
    end
    
    def parse_error_response
      @type = :error
      @data = 'Unauthorized access'
    end
    
  end
end




