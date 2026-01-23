FROM python:3.14

WORKDIR /app

# Set pip configuration to avoid threading issues
ENV PIP_PROGRESS_BAR=off
ENV PIP_NO_CACHE_DIR=1

# Install Python packages directly (add/remove packages as needed)
RUN pip install --no-cache-dir --progress-bar off \
    flask \
    requests \
    numpy \
    pandas

# Copy your application code AND templates
COPY sample_app.py .
COPY templates/ templates/

# Run your application
CMD ["python", "sample_app.py"]
