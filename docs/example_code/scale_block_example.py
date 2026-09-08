from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

wedge_blocks = model.getScaleWedgeBlocks()
wedge_blocks.setIsApplyScalingWedgeVolume(True)
wedge_blocks.setScalingValueWedgeVolume(100.0)
wedge_blocks.setIsApplyScalingTraceLengthJoint1(True)
wedge_blocks.setScalingValueTraceLengthJoint1(50.0)

planar_blocks = model.getScalePlanarBlocks()
planar_blocks.setIsApplyScalingWedgeVolume(True)
planar_blocks.setScalingValueWedgeVolume(75.0)

print(f"Wedge volume scaling applied: {wedge_blocks.getIsApplyScalingWedgeVolume()}")
print(f"Wedge volume scaling value: {wedge_blocks.getScalingValueWedgeVolume()}")
print(f"Planar volume scaling value: {planar_blocks.getScalingValueWedgeVolume()}")

# Maximize scaled blocks after configuring limits
wedge_blocks.maximize()
print("Maximize completed.")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
