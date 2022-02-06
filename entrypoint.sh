#!/bin/sh -l
jupyter nbconvert --to markdown $1
echo "Converting $1"
time=$(date)
echo "::set-output name=time::$time"
