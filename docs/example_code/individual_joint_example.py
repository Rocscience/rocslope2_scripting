from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

joint_set = model.getAllJointSets()[0]
individual_joint = joint_set.getAllIndividualJoints()[0]

individual_joint.setDip(55.5)
individual_joint.setDipDirection(270.0)
individual_joint.setFisherK(12.5)
individual_joint.setFisherStDv(4.25)

print(f"Dip: {individual_joint.getDip()}")
print(f"Dip direction: {individual_joint.getDipDirection()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
