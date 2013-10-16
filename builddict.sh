#!/bin/bash
# usage: builddict.sh in_filename tokensize numbersize1 numbersize2 out_filename
#
# Input file format:
#   lines starting with # or empty lines are ignored
#   lines must contain at least one \t, characters after last \t of each line
#   are discarded
#
# Output file format:
#   input file
#   index
#   10 characters: byte at which index starts, as decimal string
#   space
#   10 characters: length of index in bytes, as decimal string
#   space
#   10 characters: tokensize, as decimal string
#   space
#   10 characters: numbersize, as decimal string
#   space
#   10 characters: numbersize of line length, as decimal string

filename="$1"
tokensize="$2"
numbersize="$3"
numbersize2="$4"
outfile="$5"

python buildindex.py "$filename" $tokensize $numbersize $numbersize2 > tmp-index.dat
LC_LOCALE=C LC_COLLATE=C sort tmp-index.dat > tmp-index_sorted.dat
indexstart=`cat $1 | wc -c`
indexlength=`cat tmp-index_sorted.dat | wc -c`
echo $linelength $indexstart $indexlength
cat "$filename" tmp-index_sorted.dat > "$outfile"
printf "%10d %10d %10d %10d %10d" $indexstart $indexlength $tokensize $numbersize $numbersize2 >> "$outfile"
