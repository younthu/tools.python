FROM python:3.10-bullseye
 
# Create app directory
WORKDIR /app
 
RUN apt-get update && apt-get install -y python3-opencv

# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]