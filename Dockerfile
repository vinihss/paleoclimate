FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "paleoclimate", "/bin/bash", "-c"]

COPY . .

RUN chmod +x ./scripts/start.sh

CMD ["conda", "run", "--no-capture-output", "-n", "paleoclimate", "./scripts/start.sh", './scripts/run_quality_tools.sh']
