

require 'debugger'              # optional, may be helpful
require 'open-uri'              # allows open('http://...') to return body
require 'cgi'                   # for escaping URIs
require 'nokogiri'              # XML parser
require 'active_model'          # for validations

class OracleOfBacon

  class InvalidError < RuntimeError ; end
  class NetworkError < RuntimeError ; end
  class InvalidKeyError < RuntimeError ; end

  attr_accessor :from, :to
  attr_reader :api_key, :response, :uri
  
  include ActiveModel::Validations
  validates_presence_of :from
  validates_presence_of :to
  validates_presence_of :api_key
  validate :from_does_not_equal_to

  def from_does_not_equal_to
    # YOUR CODE HERE
    return ( @from != @to )
  end

  def initialize(api_key='')
    # your code here
    @api_key = api_key
    @from    = 'Kevin Bacon'
    @to      = 'Kevin Bacon'
  end

  def find_connections
    if ( !make_uri_from_arguments )
        @response = nil
	return false
    end
    puts "Generated URI is: \"#{uri}\""
    begin
      xml = URI.parse(uri).read
    # Timeout::Error, 
    rescue Errno::EINVAL, Errno::ECONNRESET, EOFError,
      Net::HTTPBadResponse, Net::HTTPHeaderSyntaxError,
      Net::ProtocolError => e
      # convert all of these into a generic OracleOfBacon::NetworkError,
      #  but keep the original error message
      # your code here
      raise NetworkError e
    end
    # your code here: create the OracleOfBacon::Response object
    # extract data from 'xml' variable
    @response = Response.new( xml )
  end

  def make_uri_from_arguments
    # your code here: set the @uri attribute to properly-escaped URI
    #   constructed from the @from, @to, @api_key arguments
    # http://oracleofbacon.org/cgi-bin/xml?p=my_key&a=Kevin+Bacon&b=Laurence+Olivier
    if ( !from_does_equal_to )
        return false
    end
    @to ||= "Kevin Bacon"
    @uri = %Q{http://oracleofbacon.org/cgi-bin/xml?p=#{@api_key}&a=#{@from}&b=#{@to}}
    @uri = @uri.gsub( ' ', '+' )
    return true
  end
      
  class Response
    attr_reader :type, :data
    # create a Response object from a string of XML markup.
    def initialize(xml)
      @doc = Nokogiri::XML(xml)
      parse_response
    end

    private

    def parse_response
      if ! @doc.xpath('/error').empty?
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
          @data << actors[0].text
          movies.each do |m|
            @data << m.text
          end
          @data << actors[1].text
        elsif !spellcheck.empty?
          @type = :spellcheck
          arr = @doc.xpath( '//match' )
          @data = []
          arr.each do |a|
            @data << a.text
          end
        end
      end
    end
    
    def parse_error_response
      @type = :error
      @data = 'Unauthorized access'
    end
    
  end
end




