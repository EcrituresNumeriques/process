#!/bin/bash

#Quick parameters links
#version="5b2bc423e5842b0011ac871a"
#id="default"
#processor="xelatex"

export HOME="/usr/local/apache2/cgi-bin"


echo "Content-type: text/html"
echo ""

echo "<html>
<head>
<title>Stylo export</title>

<!--style et lien vers CSS-->
<style type=\"text/css\">code{white-space: pre;}</style>
<!--Generated CSS from stylo-->
<style type=\"text/css\">
html, body {
background: #f8f8f8;
font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;
margin: 0;
padding: 0;
width: 100%;
min-height: 100%;
overflow-x: hidden;
position: relative;
      }
      body {
      overflow-y: scroll;
      }

      #app {
      min-height: 100vh;
      }

      #app > header, .gridCenter > header {
      padding: 0.5rem 1rem;
      background-color: #7c7c7c;
      color: white;
      display: flex;
      align-items: center;
      }
      #app > header .wrapper, .gridCenter > header .wrapper {
      flex: 1 1 auto;
      }
      #app > header h1, .gridCenter > header h1 {
      margin: 0;
      flex: 0 0 auto;
      }
      #app > header nav, .gridCenter > header nav {
      flex: 0 0 auto;
      }
      #app > header nav a, .gridCenter > header nav a {
      color: white;
      margin-left: 1rem;
      }

      div#app header {
      margin-bottom: 20px;
      }
      div#app header img {
      width: 100%;
      padding-bottom: 20px;
      }
      div#app main#mainView {
      margin: 0 auto;
      width: 100%;
      max-width: 1000px;
      background-color: white;
      padding: 1em;
      }
      div#app main#mainView section h1 {
      font-size: 2em;
      margin: 0 0 1em 0;
      }

      div#app main#mainView p {
      text-align: justify;
      font-family: sans;
      font-size: 1em;
      line-height: 1.5em;
      }

      div#app main#mainView h1, div#app main#mainView h2, div#app main#mainView h3 {
      color:purple;
      }

      div#app main#mainView a{
      color:purple;
      }

      div#app main#mainView li {
      text-align: justify;
      font-family: sans;
      font-size: 1em;
      line-height: 1.4em;
      }

      div#app main#mainView blockquote {
      border-left: 4px solid lightgrey;
      padding-left: 1em;
      font-size: 1em;
      }

      div#app main#mainView sup {
      font-size: 0.7em;
      }

      div#app main#mainView .citation {
      color: darkslateblue;
      }

      div#app main#mainView .footnoteRef {
      font-weight: 600;
      }

      div#app main#mainView .references p{
      font-size: 0.9em;
      line-height: 1.3em;
      }

      div#app main#mainView .footnotes p {
      font-size: 0.9em;
      line-height: 1.3em;
      }

      div.indexations-foaf{
      background-color: #f0f0f0;
      padding: 0.5rem 1rem;
      }

      div#schema-scholarly-article{
      background-color: #f0f0f0;
      padding: 0.5rem 1rem;
      }

      #schema-scholarly-article > span:nth-child(1)::before {
      content: \\"Title: \\";
      }

      #schema-scholarly-article > span:nth-child(1) {
      font-size:2rem;
      }

      #schema-scholarly-article > span:nth-child(3)::before{
      content: \"Subtitle: \";
      font-weight: bold;
      }

      #schema-scholarly-article > span[property=\"author\"]::before{
      content:\"Author: \";
      font-weight: bold;
      }

      .indexations-foaf {
      display:none;
      }

      #schema-scholarly-article > span:nth-child(9) > span:nth-child(1)::before {
      content:\"Publisher: \";
      font-weight: bold;
      }

      #schema-scholarly-article > span:nth-child(9) > span:nth-child(3)::before {
      content:\"ISSN: \";
      font-weight: bold;
      }

      #schema-scholarly-article > div:nth-child(10) > span:nth-child(1) > span:nth-child(1)::before {
      content:\"Journal: \";
      font-weight: bold;
      }

      #schema-scholarly-article > div:nth-child(10) > span:nth-child(2)::before {
      content:\"Date: \";
      font-weight: bold;
      }

      .titreDossier::before {
      content:\"Dossier: \";
      font-weight: bold;
      }

      div.resume:nth-child(1)::before {
      content:\"Abstract: \";
      font-weight: bold;
      }

      .keywords::before {
      content:\"Aligned Keywords:\";
      font-weight: bold;
      }

      div.authorKeywords_fr {
      background-color: #f0f0f0;
      padding: 0.5rem 1rem;
      }

      div.authorKeywords_en {
      background-color: #f0f0f0;
      padding: 0.5rem 1rem;
      }

      div.indexations-foaf:before {
      content:\"foaf: \";
      font-style:italic;

      }
      div.authorKeywords_fr:before {
      content:\"Mot-clefs: \";
      font-style:italic;
      }
      div.authorKeywords_en:before {
      content:\"Keywords: \";
      font-style:italic;
      }

      p span.epigraphe {
      margin-left: 100px;
      margin-right: 300px;
      text-align: left;
      margin-top: 10px;
      margin-bottom: 30px;
      float: right;
      font-style: italic;
}

