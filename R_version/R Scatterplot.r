#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

data <- read.csv(args[1])

x <- data$x
y <- data$y

png('r_orig.png')
plot(x, y, main = "Scatter in R")

png('r_lm.png')
plot(x, y, main = "Scatter in R with regression")
abline(lm(y ~ x))



