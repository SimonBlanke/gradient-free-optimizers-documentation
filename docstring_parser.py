import os
import re


from gradient_free_optimizers import (
    HillClimbingOptimizer,
    StochasticHillClimbingOptimizer,
    RepulsingHillClimbingOptimizer,
    SimulatedAnnealingOptimizer,
    DownhillSimplexOptimizer,
    RandomSearchOptimizer,
    PowellsMethod,
    GridSearchOptimizer,
    RandomRestartHillClimbingOptimizer,
    RandomAnnealingOptimizer,
    PatternSearch,
    DirectAlgorithm,
    ParallelTemperingOptimizer,
    ParticleSwarmOptimizer,
    SpiralOptimization,
    GeneticAlgorithmOptimizer,
    EvolutionStrategyOptimizer,
    DifferentialEvolutionOptimizer,
    LipschitzOptimizer,
    BayesianOptimizer,
    TreeStructuredParzenEstimators,
)


def generate_markdown_files(name, docstring):
    # Get the current script's directory
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Create directories
    dir_path = os.path.join(base_path, "docs", "optimizers", name)
    param_dir = os.path.join(dir_path, "parameters")
    os.makedirs(param_dir, exist_ok=True)

    # Split the docstring into lines
    lines = docstring.strip().split("\n")
    lines = [line.strip() for line in lines]

    # Extract the title and description
    title = lines[0].strip("**").strip()

    try:
        param_index = lines.index("Parameters")
    except ValueError:
        raise ValueError(
            "The docstring does not contain a 'Parameters' section."
        )

    description = "\n".join(lines[1:param_index]).strip()

    # Create the title markdown file
    title_file_path = os.path.join(dir_path, f"{name}.md")
    with open(title_file_path, "w") as title_file:
        title_file.write(f"# {title}\n\n")
        title_file.write(f"{description}\n")
    print(f"Generated: {title_file_path}")

    # Extract the parameters section
    if param_index + 1 < len(lines):
        param_lines = lines[param_index + 2 :]
    else:
        param_lines = []

    # Process parameters
    current_param = []
    for line in param_lines:
        if re.match(r"^\s*\w+\s*:\s*\S+", line):  # Parameter name with type
            if current_param:  # Save the previous parameter block
                save_parameter_file(param_dir, current_param)
            current_param = [line.strip()]
        else:
            current_param.append(line.strip())

    # Save the last parameter
    if current_param:
        save_parameter_file(param_dir, current_param)


def save_parameter_file(param_dir, param_lines):
    """Helper function to save individual parameter markdown files."""
    # Extract parameter name and type
    param_header = param_lines[0].split(":", 1)
    param_name = param_header[0].strip()
    param_type = param_header[1].strip() if len(param_header) > 1 else "Unknown"

    # Extract parameter description with proper indentation
    param_description = "\n".join(
        line.strip() for line in param_lines[1:]
    ).strip()

    # Write parameter markdown file
    param_file_path = os.path.join(param_dir, f"{param_name}.md")
    with open(param_file_path, "w") as param_file:
        param_file.write(f"# {param_name}\n\n")
        param_file.write(f"**Type**: {param_type}\n\n")
        param_file.write(param_description)
    print(f"Generated: {param_file_path}")


optimizers = [
    HillClimbingOptimizer,
    StochasticHillClimbingOptimizer,
    RepulsingHillClimbingOptimizer,
    SimulatedAnnealingOptimizer,
    DownhillSimplexOptimizer,
    RandomSearchOptimizer,
    PowellsMethod,
    GridSearchOptimizer,
    RandomRestartHillClimbingOptimizer,
    RandomAnnealingOptimizer,
    PatternSearch,
    DirectAlgorithm,
    ParallelTemperingOptimizer,
    ParticleSwarmOptimizer,
    SpiralOptimization,
    GeneticAlgorithmOptimizer,
    EvolutionStrategyOptimizer,
    DifferentialEvolutionOptimizer,
    LipschitzOptimizer,
    BayesianOptimizer,
    TreeStructuredParzenEstimators,
]

for optimizer in optimizers:
    generate_markdown_files(optimizer._name_, optimizer.__doc__)
