from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")
dips_results = os.path.join(current_dir, "example_models", "DipsResults Sample.dipsresults")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

import_from_dips = model.getImportFromDips()
target_joint_set = model.getAllJointSets()[0]

# Import grid orientations into an existing joint set
import_from_dips.importGridDataToJointSet(
    dips_results,
    target_joint_set,
    overwriteExistingOrientations=False,
)

# Or preserve Dips joint-set grouping while importing
import_from_dips.importGridDataPreservingDipsJointSets(
    dips_results,
    overwriteExistingSets=False,
    importUncategorizedJointSets=True,
)

joint_sets = model.getAllJointSets()
joint_count = len(joint_sets)
joints_in_first_set = len(joint_sets[0].getAllIndividualJoints())
print(f"Joint set count: {joint_count}")
print(f"Joints in first set: {joints_in_first_set}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
