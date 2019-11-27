#!/bin/bash

# Standalone generator for cheeesy/UwUizer.py

standalonePath="standalone.py"

cp UwUizer.py $standalonePath

sed -i 's;"Placeholder text?";input("Pwease entew the sentence you would wike to have uwu-ized, uwu: ");g' $standalonePath

chmod +x $standalonePath
