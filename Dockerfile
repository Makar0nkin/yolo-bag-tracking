FROM ultralytics/ultralytics

USER $NB_UID

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir shapely lap && \
    pip install --no-cache-dir numpy==2.0.0 --upgrade
