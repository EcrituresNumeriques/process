#!/bin/bash
 echo "Content-type: text/html"
 echo ""
 
echo "<html><head><title>Demo</title></head><body>"
echo "Testing some script<br>"
echo "Current directory is $(pwd) <br>"
echo "Shell Script name is $0"

version="5b2a766ec032fa0011a6a6b9"
id="SP001"


curl -o $id.zip https://stylo.ecrituresnumeriques.ca/api/v1/zipVersion/$version
curl -o $id.html https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
wget -nd -p -H -P media/ -A jpeg,jpg,bmp,gif,png -e robots=off https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
unzip $id.zip
rename "s/${version}/${id}/g" *
sed -i -e "s/\/${version}/${id}/g" $id.yaml
pandoc --standalone --filter pandoc-citeproc --template=/home/marcello/Desktop/sp/git/chaineEditorialeSP/templates/templateLaTeX.latex -f markdown -t latex $id.md $id.yaml -o $id.md.tex
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.html
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md.tex
cd media
COUNTER=0
for filename in "$3"*; do
    COUNTER=$[$COUNTER +1]
    echo "${filename%.*}" 
    sed -i -e "s/${filename%.*}/img${COUNTER}/g" ../$id.md
    sed -i -e "s/${filename%.*}/img${COUNTER}/g" ../$id.md.tex
    sed -i -e "s/${filename%.*}/img${COUNTER}/g" ../$id.html
    mv ${filename%.*}.${filename##*.} img${COUNTER}.${filename##*.}
done
cd ..
cp -r ../media ./
pdflatex $id.md.tex
rm $id.zip

 echo "</body></html>"