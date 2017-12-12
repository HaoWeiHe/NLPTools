mkdir StanfordNLP
mkdir StanfordNLP/jars
cd StanfordNLP/jars
wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1NWT_iNzYhFLR9jQMArFzp4Whc2dblvvl' -O "slf4j-api.jar"| sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p'
wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1jLovERrqdRwgyJvV8MG8qSwPTcKrTP_t' -O "stanford-parser.jar"| sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p'
wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1VIgrfPOSmxyqEcx1oadHspYO7TfibE-e' -O "stanford-postagger.jar"| sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p'
wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1SLcGyC1oZ942B43vu_q4HjROvdxowgZb' -O "stanford-segmenter-3.7.0.jar"| sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p'

#!/bin/bash

SOURCE="https://drive.google.com/open?id=1TPChlN4iHx8aqGtqv-jztDEuPH2309PH"
if [ "${SOURCE}" == "" ]; then
    echo "Must specify a source url"
    exit 1
fi

DEST="stanford-parser-3.8.0-models.jar"
if [ "${DEST}" == "" ]; then
    echo "Must specify a destination filename"
    exit 1
fi

FILEID=$(echo $SOURCE | rev | cut -d= -f1 | rev)
COOKIES=$(mktemp)

CODE=$(wget --save-cookies $COOKIES --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=${FILEID}" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p')


CODE=$(echo $CODE | rev | cut -d: -f1 | rev | xargs)

wget --load-cookies $COOKIES "https://docs.google.com/uc?export=download&confirm=${CODE}&id=${FILEID}" -O $DEST

rm -f $COOKIES
