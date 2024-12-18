from odbAccess import *
from abaqusConstants import *
from odbAccess import openOdb

# Get the ODB object
my_odb = openOdb(r"Y:/331589-case9_modaldynamics.inp/case9_modaldynamics.odb")

# Get the specified analysis step
step = my_odb.steps['Step-3']

# Get displacements for all increments
all_displacements = [frame.fieldOutputs['U'] for frame in step.frames]

# Specify the node label to extract
node_labels = (5203,)

# Define a set named 'set_for_datas' in PART-1-1 containing the specified node
node_set = my_odb.rootAssembly.instances['PART-1-1'].NodeSetFromNodeLabels(
    name='set_for_datas_case9', nodeLabels=node_labels
)

# Generate a txt file and write the extracted results
with open('data_case9.csv', 'w') as f:
    f.write("Increment, NodeLabel, U3\n")
    for i, dis_field in enumerate(all_displacements):
        local_dis_values = dis_field.getSubset(region=node_set)
        for node_value in local_dis_values.values:
            txt_line = "{}, {}, {}\n".format(i, node_value.nodeLabel, node_value.data[2])
            f.write(txt_line)
