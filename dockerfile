FROM httpd:2.4.33
COPY ./html/ /usr/local/apache2/htdocs/
COPY ./config/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./cgi-bin /usr/local/apache2/cgi-bin