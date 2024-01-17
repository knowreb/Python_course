# We strat with some design to be printed
unprinted_designs = ['phone case', 'robot pendant', 'icosahedron']
completed_models = []

#We stimulate the printinh of individual projects as long as there is any project left on the list.
#Each printed model is transferred to the completed_models list.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing out the model: {current_design}")
    completed_models.append(current_design)

# Display of all printed models
print("\nThe following models were printed: ")
for completed_model in completed_models:
    print(completed_model)

#Reorganisation of the code by creating two functions
def print_models(unprinted_designs, completed_models):
    """We stimulate the printing of individual projects as long as there is any project left on the list.
    Each printed model is transferred to the complited_model list."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    print(f"\nPrinting out of the model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Displays all models that have been printed"""
    print("\nModels were printed: ")
    for completed_models in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'icosahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

