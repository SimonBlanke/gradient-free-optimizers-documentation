# Search





## Parameters

### `objective_function`

- **type:** `callable`

The objective function defines the optimization problem. The optimization algorithm will try to maximize the numerical value that is returned by the objective function by trying out different parameters from the search space.

example:
```python
def objective_function(para):
    score = -(para["x1"] * para["x1"] + para["x2"] * para["x2"])
    return score
```

### `n_iter`

- **type:** `int`

The number of iterations that will be performed during the optimiation run. The entire iteration consists of the optimization-step, which decides the next parameter that will be evaluated and the evaluation-step, which will run the objective function with the chosen parameter and return the score.

### `max_time`

- **type:** `float`, `None`
- **default:** `None`

Maximum number of seconds until the optimization stops. The time will be checked after each completed iteration.

### `max_score`

- **type:** `float`, `None`
- **default:** `None`

Maximum score until the optimization stops. The score will be checked after each completed iteration.


### `early_stopping`

- **type:** `dict`, `None`
- **default:** `None`

Stops the optimization run early if it did not achive any score-improvement within the last iterations. The early_stopping-parameter enables to set three parameters:

- `n_iter_no_change`: Non-optional int-parameter. This marks the last n iterations to look for an improvement over the iterations that came before n. If the best score of the entire run is within those last n iterations the run will continue (until other stopping criteria are met), otherwise the run will stop.

- `tol_abs`: Optional float-paramter. The score must have improved at least this absolute tolerance in the last n iterations over the best score in the iterations before n. This is an absolute value, so 0.1 means an imporvement of 0.8 -> 0.9 is acceptable but 0.81 -> 0.9 would stop the run.

- `tol_rel`: Optional float-paramter. The score must have imporved at least this relative tolerance (in percentage) in the last n iterations over the best score in the iterations before n. This is a relative value, so 10 means an imporvement of 0.8 -> 0.88 is acceptable but 0.8 -> 0.87 would stop the run.

  

### `memory`

- **type:** `bool`
- **default:** `True`

Whether or not to use the "memory"-feature. The memory is a dictionary, which gets filled with parameters and scores during the optimization run. If the optimizer encounters a parameter that is already in the dictionary it just extracts the score instead of reevaluating the objective function (which can take a long time).


### `memory_warm_start`

- **type:** `dataframe`, `None`
- **default:** `None`

Pandas dataframe that contains score and paramter information that will be automatically loaded into the memory-dictionary.

example:

<table class="table">
<thead class="table-head">
    <tr class="row">
    <td class="cell">score</td>
    <td class="cell">x1</td>
    <td class="cell">x2</td>
    <td class="cell">x...</td>
    </tr>
</thead>
<tbody class="table-body">
    <tr class="row">
    <td class="cell">0.756</td>
    <td class="cell">0.1</td>
    <td class="cell">0.2</td>
    <td class="cell">...</td>
    </tr>
    <tr class="row">
    <td class="cell">0.823</td>
    <td class="cell">0.3</td>
    <td class="cell">0.1</td>
    <td class="cell">...</td>
    </tr>
    <tr class="row">
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    </tr>
    <tr class="row">
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    </tr>
</tbody>
</table>


### `verbosity`

- **type:** `list`, `False`
- **default:** `["progress_bar", "print_results", "print_times"]`

The verbosity list determines what part of the optimization information will be printed in the command line.