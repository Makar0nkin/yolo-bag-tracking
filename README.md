## Run model
1. Set up environment
    ```
    conda env create --name <env_name> --file=environments.yml 
    conda activate <env_name>
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