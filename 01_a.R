#' 01_a.R
#' Day 1: Calorie Counting
#' https://adventofcode.com/2022/day/1
#'
#' ========= SOLUTIONS ==========
#' + PART 1 ......65,912 calories
#' + PART 2 .....195,625 calories

packages <- c("tidyverse")
lapply(packages, require, character.only = T)

repo.local <- "~/repos/_misc/adventofcode"
puzzle.input <- "./data/01_input.txt"

setwd(repo.local)

# Define input and solvers ------------------------------------------------
get.cal.totals <- function(filepath) {
  calories <- readLines(filepath)
  n.vec <- length(calories)
  breaks <- which(grepl("^[[:space:]]*$", calories))
  n.breaks <- length(breaks)
  if (breaks[n.breaks] < n.vec) {
    breaks <- c(breaks, n.vec + 1L)
    n.breaks <- n.breaks + 1L
  }
  if (n.breaks > 0L) {
    calories <-
      mapply(function(i, j) {
        paste(calories[i:j], collapse = " ")
      },
      c(1L, 1L + breaks[-n.breaks]), breaks - 1L)
  }
  calories <-
    lapply(calories, function(x) {
      as.numeric(strsplit(x, split = " ")[[1]])
    })
  return (sapply(calories, sum))
}

get.max.cals <- function(total_calories) {
  return (max(unlist(total_calories)))
}

sum.top.n.max.cols <- function(total_calories, n = 3) {
  total_calories <- sort.int(total_calories)
  return(sum(total_calories[seq.int(to = length(total_calories),
                                    length.out = n)]))
}

# Driver ------------------------------------------------------------------
calories <- get.cal.totals(puzzle.input)
print(get.max.cals(calories))
print(sum.top.n.max.cols(calories))
