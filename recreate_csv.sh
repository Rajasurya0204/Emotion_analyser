#!/bin/bash
input="train.csv"
while IFS= read -r line
do
  echo "$line"
done < "$input" 
