from rocslope2.RocSlope2Modeler import RocSlope2Modeler
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
swedge_sample = os.path.join(current_dir, "..", "..", "tests", "resources", "Swedge Sample.swd7")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()

# Create a new blank project
new_model = modeler.newProject()
print(f"Created new project id: {new_model.project_id}")
new_model.close(saveProject=False)

# Import a legacy Swedge / RocPlane / RocTopple file
imported_model = modeler.importFile(swedge_sample)
print(f"Imported project id: {imported_model.project_id}")
imported_model.close(saveProject=False)

modeler.closeProgram()
