FROM ultralytics/ultralytics

USER $NB_UID

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir shapely lap

# RUN apt-get update && \
#     apt-get install libgl1 -y && \
#     pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# apt-get update && apt-get install libgl1
# apt-get install ffmpeg libsm6 libxext6