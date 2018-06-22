FROM httpd:2.4.33
RUN apt-get update && apt-get install -y curl wget unzip rename pandoc
COPY ./html/ /usr/local/apache2/htdocs/
COPY ./config/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./cgi-bin /usr/local/apache2/cgi-bin

# Give permission to Daemon to cgi-bin
RUN chown daemon:daemon -R /usr/local/apache2/cgi-bin

