# train the model and saving model and scaler
FROM python:3.10 AS model_training

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/model_training.py .
RUN python model_training.py

# predictions
FROM python:3.10 AS serving
WORKDIR /app

# coping trained model and scaler
COPY --from=model_training /app/my_model.keras .
COPY --from=model_training /app/scaler.pkl .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/main.py .
COPY src/templates ./templates
COPY src/statics   ./statics

EXPOSE 5000

CMD ["python", "main.py"]