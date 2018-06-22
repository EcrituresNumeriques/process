FROM httpd:2.4.33
RUN apt-get update && apt-get install -y curl wget unzip zip rename pandoc pandoc-citeproc texlive texlive-lang-french texlive-latex-extra
COPY ./html/ /usr/local/apache2/htdocs/
COPY ./config/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./cgi-bin /usr/local/apache2/cgi-bin

# Give permission to Daemon to cgi-bin
RUN chown daemon:daemon -R /usr/local/apache2/cgi-bin
RUN chown daemon:daemon -R /usr/local/apache2/htdocs/export/

