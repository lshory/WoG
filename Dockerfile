FROM python:3.8-slim
COPY . /app/ 
WORKDIR /app/
COPY ./Scores.txt /app/
RUN pip install Flask
EXPOSE 8777
CMD python3 MainScores.py
