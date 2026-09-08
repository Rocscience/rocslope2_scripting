from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.ColorPicker import ColorType
from rocslope2.PropertyEnums import JointStrengthType, JointRandomVariables
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

joint_properties = model.addJointProperty("Script Joint Property")
joint_properties.setName("Script Joint Property")
joint_properties.setColor(ColorType.Gold)

strength = joint_properties.strengthTab
strength.setSelectedStrengthTypeMethod(JointStrengthType.MOHR_COULOMB)
strength.setSelectedRandomVariablesMethod(JointRandomVariables.PARAMETERS)
strength.setWaviness(5.0)
strength.setCohesion(0.05)
strength.setPhi(35.0)
strength.setTensileStrength(0.01)

joint_property_names = [joint_property.getName() for joint_property in model.getAllJointProperties()]
print(f"Joint properties: {joint_property_names}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
