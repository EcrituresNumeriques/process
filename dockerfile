FROM httpd:2.4.33

RUN apt-get update && apt-get install -y curl wget unzip zip rename texlive texlive-lang-french texlive-latex-extra texlive-xetex default-jre python-pip wget
COPY ./vendor /usr/local/vendor/
RUN dpkg -i /usr/local/vendor/pandoc-1.19.2.1-1-amd64.deb
RUN tar -xzf /usr/local/vendor/linux-ghc8-pandoc-1-19.tar.gz && \
    mv pandoc-crossref /usr/bin/ && \
    pip install pandocfilters && \
    apt-get clean -y && \
    rm -rf /usr/local/vendor/pandoc-1.19.2.1-1-amd64.deb /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && apt-get install -y texlive-lang-all texlive-math-extra


COPY ./html/ /usr/local/apache2/htdocs/
COPY ./config/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./cgi-bin /usr/local/apache2/cgi-bin

# Give permission to Daemon to cgi-bin
RUN chown daemon:daemon -R /usr/local/apache2/cgi-bin
RUN chown daemon:daemon -R /usr/local/apache2/htdocs/export/
