#!/bin/bash


version="5b2bc423e5842b0011ac871a"
id="default"
export HOME="/usr/local/apache2/cgi-bin"


echo "Content-type: text/html"
echo ""

echo "<html><head><title>Demo</title></head><body>"

#Assign parameters : exec.cgi?id=SP002&version=5b2be647e5842b0011ac874d
id=$(echo $QUERY_STRING | sed 's/.*id\=\([^&]\+\).*/\1/')
version=$(echo $QUERY_STRING | sed 's/.*version\=\([^&]\+\).*/\1/')

echo "<br>Version : ${version} => ${id}<br>"
mkdir $version
cd $version

curl -o $id.zip https://stylo.ecrituresnumeriques.ca/api/v1/zipVersion/$version
curl -o $id.html https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
wget -nd -p -H -P media/ -A jpeg,jpg,bmp,gif,png -e robots=off https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/$version
unzip $id.zip
rm $id.zip

rename "s/${version}/${id}/g" *
sed -i -e "s/\/${version}/${id}/g" $id.yaml

#pandoc --standalone --filter pandoc-citeproc --latex-engine=xelatex --template=../templates/templateLaTeX.latex -f markdown -t latex $id.md $id.yaml -o $id.md.tex


sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.html
sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' $id.md.tex



if find media/ -mindepth 1 -print -quit 2>/dev/null | grep -q .; then
cd media
COUNTER=0
for filename in "$3"*; do
    COUNTER=$[$COUNTER +1]
    echo "${filename%.*}" 
    sed -i -e "s@${filename%.*}@${id}\-img${COUNTER}@g" $id.md
    sed -i -e "s@${filename%.*}@${id}\-img${COUNTER}@g" $id.md.tex
    sed -i -e "s@${filename%.*}@${id}\-img${COUNTER}@g" $id.html
    mv ${filename%.*}.${filename##*.} ${id}-img${COUNTER}.${filename##*.}
done
cd ..
fi


#Copy assets in the /media files
cp -r ../assets/* ./media

#create PDF

pandoc --standalone --filter pandoc-citeproc --latex-engine=xelatex --template=../templates/templateLaTeX.latex -f markdown -t latex $id.md $id.yaml -o $id.md.pdf


#xelatex $id.md.tex


#Zip all files and move ZIP and PDF to export
zip -r $id.zip .
mv $id.zip /usr/local/apache2/htdocs/export/ 
mv $id.md.pdf /usr/local/apache2/htdocs/export/ 

#Clean folder
cd ..
rm -R $version

echo "<br>"
echo "PDF : <a href='/export/${id}.md.pdf' target='_blank'>/export/${id}.md.pdf</a><br>"
echo "ZIP : <a href='/export/${id}.zip' target='_blank'>/export/${id}.zip</a><br>"


echo "</body></html>"
