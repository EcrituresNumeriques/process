#!/bin/bash

#Quick parameters links
#version="5b2bc423e5842b0011ac871a"
#id="default"
#processor="xelatex"

export HOME="/usr/local/apache2/cgi-bin"


echo "Content-type: text/html"
echo ""

echo "<html><head><title>Demo</title></head><body>"

#Assign parameters : exec.cgi?id=SP002&version=5b2be647e5842b0011ac874d&processor=pdflatex
#returns ${GET[id]} ${GET[version]} ${GET[processor]}
saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS
declare -A GET
for ((i=0; i<${#parm[@]}; i+=2))
do
	GET[${parm[i]}]=${parm[i+1]}
done

#Assign defaults
endpoint="Version"

echo "<p>id : ${GET[id]}<br> Article : ${GET[article]}<br> Version : ${GET[version]}<br>Format : ${GET[format]}<br>Bibliographical style : ${GET[bibstyle]}<br>Processor : ${GET[processor]}</p>"

#exiting if either id or version not specified
if [ -z "${GET[id]}" ]; then
	echo "No id specified";
	echo "</body></html>"
	exit 1
fi

if [ -z "${GET[version]}" ]; then
	echo "No version specified";
	echo "</body></html>"
	exit 1
fi

#Relocate script + create folder for that version
cd "$(dirname "$0")"
mkdir ${GET[version]}
cd ${GET[version]}

curl -o ${GET[id]}.zip https://stylo.ecrituresnumeriques.ca/api/v1/zip${endpoint}/${GET[version]}
# curl -o ${GET[id]}.html https://stylo.ecrituresnumeriques.ca/api/v1/html${endpoint}/${GET[version]}
wget -nd -p -H -P media/ -A jpeg,jpg,bmp,gif,png -e robots=off https://stylo.ecrituresnumeriques.ca/api/v1/htmlVersion/${GET[version]}
unzip ${GET[id]}.zip >> bash.log
rm ${GET[id]}.zip

rename "s/${GET[version]}/${GET[id]}/g" *
sed -i -e "s/\/${GET[version]}/${GET[id]}/g" ${GET[id]}.yaml



sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' ${GET[id]}.md




if find media/ -mindepth 1 -print -quit 2>/dev/null | grep -q .; then
	cd media
	COUNTER=0
	for filename in "$3"*; do
		COUNTER=$[$COUNTER +1]
		echo "${filename%.*}"
		sed -i -e "s@${filename%.*}@${GET[id]}\-img${COUNTER}@g" ../${GET[id]}.md
		# not usefull if the html and the tex are made after renaming images in the md file
		#    sed -i -e "s@${filename%.*}@${GET[id]}\-img${COUNTER}@g" ../${GET[id]}.md.tex
		#    sed -i -e "s@${filename%.*}@${GET[id]}\-img${COUNTER}@g" ../${GET[id]}.html
		mv ${filename%.*}.${filename##*.} ${GET[id]}-img${COUNTER}.${filename##*.}
	done
	cd ..
fi


#Copy assets in the /media files: uncomment if there are any images to include (for example a logo)
# cp -r ../assets/* ./media

preparefiles ()
{
	echo "<pre>Getting ${GET[format]} file ready"
	echo "</pre>"

	#Zip all files and move ZIP and PDF to export
	echo "<pre>Getting ZIP file ready"
	zip -r ${GET[id]}.zip .
	echo "</pre>"
	mv ${GET[id]}.zip /usr/local/apache2/htdocs/export/
	mv ${GET[id]}.${GET[format]} /usr/local/apache2/htdocs/export/
	#Clean folder
	cd ..
	rm -R ${GET[version]}

	echo "<br>"
	echo "${GET[format]} : <a href='/export/${GET[id]}.${GET[format]}' target='_blank'>/export/${GET[id]}.${GET[format]}</a><br>"

	echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"

}


case "${GET[format]}" in
pdf) pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t latex --latex-engine=xelatex --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.pdf >> bash.log;;
html) pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log;;
docx) pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log;;
odt) pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log;;
tei) pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log;;
*) echo "not working";;
esac

#if [ "${GET[format]}" = "pdf" ]; then
#	pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t latex --latex-engine=xelatex --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.pdf >> bash.log

	preparefiles

#else   	
#	pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log

#	preparefiles

#fi




echo "</body></html>"
