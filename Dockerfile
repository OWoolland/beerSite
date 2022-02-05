FROM python:3.8

WORKDIR /

# The enviroment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y npm

WORKDIR /app

COPY app.py app.py
COPY helpers.py helpers.py

COPY database.sqlite database.sqlite

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
