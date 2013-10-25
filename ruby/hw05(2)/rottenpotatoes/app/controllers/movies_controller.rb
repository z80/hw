
#~ require 'debug'


class MoviesController < ApplicationController

  def show
    @movie = Movie.find(id) # look up movie by unique ID
    # will render app/views/movies/show.<extension> by default
  end

  def index
    a = Movie.find( :all, :select=>"DISTINCT movies.rating", :order=>"movies.rating" )
    @all_ratings = []
    a.each do |r|
      @all_ratings << r.rating
    end

    ratings = params["ratings"] ? params["ratings"] :
                                ( flash[:ratings] ? flash[:ratings] : @all_ratings )
    flash[:ratings] = ratings
    ratings = ratings.keys

    order = params[ "order" ] ? params[ "order" ] :
                              ( flash[:order] ? flash[:order] : nil ) # retrieve movie ID from URI route
    flash[:order] = order

    if ( order == "name" )
      @movies = Movie.order( "title ASC" )
    elsif ( order == "date" )
      @movies = Movie.order( "release_date ASC" )
    else
      #debug
      @movies = Movie
    end
    @movies = @movies.find_all_by_rating( ratings )

    #default settings:
    #@def_sort = sort
    ratings = params["ratings"]
    puts "def_ratings before assigning: "
    puts @def_ratings
    @def_ratings = ratings ? ratings : flash[:ratings]


    puts "_____________________"
    puts "\"All params structure: \""
    puts params
    puts a
    puts "\"All ratings: \""
    puts @all_ratings
    puts '########'
    puts "\"Selected ratings: \""
    puts @def_ratings
    puts "_____________________"

  end

  def new
    # default: render 'new' template
  end

  def create
    @movie = Movie.create!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully created."
    redirect_to movies_path
  end

  def edit
    @movie = Movie.find params[:id]
  end

  def update
    @movie = Movie.find params[:id]
    @movie.update_attributes!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully updated."
    redirect_to movie_path(@movie)
  end

  def destroy
    @movie = Movie.find(params[:id])
    @movie.destroy
    flash[:notice] = "Movie '#{@movie.title}' deleted."
    redirect_to movies_path
  end

end
