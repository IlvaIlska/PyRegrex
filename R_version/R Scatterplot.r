data <- read.csv("regrex1.csv")

x <- data$x
y <- data$y



plot(x, y, main = "Scatter in R")
abline(lm(y ~ x))
