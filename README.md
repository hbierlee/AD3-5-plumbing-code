# AD3-5-plumbing-code

- Run the script with python >=3.5, use `--help` for usage manual. 
- In the code, change the parameter `--print-stats` to whatever you use as statistics mode flag (in the assignment it's they use `-p`)
  - The outputted statistics should be of the form: `runtime steps λ`
- Prints progress and the results to stdout
  - results are in a csv format
  - (there are latex ways to use a csv as tabular data, haven't looked into it yet)
- My favourite way to run: `hebi6280@siegbahn:~/Projects/AD3-5/1/AD3-5-plumbing-code$ python3 -u run_experiment.py ../Release/invDes | tee ../experiments/experiment_42.csv`

