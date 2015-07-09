setwd( 'C:/projects/hw.git/stat-with-R/01' )
unmet <- read.csv( "data_unmetneed1_1.csv" )
str( unmet )
unmet$edu <- as.factor(unmet$edu)
education.levels <-c("not literate","literate without formal schooling",                     "literate but below primary","primary","upper primary",                     "secondary","intermediate","diploma/certificate course", "graduate","postgraduate and above")
levels(unmet$edu) <- education.levels
barplot(sort(table(unmet$edu)), las=2)
head( unmet$edu )
head( education.levels )
unmet$edu = education.levels[ unmet$edu ]
barplot(sort(table(unmet$edu)), las=2)