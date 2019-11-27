#!/bin/bash

# Standalone generator for cheeesy/UwUizer.py

standalonePath="standalone.py"

cp UwUizer.py $standalonePath

sed -i 's;"Placeholder text?";input("What wowowd do yowouwu want towo uwu-ize? ");g' $standalonePath

chmod +x $standalonePath
