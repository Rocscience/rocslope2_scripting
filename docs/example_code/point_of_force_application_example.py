from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.projectSettings.ProjectSettingsEnum import TopplingModel
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

# Point of force application is used with toppling analysis
project_settings = model.getProjectSettings()
project_settings.analysisTab.setIsToppling(True)
project_settings.topplingTab.setSelectedTopplingModelMethod(TopplingModel.BLOCK_FLEXURE_TOPPLING)

point_of_force = model.getPointOfForceApplication()
sliding_block_point = point_of_force.getSlidingBlockPoint()
shearing_block_point = point_of_force.getShearingBlockPoint()
flex_block_point = point_of_force.getFlexBlockPoint()
print(f"Defaults: sliding={sliding_block_point}, shearing={shearing_block_point}, flex={flex_block_point}")

point_of_force.setSlidingBlockPoint(0.82)
point_of_force.setShearingBlockPoint(0.67)
point_of_force.setFlexBlockPoint(0.88)

sliding_block_point = point_of_force.getSlidingBlockPoint()
shearing_block_point = point_of_force.getShearingBlockPoint()
flex_block_point = point_of_force.getFlexBlockPoint()
print(f"Updated: sliding={sliding_block_point}, shearing={shearing_block_point}, flex={flex_block_point}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
