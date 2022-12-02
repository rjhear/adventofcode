#' 01_b.R
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
break.point <-
  function(arr, idx) {
    unname(split(arr, cumsum(seq_along(arr) %in% idx)))
  }

sum.cals <- function(cal) {
  sum(as.numeric(cal), na.rm = T)
}

get.cal.totals <- function(filepath, n = 3) {
  calories <- readLines(filepath)
  return (calories |>
            break.point(which(calories == "")) |>
            lapply(sum.cals) |>
            unlist() |>
            sort() |>
            tail(n))
}


# Driver ------------------------------------------------------------------
calories <- get.cal.totals(puzzle.input)
print(max(calories))
print(sum(calories))
