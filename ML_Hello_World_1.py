
#Create a python file named hello.py and save it in a folder named src:


# src/hello.py
print("Hello world!")



#Creating a control script, this allows us to run a script on different computers.
#Plus, the control script will control how and where the machine learning code is run.#Plus, the control script will control how and where the machine learning code is run.


# run-hello.py
from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name='day1-experiment-hello')

config = ScriptRunConfig(source_directory='./src', script='hello.py', compute_target='cpu-cluster')  #compute cluster

run = experiment.submit(config)
aml_url = run.get_portal_url()
print(aml_url)


