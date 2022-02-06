#!/bin/sh -l
echo asddsads $(ls ${GITHUB_WORKSPACE})
echo $(ls .)
# echo "Converting $1"
# time=$(date)
# echo "::set-output name=time::$time"
python main.py