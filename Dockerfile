FROM ultralytics/ultralytics

USER $NB_UID

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir shapely lap
