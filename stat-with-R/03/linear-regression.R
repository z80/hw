setwd( '~/projects/hw.git/stat-with-R/03' )

set.seed(278)
x <- rnorm(25, mean=100, sd=10)
y <- 2 * x + 20 + rnorm(25, mean=10, sd=4)

plot(x,y)  #Do you think a linear model would fit?
cor(x,y)  #If you just want the correlation coefficient
cor(x,y)^2 #Or the coefficient of determination
lm.obj <- lm(y~x) # See how models are described in R. y depends on x
abline(lm.obj)    #We can add the regression line to the scatterplot
predict(lm.obj) #The predicted y-values for your x-values
points(x,predict(lm.obj), col="green") #Add predicted values to the graph
summary(lm.obj)   #Lets look at the content of lm.obj
str(lm.obj)     #You can retrieve parts of the lm object
lm.obj$coefficients  #You may want to collect the coefficients
par(mfrow=c(2,2)) #prepare for a 2x2 layout
plot(lm.obj) #The built in controls for your regression analysis
par(mfrow=c(1,1)) #Restore 1x1 layout

x1 <- 1:100
y1 <- x1^2
