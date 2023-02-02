FROM python:3.8-slim
WORKDIR /app
COPY ./Scores.txt /app/
RUN pip install Flask
EXPOSE 8080
CMD python MainScores.py
