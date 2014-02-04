#!/bin/bash
# File Name : lloutput.sh
# Purpose : get the last row and last column from stdout
# Creation Date : 04-02-2014
# Last Modified : Tue 04 Feb 2014 08:58:52 PM CST
# Release By : Doom.zhou

#function
function show()
{
    if [[ -n $1 ]] 
    then
        #echo "dealing....."
        #echo -e "First display stdout! with color green \033[32;1m"
        #$1
        #echo -e "\033[0mcommand end!"
        if [[ -n $2 ]]
        then
            x=`echo $2 | cut -c 1`
            y=`echo $2 | cut -c 2`
            if [[ $x == 'l' ]] && [[ $y =~ ^[0-9]$ ]]
            then
                out=`$1 | awk -v y=$y 'END{print$y}'`
                echo $out
            elif [[ $y == 'l' ]] && [[ $x =~ ^[0-9]$ ]]  
            then
                out=`$1 | awk -v x=$x 'NR==x{print$NF}'`
                echo $out
            elif [[ $2 =~ ^[0-9]{2}$ ]]
            then
                out=`$1 | awk -v x=$x -v y=$y 'NR==x{print$y}'`
                echo $out
            elif [[ $2 == 'll' ]]
            then
                out=`$1 | awk 'END{print$NF}'`
                echo $out
            fi
        else
            echo $2"is a invalid int"
        fi
    else
        echo "Input your command like df so i can get x column and y filed info"
    fi
}
show "$1" "$2"
#end
