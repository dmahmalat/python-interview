# Entrypoint file when the package is run with the -m flag from the command line
from . import interview_refactor, interview_coding_functions

print("RUNNING INTERVIEW REFACTOR:")
interview_refactor.main()

print("\n-----------------------------------")
print("RUNNING INTERVIEW CODING FUNCTIONS:")
interview_coding_functions.main()
