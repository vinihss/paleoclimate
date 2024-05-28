FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "paleoclimate-backend", "/bin/bash", "-c"]

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./scripts/start.sh

CMD ["conda", "run", "--no-capture-output", "-n", "paleoclimate-backend", "./scripts/start.sh"]