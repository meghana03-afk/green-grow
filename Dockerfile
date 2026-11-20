# Use the official Python 3.10 image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first and install dependencies
# This helps Docker cache the installed libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Tell Hugging Face that your app runs on port 7860
# This is the port they expect
ENV PORT=7860

# The command to run your Flask app using Gunicorn
# This is a production web server, not the 'flask run' development server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]