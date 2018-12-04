FROM gcr.io/google_appengine/python

RUN virtualenv /env -p python3.5

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
CMD uwsgi '/app/uwsgi/dev.ini'