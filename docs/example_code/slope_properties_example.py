from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import GroundwaterMethod
from rocslope2.projectSettings.ProjectSettingsEnum import TopplingModel
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

# Enable flexure toppling so shear strength inputs are available
project_settings = model.getProjectSettings()
project_settings.analysisTab.setIsToppling(True)
project_settings.topplingTab.setSelectedTopplingModelMethod(TopplingModel.BLOCK_FLEXURE_TOPPLING)

slope_properties = model.getSlopeProperties()

material_strength = slope_properties.materialStrengthTab
material_strength.setUnitWeight(0.028)
material_strength.setFrictionAngle(40.0)
material_strength.setCohesion(0.05)
material_strength.setTensileStrength(0.01)

water_parameters = slope_properties.waterParametersTab
water_parameters.setSelectedGroundwaterMethod(GroundwaterMethod.ELEVATION)
water_parameters.setGroundwaterElevation(10.0)

print(f"Friction angle: {material_strength.getFrictionAngle()}")
print(f"Cohesion: {material_strength.getCohesion()}")
print(f"Groundwater method: {water_parameters.getSelectedGroundwaterMethod()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
