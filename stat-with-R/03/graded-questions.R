setwd( '~/projects/hw.git/stat-with-R/03' )

x <- 0:2
plot(x, dbinom(x, 2, 0.5), type = "h", col = "blue", lwd=4, ylim= c(0,0.6))
curve(dnorm(x, 1, 0.8), add=T)

x <- 0:8
p <- dbinom(x, 8, 0.5)
plot(x, dbinom(x, 8, 0.5), type = "h", col = "blue", lwd=4, ylim= c(0,0.6))
curve(dnorm(x, 4, 1.5), add=T)
p[3]

x <- 0:30
p <- dbinom(x, 30, 0.5)
plot(x, dbinom(x, 30, 0.5), type = "h", col = "blue", lwd=4, ylim= c(0,0.6))
curve(dnorm(x, 15, 2.8), add=T)

sqrt(30*0.5*(1-0.5))
sqrt(8*0.5*(1-0.5))
30*0.5*(1-0.5)

set.seed(400)
NORMAL <- rnorm(10000)
UNIFORM <- runif(10000)
SKEWED <- rep(1:140, 1:140)
opar <- par() #Save original par settings. Read ?par() if you like
par(mfrow= c(3,1)) #Ask for three columns and one row in the graph
hist(NORMAL)
hist(UNIFORM)
hist(SKEWED)
par(opar) #Reset the graph parameters
#Reset can also be achieved by closing the Graphics window

par(mfrow= c(3,1)) #Ask for three columns and one row in the graph
sampl <- vector() #Create an empty vector
for(i in 1:1000) #Start a loop with 1000 rounds
    sampl <- c(sampl, mean(sample(NORMAL, 3, replace=T)))
#fill sampl with sampl, and the mean of three random items from NORMAL
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 3 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(NORMAL, 6, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 6 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(NORMAL, 300, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 300 " )

par(mfrow= c(3,1)) #Ask for three columns and one row in the graph
sampl <- vector() #Create an empty vector
for(i in 1:1000) #Start a loop with 1000 rounds
    sampl <- c(sampl, mean(sample(UNIFORM, 3, replace=T)))
#fill sampl with sampl, and the mean of three random items from NORMAL
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 3 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(UNIFORM, 6, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 6 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(UNIFORM, 300, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 300 " )

par(mfrow= c(3,1)) #Ask for three columns and one row in the graph
sampl <- vector() #Create an empty vector
for(i in 1:1000) #Start a loop with 1000 rounds
    sampl <- c(sampl, mean(sample(SKEWED, 3, replace=T)))
#fill sampl with sampl, and the mean of three random items from NORMAL
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 3 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(SKEWED, 6, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 6 " )
sampl <- vector()
for(i in 1:1000)
    sampl <- c(sampl, mean(sample(SKEWED, 300, replace=T)))
mean(sampl)
sd(sampl)
hist(sampl, xlim = c(-2, 2), main = " n = 300 " )

sd(sampl)^2
sd(NORMAL)
sd(sampl)*sqrt(300)

x <- rnorm(100000)
y <- rnorm(100000)
z <- rep(NA, 100000) #z is created empty but with a given size.
system.time({
    for (i in 1:100000) {
        z[i] <- x[i] + y[i]
    }
})
system.time( k <- x + y )

set.seed(897)
ME <- matrix(rnorm(24000),nrow=1000)
colnames(ME) <- c(paste("A",1:12,sep=""),paste("B",1:12,sep=""))
length(which(ME<=0))
length(which(ME>=0))
keep <- (apply(ME[,1:12],1,mean) > 0) & (apply(ME[,13:24],1,mean) > 0)
length(keep)
head(keep)
trimmed <- apply(ME,1,function(ME){mean(ME, trim=0.05)})



