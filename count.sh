#!/bin/bash

# downloading text file if not present in folder
if [ ! -e README ]
  then
    wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README
fi

# convert file content to lowercase
tr '[:upper:]' '[:lower:]' < README |

# remove unnecessary characters and numbers
sed 's|[:/.,0-9]||g' |

# remove line breaks
tr -d "\n" |

# remove multiple spaces
tr -s " " |

# split every word into a new line
sed 's/ /\n/g;' |

# sort alphabetically and remove duplicate words
sort | uniq -c |

# reverse sort the count of words and print the 10 most common words
sort -r | head