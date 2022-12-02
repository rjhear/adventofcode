#!/bin/bash

# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1
#
#  ========= SOLUTIONS ==========
# + PART 1 .......65,912 calories
# + PART 2 ......195,625 calories

function read_lines() {
  declare -a arr
  while IFS= read -r line; do
    [[ -z "$line" ]] && arr+=($sum) && sum=0 && continue && sum=0 || sum=$((sum + line))
  done \
    <$1
  arr=($(echo $arr | tr " " "\n" | sort -n | tail -3))
  echo "PART 1: $(printf "%d\n" "${arr[@]}" | tail -1)"
  echo "PART 2: $(
    IFS=+
    echo "$((${arr[*]}))"
  )"
}

read_lines "./data/01_input.txt"
