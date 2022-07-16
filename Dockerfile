FROM python:slim
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./conf.ini ./conf.ini
COPY ./DLHT_api.py ./DLHT_api.py
COPY ./DLHT_config.py ./DLHT_config.py
COPY ./DLHT_db.py ./DLHT_db.py
COPY ./DLHT_main.py ./DLHT_main.py
COPY ./DLHT_plot.py ./DLHT_plot.py
CMD ["python3", "DLHT_main.py"]