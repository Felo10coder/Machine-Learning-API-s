FROM python:3.10.11
COPY requirement.txt /tmp/requirement.txt
RUN python -m pip install -r /tmp/requirement.txt
COPY . /app
WORKDIR /app
EXPOSE 8501
CMD ["streamlit","run","home_page.py","--server.port=8501"]