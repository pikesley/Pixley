#!/bin/bash

find . -name "*pyc" -delete
rsync -av patterns /Volumes/CIRCUITPY/lib/Pixley/
cp *.py  /Volumes/CIRCUITPY/lib/Pixley
