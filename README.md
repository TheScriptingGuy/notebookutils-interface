# notebookutils-interface
Provides implementations and interfaces upon the dummy notebook utils from Microsoft in Synapse Analytics and Fabric to support local development with notebookutils

Based on the dummy-notebookutils from pypi: https://pypi.org/project/dummy-notebookutils/ and aims to add functionality to run in a local development environment.

## Sample usage
```python
from notebookutils import mssparkutils

files = mssparkutils.fs.ls("notebookutils/")

print(files)
```

Output of the sample:
[FileInfo(path=notebookutils/credentials.py, name=credentials.py, size=212), FileInfo(path=notebookutils/fabricClient.py, name=fabricClient.py, size=309), FileInfo(path=notebookutils/fs.py, name=fs.py, size=1004), FileInfo(path=notebookutils/lakehouse.py, name=lakehouse.py, size=654), FileInfo(path=notebookutils/mssparkutils, name=mssparkutils, size=None), FileInfo(path=notebookutils/notebook.py, name=notebook.py, size=681), FileInfo(path=notebookutils/runtime.py, name=runtime.py, size=123), FileInfo(path=notebookutils/session.py, name=session.py, size=61), FileInfo(path=notebookutils/warehouse.py, name=warehouse.py, size=438), FileInfo(path=notebookutils/workspace.py, name=workspace.py, size=449), FileInfo(path=notebookutils/__init__.py, name=__init__.py, size=205), FileInfo(path=notebookutils/__pycache__, name=__pycache__, size=None)]

## What can this interface be used for
- Actual mssparkutils.fs implementation to interact with the local file system
- fs implementation doesn't support Hadoop or Cloud Storage yet such as Azure Data Lake (can be added later)
- Dummy API Calls to mssparkutils for most functionality

# Important Notes
This interface should be used instead of dummy-notebookutils from Microsoft, as they have the same module path notebookutils and notebookutils.mssparkutils.

In Synapse and Fabric this install is not required, the same imports as in the sample can be used but will then point to the actual notebookutils and notebookutils.mssparkutils installed natively in Fabric/Synapse.