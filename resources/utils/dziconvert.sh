#!/bin/bash

for f in *; do 
    vips dzsave $f $f --vips-progress
done