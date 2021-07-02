data <- read.csv(args[1])

x <- data$x
y <- data$y



plot(x, y, main = "Scatter in R")
png('r_orig.png')

plot(x, y, main = "Scatter in R with regression")
abline(lm(y ~ x))
png('r_lm.png')


