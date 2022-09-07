# Attributes

## `search_data`

- **type:** `dataframe`

Dataframe containing information about the score and the value of each parameter. Each row shows the information of one optimization iteration.

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


## `best_score`

- **type:** `float`

numerical value of the best score, that was found during the optimization run.

## `best_para`

- **type:** `dict`

parameter dictionary of the best score, that was found during the optimization run.

## `eval_times`

- **type:** `list`

List of evaluation times (time of objective function evaluation) collected during the optimization run.

## `iter_times`

- **type:** `list`

List of iteration times (evaluation + optimization) collected during the optimization run.