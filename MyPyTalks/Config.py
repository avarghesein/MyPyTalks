import os

import MyPyTalks.Resources as RS
ResourceManager = RS.Resource()
UX_Internal = False

if os.environ["UI"] == "":
    if ResourceManager.IsZip():         
        UX_Internal = True
    else:
        os.environ["UI"] = ResourceManager.GetRootNamespace() + "/UI"
else:
    static_path = os.environ["UI"]
    if not os.path.isabs(static_path):
        script_dir = os.path.dirname(__file__)
        os.environ["UI"] = script_dir + "/../" + static_path


