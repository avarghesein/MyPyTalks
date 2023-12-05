from MyPyTalks.PromptHandler import Generate
from MyPyTalks.RunShell import bash, ProcessScriptRequest, RunScriptFile,SaveScriptFile,GetRecentScript

def GenerateScript(prompt):
    command = Generate(f"""{prompt}
    Output only the bash script without any comments.
    Start the code block with ``` and End with ```
    """)
    command = ProcessScriptRequest(command)
    return command

def ExplainScript(command):
    explain = Generate(f"""Summarize the Below Code in very crisp manner
    {command}
    Show Output in the below format.
    ```
    <b>Purpose Of the Script</b>:
    Show the script summary here
    <b>Execution Mode</b>:
    Show as Update Mode, if the script updates system configurations.
    Show as Update Mode, if the script update or delete files.
    Show as Update Mode, if the script kills processes.
    Show as Read Only Mode, if the scripts only reads information.
    <b>Execution Risk</b>:
    Show as High Risk, if the script updates system configurations.
    Show as High Risk, if the script update or delete files.
    Show as High Risk, if the script kills processes.
    Show as Low Risk, if the scripts only reads information.
    ```
    """)
    return explain

def ExecuteScript(command):
    SaveScriptFile(command)
    return RunScriptFile()

def GetScript():
    return GetRecentScript()

def Main():
    prompt = "\n\nMyPyTalk: I'm the Shell Co-pilot. Provide the tasks you've to perform?\n\n"
    print(prompt)
    while prompt and prompt.lower() != "exit":
        prompt = input("$>")
        if prompt.lower() == "exit": continue
        #prompt = "Delete all files in my home directory which are around 3 months old. Show only file names"

        
        command = GenerateScript(prompt)
        explain = ExplainScript(command)       
        explain += f"\n\nScript:\n\n{command}"

        print(explain)

        consent = input("Do you Want to execute the script? yes/no :")

        if consent.lower() == "yes":
            output = ExecuteScript(command)
            print(output)
