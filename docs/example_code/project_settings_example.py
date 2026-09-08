from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.PropertyEnums import UnitSystem, SamplingMethod
from rocslope2.projectSettings.ProjectSettingsEnum import (
    OrientationDefinition,
    BlockShape,
    BlockGeneration,
    TopplingModel,
    AnalysisType,
    PseudoRandomNumberGeneration,
)
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

project_settings = model.getProjectSettings()

project_settings.unitsTab.setSelectedUnitSystemMethod(UnitSystem.RFC_METRIC_MPA)

analysis = project_settings.analysisTab
analysis.setDesignFactorOfSafety(1.5)
analysis.setIsWedge(True)
analysis.setIsPlanar(True)
analysis.setIsToppling(True)
analysis.setSelectedOrientationDefinitionMethod(OrientationDefinition.USE_TRUE_DIP)

wedge = project_settings.wedgeTab
wedge.setSelectedBlockShapeMethod(BlockShape.WEDGE)
wedge.setIsIncludeSocketWedges(False)

toppling = project_settings.topplingTab
toppling.setSelectedBlockGenerationMethod(BlockGeneration.EQUAL_AREA)
toppling.setSelectedTopplingModelMethod(TopplingModel.BLOCK_TOPPLING)

statistics = project_settings.statisticsTab
statistics.setSelectedAnalysisTypeMethod(AnalysisType.DETERMINISTIC)
statistics.setSelectedSamplingMethod(SamplingMethod.LATIN_HYPERCUBE)
statistics.setNumberOfSamples(1000)
statistics.setSelectedPseudoRandomNumberGenerationMethod(PseudoRandomNumberGeneration.CONSTANT_SEED_VALUE)

print(f"Unit system: {project_settings.unitsTab.getSelectedUnitSystemMethod()}")
print(f"Design FoS: {analysis.getDesignFactorOfSafety()}")
print(f"Analysis type: {statistics.getSelectedAnalysisTypeMethod()}")

model.save()
model.close(saveProject=False)
modeler.closeProgram()