p span.dedicace {
margin-left: 100px;
text-align: left;
margin-top: 10px;
margin-bottom: 30px;
float: right;
font-style: italic;
}

p span.note {
margin-left: 100px;
text-align: left;
margin-top: 10px;
margin-bottom: 30px;
float: right;
font-style: italic;
}

span.these {
background-color: MistyRose;
}

span.these:hover::before {
content: \"Th&#232;se: <\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.these:hover::after {
content: \">\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.exemple {
background-color: PowderBlue;
}

span.exemple:hover::before {
content: \"Exemple: <\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.exemple:hover::after {
content: \">\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.concept {
background-color: Plum;
}

span.concept:hover::before {
content: \"Concept cl&#233;: <\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.concept:hover::after {
content: \">\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.definition {
background-color: Peachpuff;
}

span.definition:hover::before {
content: \"D&#233;finition: <\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.definition:hover::after {
content: \">\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.question {
background-color: PaleGoldenRod ;
}

span.question:hover::before {
content: \"Question: <\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

span.question:hover::after {
content: \">\";
position:relative;
color: purple;
background-color: whitesmoke;
font-size: 1em;
padding-left:5px;
padding-right:5px;
}

}
</style>
</head>

<!--corps du document-->
<body>
<div id=\"app\">
<header><h1>Stylo Export</h1><div class=\"wrapper\"></div><nav><a href=\"javascript:window.close()\">close</a></nav></header>
<main id=\"mainView\"><h2>Export of a Stylo article</h2> "

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

if [ "${GET[toc]}" = "true" ]; then
	toc="--table-of-contents"
else
	toc=""
fi
echo "<p>You are exporting: <br>Article name: <b>${GET[id]}</b><br> Version : <b>${GET[version]} </b>(this is the id of the version you are exporting).<br>Format : <b>${GET[format]} </b>(this is the format you asked; more formats are avaiable on this page)<br>Bibliographical style : <b>${GET[bibstyle]} </b>(more bibliographical styles avaiable on this page)<br>Table of contents : ${GET[toc]}<br>Processor : ${GET[processor]}<br> Your Stylo server is: ${GET[source]}</p>"

#exiting if either id or version not specified
if [ -z "${GET[id]}" ]; then
	echo "No id specified";
	echo "</body></html>"
	exit 1
fi
#if [ -n "${GET[article]}"]; then
#    GET[version]=${GET[article]}
#    echo "This is an article"
#    endpoint="Article"
#fi
if [ -z "${GET[version]}" ]; then
	echo "No version specified";
	echo "</body></html>"
	exit 1
fi

