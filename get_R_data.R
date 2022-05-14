library(Ecdat)
library(car)
library(tidyverse)

data <- Clothing

View(data)

write.csv(data,'/Users/benja/OneDrive/Documents/School/Spring 2022/Linear-Regression/data/Clothing.csv')

mylm = lm('tsales ~ hourspw',data)
summary(mylm)

cint(mylm)
