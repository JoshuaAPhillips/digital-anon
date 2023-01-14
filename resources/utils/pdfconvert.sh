#!/bin/bash

for f in *; do
    convert -density 240 $f -quality 90  output/$f.png
    echo $f;
done