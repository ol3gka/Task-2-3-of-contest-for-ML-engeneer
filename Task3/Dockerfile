FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y install git
#COPY ./script.sh
#COPY ./ex.txt
#CMD ["bash script.sh"]
CMD ["echo","Hi User"]
RUN git clone https://github.com/ol3gka/Tools.git
RUN cd Tools/ \
	#&& cat ex.txt \
	&& chmod +x script1.sh \
	&& chmod +x script2.sh
