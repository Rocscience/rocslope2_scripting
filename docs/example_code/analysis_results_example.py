from rocslope2.RocSlope2Modeler import RocSlope2Modeler
from rocslope2.analysisResults.AnalysisResultsEnum import AnalysisResultsType, ResultColumn
import os
import inspect

current_file = inspect.getfile(lambda: None)
current_dir = os.path.dirname(os.path.abspath(current_file))
example_model = os.path.join(current_dir, "example_models", "blankProject.rocslope2")

RocSlope2Modeler.startApplication()
modeler = RocSlope2Modeler()
model = modeler.openFile(example_model)

analysis = model.getProjectSettings().analysisTab
analysis.setIsWedge(True)
analysis.setIsPlanar(True)
analysis.setIsToppling(True)

model.compute()

results = model.getAnalysisResults()
print(f"Result types: {list(results.keys())}")

wedge = results.getWedgeResults()
print(f"Wedge rows: {len(wedge)}")
print(f"Analysis name: {wedge.analysis_type_name}")

# getValue uses 0-based row position (iloc)
print(f"ID by row index 0: {wedge.getValue(0, ResultColumn.ID)}")
print(f"FS by row index 0: {wedge.getValue(0, ResultColumn.FACTOR_OF_SAFETY)}")

# getValueById uses the Excel-style ID column value (1-based), not row order
first_row_id = wedge.getValue(0, ResultColumn.ID)
print(f"FS by ID {first_row_id}: {wedge.getValueById(first_row_id, ResultColumn.FACTOR_OF_SAFETY)}")

subset = wedge.selectColumns(
    ResultColumn.ID,
    ResultColumn.FACTOR_OF_SAFETY,
)
print(subset.head())

# Fetch a single analysis type
wedge_only = model.getAnalysisResults(AnalysisResultsType.WEDGE)
print(f"Wedge-only types: {list(wedge_only.keys())}")

model.close(saveProject=False)
modeler.closeProgram()
