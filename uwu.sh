#!/bin/bash

read UwUThis
sed -i "s/Placeholder text?/$UwUThis/g" UwUizer.py
python3 UwUizer.py
sed -i "s/$UwUThis/Placeholder text?/g" UwUizer.py
