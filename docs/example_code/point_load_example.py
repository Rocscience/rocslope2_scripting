from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.pointLoad.PointLoadEnum import ApplyTo, LoadAction, LoadEffect
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

print(f"Point loads before: {len(model.getAllPointLoads())}")

point_load = model.addPointLoad()
point_load.setTrend(180.0)
point_load.setPlunge(45.0)
point_load.setForceMagnitude(25.5)
point_load.setSelectedApplyToMethod(ApplyTo.SLOPE)
point_load.setHeightBelowCrest(12.0)

# Load action/effect require a design standard other than "None"
design_standard_tab = model.getProjectSettings().designStandardTab
design_standards = design_standard_tab.getDesignStandards()
enabled_design_standard = design_standards[1]
design_standard_tab.setSelectedDesignStandardMethod(enabled_design_standard)
point_load.setSelectedLoadActionMethod(LoadAction.PERMANENT)
point_load.setSelectedLoadEffectMethod(LoadEffect.UNFAVOURABLE)

print(f"Trend: {point_load.getTrend()}")
print(f"Plunge: {point_load.getPlunge()}")
print(f"Force magnitude: {point_load.getForceMagnitude()}")
print(f"Apply to: {point_load.getSelectedApplyToMethod()}")
print(f"Point loads after add: {len(model.getAllPointLoads())}")

model.deletePointLoad(point_load)
print(f"Point loads after delete: {len(model.getAllPointLoads())}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
