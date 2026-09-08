from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.seismicLoading import SeismicDirection
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

seismic = model.getSeismicLoading()
print(f"Default direction: {seismic.getCurrentDirection().direction}")

trend_plunge = seismic.setCurrentDirection(SeismicDirection.TREND_PLUNGE)
trend_plunge.setTrend(180.0)
trend_plunge.setPlunge(10.0)
trend_plunge.setCoefficient(0.2)
print(f"Trend/plunge/coeff: {trend_plunge.getTrend()}, {trend_plunge.getPlunge()}, {trend_plunge.getCoefficient()}")

vector = seismic.setCurrentDirection(SeismicDirection.VECTOR)
vector.setX(1.0)
vector.setY(0.5)
vector.setZ(-0.25)
vector.setCoefficient(0.3)
print(f"Vector XYZ/coeff: {vector.getX()}, {vector.getY()}, {vector.getZ()}, {vector.getCoefficient()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
