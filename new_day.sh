#!/usr/bin/env bash

# This script will prep your dev environment for a new daily challenge.
# It will create the folders, create the files with some basic commands and
# pull the input from adventofcode.com.
#
# usage:
#   # create data for day 06
#   $ sh new_day.sh 06

year=2021

if [ $# -ne 1 ] || [ ${#1} -ne 2 ] ; then
  echo "Please specify the day to create the data for in the correct format (e.g. 01, 04, 10, 25)."
  exit
fi

# check if directory exists
day_number=$1
dir_name="day"$day_number

if [ -d "days/$dir_name" ] ; then
  echo "Project files already present for $dir_name. Stopping now."
  exit
fi

# remove trailing 0's for url
if [[ ${day_number:0:1} == "0" ]] ; then
  day_number=${day_number:1}
fi

echo "Setting up project files for $dir_name."
cp -r days/day00 days/$dir_name

# setting the cookie and using it to retrieve the data
session_cookie=$(<session_cookie.txt)
url="https://adventofcode.com/$year/day/$day_number/input"
header="cookie:session=$session_cookie;"
response=$(curl -s -o /dev/null -I -w "%{http_code}" $url -H $header)

if [ $response -ne "200" ] ; then
  echo "Hmm shittie, something is wrong with retrieving the data. Received an response code $response. Sorry!"
  exit
else
  curl $url -H $header -o "days/$dir_name/input.txt"
fi
