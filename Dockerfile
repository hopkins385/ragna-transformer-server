FROM python:3.13

# Install system dependencies required for sentencepiece
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    build-essential \
    pkg-config \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Download the latest installer script for uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the uv installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Copy the application into the container.
COPY . /server

# Install the application dependencies.
WORKDIR /server
RUN uv sync --frozen --no-cache

EXPOSE 3030

CMD ["uv", "run", "app/main.py"]