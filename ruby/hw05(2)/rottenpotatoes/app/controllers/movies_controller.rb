
#~ require 'debug'


class MoviesController < ApplicationController

  def show
    @movie = Movie.find(id) # look up movie by unique ID
    # will render app/views/movies/show.<extension> by default
  end

  def index
    #~ a = Movie.select( "rating" ).distinct.all
    a = Movie.find( :all, :select=>"DISTINCT movies.rating", :order=>"movies.rating" )
    @all_ratings = []
    a.each do |r|
      @all_ratings << r.rating
    end
    puts "_____________________"
    puts params
    puts a
    puts @all_ratings
    sort = params[ "order" ] # retrieve movie ID from URI route
    puts sort
    puts "_____________________"
    
    ratings = params["ratings"]
    if !ratings
      ratings = @all_ratings
    else
      ratings = ratings.keys
    end
    if ( sort == "name" )
      @movies = Movie.order( "title ASC" )
    elsif ( sort == "date" )
      @movies = Movie.order( "release_date ASC" )
    else
      #debug
      @movies = Movie
    end
    @movies = @movies.find_all_by_rating( ratings )
    
    @last_sort = sort
    @last_ratings = ratings
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