GET[source]=${GET[source]//"%3A"/:}
GET[source]=${GET[source]//"%2F"/\/}
#echo ${GET[source]}
#Relocate script + create folder for that version
cd "$(dirname "$0")"
mkdir ${GET[version]}
cd ${GET[version]}
curl -o ${GET[id]}.zip ${GET[source]}zip${endpoint}/${GET[version]}
# curl -o ${GET[id]}.html https://stylo.ecrituresnumeriques.ca/api/v1/html${endpoint}/${GET[version]}
wget -nd -p -H -P media/ -A jpeg,jpg,bmp,gif,png -e robots=off ${GET[source]}htmlVersion/${GET[version]}
unzip ${GET[id]}.zip >> bash.log
rm ${GET[id]}.zip

rename "s/${GET[version]}/${GET[id]}/g" *
sed -i -e "s/\/${GET[version]}/${GET[id]}/g" ${GET[id]}.yaml



sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' ${GET[id]}.md

# not usefull if the html and the tex are made after renaming images in the md file
# sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' ${GET[id]}.html
# sed -i -e 's/https:\/\/i\.imgur.com\//media\//g' ${GET[id]}.md.tex



if find media/ -mindepth 1 -print -quit 2>/dev/null | grep -q .; then
	cd media
	echo "You have media file(s):<br>"
	COUNTER=0
	for filename in "$3"*; do
		COUNTER=$[$COUNTER +1]
		echo "<b>${filename%.*}</b> will be renamed <b>${GET[id]}-img${COUNTER}.*</b><br>"
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


# commands of the sens public export. delete when yo are sure that everything works
# pandoc --standalone --template=../templates/templateHtmlDcV2.html5  --ascii --filter pandoc-citeproc -f markdown -t html ${GET[id]}.md ${GET[id]}.yaml  --csl ../templates/chicagomodified.csl -o ${GET[id]}.html
# 
# pandoc --standalone --filter pandoc-citeproc --table-of-contents --template=../templates/templateLaTeX.latex -f markdown -t latex ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.md.tex
# 
#create PDF using processor


case "${GET[format]}" in
	"pdf")
		pandoc --standalone --verbose --filter pandoc-citeproc $toc  -f markdown -t latex --csl ../templates/${GET[bibstyle]}.csl --pdf-engine=xelatex ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.pdf >> bash.log

		echo "pandoc --standalone --verbose --filter pandoc-citeproc --table-of-contents -f markdown -t latex --csl ../templates/${GET[bibstyle]}.csl --pdf-engine=xelatex ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.pdf >> bash.log"



		echo "<pre>Getting PDF file ready"
		echo "</pre>"

		#Zip all files and move ZIP and PDF to export
		echo "<pre>Getting ZIP file ready"
		zip -r ${GET[id]}.zip .
		echo "</pre>"
		mv ${GET[id]}.zip /usr/local/apache2/htdocs/export/
		mv ${GET[id]}.pdf /usr/local/apache2/htdocs/export/
		#Clean folder
		cd ..
		rm -R ${GET[version]}

		echo "<br>"
		echo "PDF : <a href='/export/${GET[id]}.pdf' target='_blank'>/export/${GET[id]}.pdf</a><br>"

		echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"

		;;
	"tex")
		pandoc --standalone --verbose --filter pandoc-citeproc $toc -f markdown -t latex --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.tex >> bash.log

		echo "pandoc --standalone --filter pandoc-citeproc --table-of-contents -f markdown -t latex --template=../template/template.latex --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.pdf >> bash.log"
		xelatex --interaction=batchmode ${GET[id]}.tex >> bash.log
		xelatex --interaction=batchmode ${GET[id]}.tex


		echo "<pre>Getting PDF file ready"
		echo "</pre>"

		#Zip all files and move ZIP and PDF to export
		echo "<pre>Getting ZIP file ready"
		zip -r ${GET[id]}.zip .
		echo "</pre>"
		mv ${GET[id]}.zip /usr/local/apache2/htdocs/export/
		mv ${GET[id]}.pdf /usr/local/apache2/htdocs/export/
		#Clean folder
		cd ..
		rm -R ${GET[version]}

		echo "<br>"
		echo "PDF : <a href='/export/${GET[id]}.pdf' target='_blank'>/export/${GET[id]}.pdf</a><br>"

		echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"

		;;
	"xml")   	
		pandoc --standalone --verbose --filter pandoc-citeproc -f markdown -t html5 --csl ../templates/chicagomodified.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.html >> bash.log

java  -cp /usr/local/vendor/saxon9he.jar:/usr/local/vendor/tagsoup-1.2.1.jar net.sf.saxon.Transform -x:org.ccil.cowan.tagsoup.Parser -s:${GET[id]}.html -xsl:../templates/XHTML52erudit.xsl -o:${GET[id]}.xml !indent=yes
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
		;;
	zip)   	

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

		echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"
		;;
	html5)   	
		pandoc --standalone --verbose --filter pandoc-citeproc $toc -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.html >> bash.log

		echo "<pre>Getting ${GET[format]} file ready"
		echo "</pre>"

		#Zip all files and move ZIP and PDF to export
		echo "<pre>Getting ZIP file ready"
		zip -r ${GET[id]}.zip .
		echo "</pre>"
		mv ${GET[id]}.zip /usr/local/apache2/htdocs/export/
		mv ${GET[id]}.html /usr/local/apache2/htdocs/export/
		#Clean folder
		cd ..
		rm -R ${GET[version]}

		echo "<br>"
		echo "${GET[format]} : <a href='/export/${GET[id]}.html' target='_blank'>/export/${GET[id]}.html</a><br>"

		echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"
		;;
	*)   	
		pandoc --standalone --verbose --filter pandoc-citeproc $toc -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log

	echo	"pandoc --standalone --verbose --filter pandoc-citeproc $toc -f markdown -t ${GET[format]} --csl ../templates/${GET[bibstyle]}.csl ${GET[id]}.md ${GET[id]}.yaml -o ${GET[id]}.${GET[format]} >> bash.log"
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
		;;
