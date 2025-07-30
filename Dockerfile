FROM python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    libopenmpi-dev \
    libopenmpi3 \
    openmpi-bin \
    openmpi-common \
    openmpi-doc \
    libgsl-dev \
    libopenblas-dev

RUN pip install --upgrade pip
RUN pip install Cython==3.0.6

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install Gpy

# Create a non-root user to make mpirun happy
RUN useradd -ms /bin/bash myuser
USER myuser
COPY . .
CMD [ "mpirun", "python", "test.py"]
