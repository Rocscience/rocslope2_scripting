from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.projectSettings.ProjectSettingsEnum import AnalysisType
from rocslope2.individualJoint.IndividualJoint import StatsDistributionProperty
import rocslope2.generatedPythonFiles.CommonMessages_pb2 as CommonMessages_pb2
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

# Probabilistic analysis is required before editing statistical distributions
statistics = model.getProjectSettings().statisticsTab
statistics.setSelectedAnalysisTypeMethod(AnalysisType.PROBABILISTIC)

joint_set = model.getAllJointSets()[0]
individual_joint = joint_set.getAllIndividualJoints()[0]

dip_stats = individual_joint.getStatsDistribution(StatsDistributionProperty.dipStats)
dip_stats.setMean(55.5)
dip_stats.setDistType(CommonMessages_pb2.STATISTICS_NORMAL)
dip_stats.setStdv(3.0)
dip_stats.setRelMin(9.0)
dip_stats.setRelMax(9.0)

print(f"Dip mean: {dip_stats.getMean()}")
print(f"Dip stdv: {dip_stats.getStdv()}")
print(f"Dip distribution: {dip_stats.getDistType()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
