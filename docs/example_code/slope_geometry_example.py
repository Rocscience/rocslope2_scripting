from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import FisherDistOption, JointOrientationDistributionMethod
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

slope_geometry = model.getSlopeGeometry()
slope_geometry.setOriginPoint((0.0, 0.0, 0.0))
slope_geometry.setSlopeDip(55.5)
slope_geometry.setSlopeDipDirection(270.0)
slope_geometry.setSlopeHeight(42.25)
slope_geometry.setSlopeLength(88.75)
slope_geometry.setIsOverhanging(False)
slope_geometry.setIsDefineSlopeLength(True)

slope_geometry.setUpperFaceDip(12.5)
slope_geometry.setUpperFaceDipDirection(95.0)
slope_geometry.setUpperFaceBenchWidth(6.25)

slope_geometry.setIsTensionCrackExists(True)
slope_geometry.setTensionCrackDip(60.0)
slope_geometry.setTensionCrackDipDirection(200.0)
slope_geometry.setTensionCrackDistanceFromCrest(3.5)
slope_geometry.setSelectedTC_OrientationDistributionMethod(JointOrientationDistributionMethod.FISHER)
slope_geometry.setSelectedTC_FisherDistOptionMethod(FisherDistOption.OPTION_USE_FISHERK)
slope_geometry.setTC_FisherDist_FisherK(80.0)

print(f"Slope dip: {slope_geometry.getSlopeDip()}")
print(f"Slope height: {slope_geometry.getSlopeHeight()}")
print(f"Tension crack exists: {slope_geometry.getIsTensionCrackExists()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
