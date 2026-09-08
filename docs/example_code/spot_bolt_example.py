from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import BoltOrientation, FaceAppliedTo, SpotBoltInstallationFace
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

spot_bolt = model.addSpotBolt(SpotBoltInstallationFace.SLOPE_FACE)
spot_bolt.setBoltLength(12.5)
spot_bolt.setSelectedOrientationMethod(BoltOrientation.TREND_PLUNGE)
spot_bolt.setTrend(120.0)
spot_bolt.setPlunge(-30.0)
spot_bolt.setBoltProperties(model.getAllBoltProperties()[0])
spot_bolt.setSelectedInstallationFaceMethod(FaceAppliedTo.UPPER_FACE)

print(f"Length: {spot_bolt.getBoltLength()}")
print(f"Orientation: {spot_bolt.getSelectedOrientationMethod()}")
print(f"Trend/plunge: {spot_bolt.getTrend()}, {spot_bolt.getPlunge()}")
print(f"Face: {spot_bolt.getSelectedInstallationFaceMethod()}")
print(f"Spot bolt count: {len(model.getAllSpotBolts())}")

model.deleteSpotBolt(spot_bolt)
print(f"Spot bolt count after delete: {len(model.getAllSpotBolts())}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
