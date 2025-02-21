## Run model
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


## Update environment data 
```
conda env export > environment.yml
```