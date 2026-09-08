from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.loading.PressureLoadingEnum import PressureModel
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

pressure_loading = model.getPressureLoading()

pressure_loading.setIsSlopeFaceEnabled(True)
pressure_loading.setSlopeFaceTrend(180.0)
pressure_loading.setSlopeFacePlunge(45.0)
pressure_loading.setSlopeFacePressure(25.5)
pressure_loading.setSelectedSlopeFaceModelMethod(PressureModel.ACTIVE)

pressure_loading.setIsUpperSlopeFaceEnabled(True)
pressure_loading.setUpperSlopeFaceTrend(90.0)
pressure_loading.setUpperSlopeFacePlunge(-30.0)
pressure_loading.setUpperSlopeFacePressure(12.0)
pressure_loading.setSelectedUpperSlopeFaceModelMethod(PressureModel.PASSIVE)

print(f"Slope face enabled: {pressure_loading.getIsSlopeFaceEnabled()}")
print(f"Slope face pressure: {pressure_loading.getSlopeFacePressure()}")
print(f"Upper face pressure: {pressure_loading.getUpperSlopeFacePressure()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
