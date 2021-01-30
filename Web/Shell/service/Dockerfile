FROM fauria/lamp

# copy the files over
COPY www/src /var/www/html/
COPY /www/flag.txt /home/flag.txt
COPY /www/apache2.conf /etc/apache2/apache2.conf
COPY --chown=www-data /www/uploads /var/www/html/uploads
RUN chmod 755 /var/www/html/*

CMD /usr/sbin/apache2ctl -D FOREGROUND

