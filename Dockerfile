# Build
FROM python:3.13 AS builder  
# Create the app directory
RUN mkdir /app
# Set the working directory inside the container
WORKDIR /app
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
# Upgrade pip
RUN pip install --upgrade pip 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Production
FROM python:3.13 

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app
# Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
# set working directory
WORKDIR /app
# Copy application code
COPY --chown=appuser:appuser . .
# Set python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
# switch user so not operating as root
USER appuser
# Expose the Django port
EXPOSE 8000
# Run Django’s development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "chiptuner_site.wsgi:application"]
