from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import BoltOrientation, FaceAppliedTo, BoltPatterns
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "BoltPatternsProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

pattern = model.getAllBoltPatterns()[0]
pattern.setBoltLength(7.0)
pattern.setSelectedOrientationMethod(BoltOrientation.TREND_PLUNGE)
pattern.setTrend(120.0)
pattern.setPlunge(-30.0)
pattern.setSelectedInstallationFaceMethod(FaceAppliedTo.SLOPE_FACE)
pattern.setHorizontalSpacing(1.25)
pattern.setVerticalSpacing(2.5)
pattern.setHorizontalOffset(0.75)
pattern.setVerticalOffset(1.0)
pattern.setSelectedBoltPatternMethod(BoltPatterns.RECTANGLE)

# Create an additional pattern linked to an existing bolt property
new_pattern = model.addBoltPattern()
new_pattern.setBoltLength(5.0)

print(f"Bolt pattern count: {len(model.getAllBoltPatterns())}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
