from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import ActiveApplicationType, BoltOrientationEfficiencyType, BoltType
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

bolt = model.addBoltProperty("Script Bolt")

simple_bolt_force = bolt.setCurrentSupportType(BoltType.SIMPLE_BOLT_FORCE)
simple_bolt_force.setSelectedActiveApplicationMethod(ActiveApplicationType.PASSIVE)
simple_bolt_force.setForce(1.25)

mechanically_anchored_bolt = bolt.setCurrentSupportType(BoltType.MECHANICALLY_ANCHORED)
mechanically_anchored_bolt.setTensileCapacity(0.5)
mechanically_anchored_bolt.setPlateCapacity(0.4)
mechanically_anchored_bolt.setAnchorCapacity(0.3)
mechanically_anchored_bolt.setIsUseShearCapacity(True)
mechanically_anchored_bolt.setShearCapacity(0.2)
mechanically_anchored_bolt.setIsUseBoltOrientationEfficiency(True)
mechanically_anchored_bolt.setSelectedBoltOrientationEfficiencyMethod(BoltOrientationEfficiencyType.LINEAR_TENSIONSHEAR)

bolt_property_names = [bolt_property.getName() for bolt_property in model.getAllBoltProperties()]
print(f"Bolt properties: {bolt_property_names}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
