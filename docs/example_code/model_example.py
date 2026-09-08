from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")
save_as_path = os.path.join(current_dir, "example_models", "blankProject_saveAs.rocslope2")
image_path = os.path.join(current_dir, "example_models", "blankProject_export.png")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

joint_set = model.getAllJointSets()[0]
joint_set.setName("Joint Set A")

print(f"Joint set name: {joint_set.getName()}")

model.save()
model.saveAs(
    save_as_path,
    createDirectory=True,
)
model.exportImage(image_path)
model.compute()
print("Model saved, saved-as, image exported, and computed.")
print(f"Save-as path: {save_as_path}")
print(f"Export image path: {image_path}")

model.close(saveProject=False)
modeler.closeProgram()
