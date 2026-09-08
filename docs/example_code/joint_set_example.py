from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.ColorPicker import ColorType
from rocslope2.PropertyEnums import FisherDistOption, JointOrientationDistributionMethod
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

joint_set = model.getAllJointSets()[0]
joint_set.setName("Primary Joint Set")
joint_set.setColor(ColorType.Rose)
joint_set.setIsJointSetEnabled(True)
joint_set.setJointSpacing(3.75)
joint_set.setTopplingJointLateralLimits(45.5)
joint_set.setSlidingJointLateralLimits(18.25)
joint_set.setSelectedJointOrientationDistributionMethod(JointOrientationDistributionMethod.FISHER)
joint_set.setSelectedFisherDistOptionMethod(FisherDistOption.OPTION_USE_FISHERK)

created_joint = joint_set.createNewIndividualJoint()
print(f"Created individual joint id: {created_joint.id}")
print(f"Joint count: {len(joint_set.getAllIndividualJoints())}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
