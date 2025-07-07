FROM ghcr.io/swalia-proj/secure-base:latest

WORKDIR /app

# Copy only what's needed first (for better caching)
COPY requirements.txt ./

# Install Python deps using requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Now copy the app code
COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
