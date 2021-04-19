#!/bin/bash

# downloading text file if not present in folder TODO change to wget
if [ ! -e README ]
  then
    curl -O ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README
fi

# convert file content to lowercase
tr '[:upper:]' '[:lower:]' < README |

# remove unnecessary characters and numbers
sed 's|[:/.,0-9]||g'