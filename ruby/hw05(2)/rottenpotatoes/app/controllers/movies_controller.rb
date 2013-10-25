
#~ require 'debug'


class MoviesController < ApplicationController

  def show
    @movie = Movie.find(id) # look up movie by unique ID
    # will render app/views/movies/show.<extension> by default
  end

  def index
    puts "_____________________"
    puts params
    sort = params[ "order" ] # retrieve movie ID from URI route
    puts sort
    puts "_____________________"
    if ( sort == "name" )
      @movies = Movie.order( "title ASC" ).all
    elsif ( sort == "date" )
      @movies = Movie.order( "release_date ASC" ).all
    else
      #debug
      @movies = Movie.all
    end
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
