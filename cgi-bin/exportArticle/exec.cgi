#!/bin/bash
 echo "Content-type: text/html"
 echo ""
 
echo "<html><head><title>Demo</title></head><body>"
echo "Testing some script<br>"
echo "Current directory is $(pwd) <br>"
echo "Shell Script name is $0"

version="5b2bc423e5842b0011ac871a"
id="SP001"
export HOME="/usr/local/apache2/cgi-bin"


curl -o $id.zip https://stylo.ecrituresnumeriques.ca/api/v1/zipVersion/$version
curl -o $id.html https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
wget -nd -p -H -P media/ -A jpeg,jpg,bmp,gif,png -e robots=off https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
unzip $id.zip
rename "s/${version}/${id}/g" *
sed -i -e "s/\/${version}/${id}/g" $id.yaml
pandoc --standalone --filter pandoc-citeproc --template=templates/templateLaTeX.latex -f markdown -t latex $id.md $id.yaml -o $id.md.tex

echo "<br>"
echo "PANDOC DONE<br>"
echo "<br>"
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.html
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md.tex
cd media

echo "<br>"
echo "In media<br>"
echo "<br>"

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

echo "<br>"
echo "Outside Media<br>"
echo "<br>"

cp -r media/* ./


echo "<br>"
echo "Copied<br>"
echo "<br>"


pdflatex $id.md.tex
mv $id.md.pdf /usr/local/apache2/htdocs/export/ 
rm $id.zip
echo "<br>"
echo "Cleaned<br>"
echo "<br>"

ls || echo

echo "<br>"
echo "pdf : <a href='/export/${id}.md.pdf' target='_blank'>/export/${id}.md.pdf</a>"
echo "Tex file :<br>"
echo "<br>"

cat $id.md.tex

echo "</body></html>"