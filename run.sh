#!/bin/bash

for file in backend/*;
do
  if [ -f "$file" ]
  then
    echo "Running $file..."
    python "$file"
    echo "Done."
  fi
done
