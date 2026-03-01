# Use official Python slim image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping && \
    chmod u+s /usr/bin/ping && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# --- Layer Kesulitan: Flag Labyrinth ---
# Membuat folder root jebakan
RUN mkdir -p /ada-flag-di-sini/disini \
             /ada-flag-di-sini/disana/maybe \
             /ada-flag-di-sini/disana/flag \
             /ada-flag-di-sini/disitu

# File jebakan di root folder target
RUN echo "semangat yhh. bukan di sini" > /ada-flag-di-sini/fake_flag.txt

# File ledekan di subfolder
RUN echo "lmaoo, bukan di sini. keep digging!" > /ada-flag-di-sini/disini/flag345.txt && \
    echo "lmaoo, bukan di sini juga. keep digging!" > /ada-flag-di-sini/disana/flagyyyy98989.txt && \
    echo "lmaoo, bukan di sini juga. keep digging!" > /ada-flag-di-sini/disitu/flag123.txt

# File passwd palsu berisi ejekan
RUN echo "root:x:0:0:root:/root:/bin/bash\nuser:x:1000:1000:user:/home/user:/bin/sh\nPRO TIP: The flag is NOT here. Stop reading system files and find the real path!" > /ada-flag-di-sini/disana/flag/passwd

# FLAG ASLI (Sembunyi di folder maybe/)
RUN echo "inkubasi26{0S_CMD_1NJ_W1TH_4NN0Y1NG_L4BYR1NTH_1337}" > /ada-flag-di-sini/disana/maybe/flag_asli.txt

# Set permissions agar semua file bisa dibaca oleh user non-root
RUN chmod -R 755 /ada-flag-di-sini
# ---------------------------------------

# Run as non-root user
RUN useradd -m zenc
USER zenc

# Expose the port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

