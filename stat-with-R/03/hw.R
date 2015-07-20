setwd( '~/projects/hw.git/stat-with-R/03' )

cv <- function( data )
{
  return( sd(data)/mean(data)*100.0 )
}

set.seed(200)
instrument1 <- round(rnorm(20,6,0.5),3)
instrument2 <- round(rnorm(20,6,2),3)
comparemethods <- cbind(instrument1, instrument2); boxplot(comparemethods)
cv(instrument1)
cv(instrument2)

baPlot <- function( fname )
{
    baData <- read.csv( fname, header=T )
    m <- (baData$Wright + baData$Mini)/2.0
    d <- (baData$Wright - baData$Mini)
    plot( m, d )
    md<- mean( d )
    abline( a=md, b=0.0 )
    sdd <- sd( d )
    abline( a=md+2*sdd, b=0.0 )
    abline( a=md-2*sdd, b=0.0 )
}

baPlot( "./BlandAltman.csv" )
