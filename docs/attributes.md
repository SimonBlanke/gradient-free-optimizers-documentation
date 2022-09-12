# Attributes

## `search_data`

- **return type:** `pandas dataframe`

Dataframe containing information about the score and the value of each parameter. Each row shows the information of one optimization iteration.

example:

|  x1 | x2  | score  |  
|---|---|---|
|  5 |  15 |  0.3 |  
|  10 | 12  |  0.7 |  
| ...  |  ... |  ... |  
| ...  |  ... |  ... |  


## `best_score`

- **return type:** `float`

Numerical value of the best score, that was found during the optimization run.

## `best_para`

- **return type:** `dict`

Parameter dictionary of the best score, that was found during the optimization run.

## `eval_times`

- **return type:** `list`

List of evaluation times (time of objective function evaluation) collected during the optimization run.

## `iter_times`

- **return type:** `list`

List of iteration times (evaluation + optimization) collected during the optimization run.