#!/bin/bash

# Standalone generator for cheeesy/UwUizer.py

sed -i 's;#!/usr/bin/env python3;#bigdumb;g' UwUizer.py
sed -i 's;NotYetUwUed="Placeholder text?";#NotYetUwUed;g' UwUizer.py

standalonePath="standalone.py"

echo "#!/usr/bin/env python3" > $standalonePath
echo "" >> $standalonePath
echo 'NotYetUwUed=input("What wowd do yowouwu want towo uwu-ize? ")' >> $standalonePath
echo "" >> $standalonePath

echo "$(cat $standalonePath UwUizer.py)" > $standalonePath

sed -i "s;#bigdumb;;g" $standalonePath
sed -i "s;#NotYetUwUed;;g" $standalonePath

sed -i 's;#bigdumb;#!/usr/bin/env python3;g' UwUizer.py
sed -i 's;#NotYetUwUed;NotYetUwUed="Placeholder text?";g' UwUizer.py

chmod +x $standalonePath
