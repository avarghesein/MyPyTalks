# MyPyTalks
Talk to Your Pi (RaspberryPi | UNIX | Linux Systems) in Natural Language using Generative AI

![alt MyPyTalks](https://github.com/avarghesein/MyPyTalks/blob/main/DOC/MyPyTalks_en.jpg)

# Features

Gain 60-70% improvement in effot savings and quality of the maintenance tasks, You do with Your Linux/Unix Boxes with the Power Of Generative AI.

1. Execute Your Talks under Linux, with Plain English Prompts
2. Assesses The Prompt and Provides the impact and risk of the given Task on the System
3. Flag, Tasks which are of High Impact on the System, like Deleting Files
4. Allow you to Edit the Generated Script as per your need, before execution

# Sample MyPyTalk Commands
Talk to your Linux Systems in Plain English. It could generate the desired native shell commands using GenerativeAI.
Tried and tested with GPT-3.5-turbo model from OpenAI

    who am i?
    What is the current linux distribution name?
    delete all files in my download directory which are 2 months old.
    which all files in my download directory modified last two weeks?. show count
    Kill the vscode process
    who all are the users of the system?
    which all files in my download directory having more than 10 lines?
    which all files in my download directory having more than 5MB? show count
    show all files modified till last month. show file name only in descending order
    which all kernel modules are available?
    Show total memory
    Show the cpu cores available
    Show current system load
    what is the current swappiness?
    when the files sytem was created
    which all are mounted under /media
    show free memory in MB
    show the contents of  ~/.profile


## How To Deploy

1. Based on the Architecture (RaspberryPi Or X64), copy the Release zip file from [Releases folder](https://github.com/avarghesein/MyPyTalks/tree/main/Releases)
2. Unzip to your desired location
3. Update permissions for RunApp.sh (chmod a+x ./RunApp.sh)
4. Update your OpenAI key and other related details in .env file
5. Run RunApp.sh
6. Access MyPyTalks with http://localhost:2177
