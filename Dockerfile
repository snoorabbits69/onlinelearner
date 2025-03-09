FROM python:3.12.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Clear all pip caches thoroughly
RUN pip cache purge
RUN rm -rf /root/.cache/pip
RUN pip install --upgrade pip

# Copy requirements file first for caching
COPY requirements.txt .

# Install dependencies with a clean environment
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

# Copy the rest of the application code
COPY . .