esac


# Unnecessary if the pdf is made directly without using tex file
# if [ "${GET[processor]}" = "pdflatex" ]; then
#     pdflatex ${GET[id]}.md.tex >> bash.log
#     pdflatex ${GET[id]}.md.tex >> bash.log
# else
#     xelatex ${GET[id]}.md.tex >> bash.log
#     xelatex ${GET[id]}.md.tex >> bash.log
# fi

#Create erudit XML from HTML
#java  -jar /usr/local/vendor/saxon9he.jar -s:${GET[id]}.html -xsl:../templates/XHTML2eruditV2.xsl -o:${GET[id]}.erudit.xml

#Zip all files and move ZIP and PDF to export
# echo "<pre>Getting ZIP file ready"
# zip -r ${GET[id]}.zip .
# echo "</pre>"
# mv ${GET[id]}.zip /usr/local/apache2/htdocs/export/
# mv ${GET[id]}.pdf /usr/local/apache2/htdocs/export/
# 
#Clean folder
# cd ..
# rm -R ${GET[version]}
# 
# echo "<br>"
# echo "PDF : <a href='/export/${GET[id]}.pdf' target='_blank'>/export/${GET[id]}.pdf</a><br>"
# echo "ZIP : <a href='/export/${GET[id]}.zip' target='_blank'>/export/${GET[id]}.zip</a><br>"
# 

echo "
<h3>More export options</h3>
<form action=\"/cgi-bin/exportArticle/exec.cgi\" method=\"get\">
<input type=\"hidden\" name=\"source\" value=\"${GET[source]}\"> 
<input type=\"hidden\" name=\"id\" value=\"${GET[id]}\">
<input type=\"hidden\" name=\"version\" value=\"${GET[version]}\">
Format:
<select name=\"format\">
<option value=\"pdf\">PDF</option>
<option value=\"tex\">tex</option>
<option value=\"html5\">HTML</option>
<option value=\"xml\">XML eruditArticle</option>
<option value=\"odt\">odt</option>
<option value=\"docx\">docx</option>
<option value=\"tei\">TEI Lite</option>

</select>
<br/>
<br/>
Bibliographical style:  

<select name=\"bibstyle\">
<option value=\"chicagomodified\">Chicago inline</option>
<option value=\"chicago-fullnote-bibliography-fr\">Chicago footnotes</option>
<option value=\"lettres-et-sciences-humaines-fr\">Lettres et sciences humaines</option>
</select>
<br/>
Processor: <br>
<label><input type=\"radio\" name=\"processor\" value=\"xelatex\" checked>xelatex</label><br>
<label><input type=\"radio\" name=\"processor\" value=\"pdflatex\">pdflatex</label><br>

<input type=\"submit\" value=\"Submit\">
</form>"

#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=html&bibstyle=${GET[bibstyle]}\">Export en HTML</a>"
#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=docx&bibstyle=${GET[bibstyle]}\">Export en DOCX</a>"
#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=tei&bibstyle=${GET[bibstyle]}\">Export en TEI Lite</a>"
#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=odt&bibstyle=${GET[bibstyle]}\">Export en ODT</a>"
#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=pdf&bibstyle=${GET[bibstyle]}\">Export en PDF</a>"
#echo "<a href=\"/cgi-bin/exportArticle/exec.cgi?id=${GET[id]}&version=${GET[version]}&processor=${GET[procesor]}&source=${GET[source]}&format=${GET[format]}&bibstyle=chicago-fullnote-bibliography-fr.csl\">Export en Chicago Fullnote</a>"
#echo "</main></div></body></html>"
