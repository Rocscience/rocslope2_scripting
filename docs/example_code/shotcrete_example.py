from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

shotcrete = model.getShotcrete()
shotcrete.setIsApplied(True)
shotcrete.setThickness(0.25)
shotcrete.setShearStrength(2.5)
shotcrete.setUnitWeight(0.03)

print(f"Shotcrete applied: {shotcrete.getIsApplied()}")
print(f"Thickness: {shotcrete.getThickness()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
