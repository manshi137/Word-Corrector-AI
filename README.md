# Word-Corrector-AI
## Pre Requisites
1. Python 3.7
2. Conda Environment
  Set-up using :    https://docs.conda.io/en/latest/miniconda.html
3. Set environment variables using :    conda env create -f environment.yml
## Running the implementation
  python run.py -src data/input.txt -tar data/pred.txt -tm 2
This command will run your solution for each string in the data/input.txt file and write the solutions to data/pred.txt. For each input sentence, your program is allowed to run for at most 2 seconds (as specified by the -tm option). You may experiment with this parameter.
