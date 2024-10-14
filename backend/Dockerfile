# Base image using Miniconda for Python
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy the environment file and install dependencies
COPY environment.yml .

# Install Conda environment (paleoclimate)
RUN conda env create -f environment.yml

# Activate the environment and ensure bash is the shell
SHELL ["conda", "run", "-n", "paleoclimate", "/bin/bash", "-c"]

# Copy all source code
COPY . .

# Expose port 8002 for the FastAPI app
EXPOSE 8002

# Use the start script to run Uvicorn (with hot reload during development)
CMD ["./scripts/start.sh"]
