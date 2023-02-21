FROM python:3.9.1-slim-buster

# Copy the rest of the code
WORKDIR /app
ADD requirements.txt /app
ADD app /app/app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT=8000
EXPOSE $PORT

# Run the app
CMD uvicorn app.app:app --host 0.0.0.0 --port $PORT
