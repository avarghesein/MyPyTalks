def bash(s):
    import subprocess
    return subprocess.check_output(s,shell=True)

def ProcessScriptRequest(response):
    import re
    bash_script = re.findall('```(?P<program>[^`]+)```', response, re.IGNORECASE)

    if bash_script:
        try:
            #program = bash_script.group(1)
            program = ""
            for line in bash_script:                
                program += line + "\n"

            program = program.replace("bash","")
            program = re.sub("\n#[^\n]+","",program)
            program = "#!/bin/bash\n" + program + "\nexit 0"
            program = re.sub("[\n]{2,}","\n",program)
            return program
        except Exception as ex:
            pass
    
    return None

ScriptFile = "MyPyTalks.sh"

def GetRecentScript():
    import os
    # Get the home directory path
    home_dir = os.path.expanduser('~')
    # Create the file path
    bash_script_file = os.path.join(home_dir, ScriptFile)
    with open(bash_script_file, "r") as f:
        return f.read()
    

def SaveScriptFile(s):
    import os
    # Get the home directory path
    home_dir = os.path.expanduser('~')
    # Create the file path
    bash_script_file = os.path.join(home_dir, ScriptFile)
   
    with open(bash_script_file, "w+") as f:
        f.write(s)
    
    bash(f"chmod a+x ~/{ScriptFile}")

def RunScriptFile():
    import subprocess
    
    import os
    # Get the home directory path
    home_dir = os.path.expanduser('~')
    # Create the file path
    bash_script_file = os.path.join(home_dir, ScriptFile)

    try:
        # Run the Bash script and capture the output
        result = subprocess.run(['bash', bash_script_file], stdout=subprocess.PIPE, check=True, text=True)

        # Access the captured output
        script_output = result.stdout
        return script_output
    except subprocess.CalledProcessError as e:
        print(f"Error running Bash script '{bash_script_file}': {e}")
        return str(e)