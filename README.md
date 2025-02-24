## Run model

### Docker
1. Run container
    ```
    docker compose up -d
    ```
2. Go to bash
    ```
    docker exec -it yolo-bag-tracking-app-1 /bin/bash
    ```
2. Run
    - train model
        ```
        python train.py
        ```
    - track and count objects (by default: input folder = video\input, output folder = video\output)
        ```
        python track.py -i <input folder> -o <output folder>
        ```

### Python
1. Set up environment with python 3.10.16
    ```
    python -m venv venv
    venv\Scripts\activate
    python install -r requirements.txt
    ```
2. Run
    - train model
        ```
        python train.py
        ```
    - track and count objects (by default: input folder = video\input, output folder = video\output)
        ```
        python track.py -i <input folder> -o <output folder>
        ```

In case of throwing error in `train.py` about wrong dataset directory change `settings.json`:
```
{
    ...
    "datasets_dir": "datasets",
    ...
}
```


## Update environment data 
```
pip freeze > requirements.txt
```