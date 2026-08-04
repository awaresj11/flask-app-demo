#this flask-app dockerfile 
#Base image
FROM python:3.11

WORKDIR /app

#code copy
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

#To run app
#CMD["python", "app.py"]
CMD ["python", "app.py"]
