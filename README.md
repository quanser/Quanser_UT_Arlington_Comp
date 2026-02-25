<img src="docs/images/quanser-resources-header.png" width="100%">

## Getting Started

Start by downloading the resources and setting up your computer using the [Quanser Academic Resources](https://github.com/quanser/Quanser_Academic_Resources) repository.
Make sure to follow the instructions in the `Setting Up Your Computer` Section in that repo.

> [!NOTE]
> **DO NOT FOLLOW ANY OF THE INSTRUCTIONS OF DOWNLOADING QUANSER INTERACTIVE LABS, FOLLOW THE INSTRUCTIONS IN THIS README INSTEAD**  
> The section [How to Download Quanser Interactive Labs](#qlabs) has the specific instructions for this.

You should now have a `C:/Users/user/Documents/Quanser` folder with all of our resources.

## Downloading Arlington Specific Resources

The first step is to download these resources into your computer. We recommend downloading the files simply as a .zip file. 

### How to Download the Resources

1. Inside your `C:/Users/user/Documents/Quanser` folder that was created when downloading the Academic Resources, create a new folder with whatever name you prefer. We suggest calling it something like `Arlington_Competition`. This should live in the same level as the numbered folders (0_libraries, 1_setup ...).

2. Click the green Code button at the top of this GitHub page, click _Download ZIP_ at the bottom of the menu that pops up.

3. Unzip/extract the folder in your system.

4. Go into _Quanser_UT_Arlington_Comp-main_, you will see the individual files. Copy all the contents of that folder into your newly created `C:/Users/user/Documents/Quanser/Arlington_Competition` folder.

<a id="qlabs"></a>

### How to Download Quanser Interactive Labs

#### If you are using MATLAB/Simulink:

Note that this download is necessary but done only to get the Quanser blocks for Simulink. Do not try to open this version. Download the latest Quanser Interactive Labs from the Python section below and follow those instructions too. 

- Download Quanser Interactive Labs through the MATLAB Add On Explorer.

    <img src="docs/images/addOnExplorer.png" width="300">

    ```
    Quanser Interactive Labs for MATLAB
    ```

    <img src="docs/images/qlabsAddOn.png" width="400">

    
#### If you are using Python:

1.  Download the latest Quanser Interactive Labs [from here](https://quanserinc.box.com/shared/static/1jqs60lq2hpebu55c7btbqo5wgrf8zgm.zip).

2.  Unzip the folder and move the complete folder (QLabs) inside the folder you created `C:/Users/user/Documents/Quanser/Arlington_Competition`.
    - The folder structure for the downloaded files should look like this: 

        <img src="docs/images/qlabs_setup.png" width="300">

3. Open your new `QLabs` folder. Double click on `Quanser Interactive Labs.exe`, on the window that opens, fill your login information, click `remember me` and log in.

4. Close `Quanser Interactive Labs`. This steps ensure that when you run the provided bat files, you do not have to worry about logins anymore.


## Using the Files

1. Make sure you do not have Quanser Interactive Labs open.

2. Open the correct navigator file:
    - If you are going to be using Simulink, open `Arlington_Competition/Navigator.slx`.
    - If you are going to be using Python, open `navigator.py` in your preferred development environment. We use Visual Studio Code.

3. From your `Arlington_Competition` folder, run `Start_Everything.bat`.
    - This will open Quanser Interactive Labs and load the QDrone Workspace.
    - It will create colored structures around the workspace.
    - It will initialize the Drone models that will receive commands to fly the drone. 
    - The drone will take flight and hover around the [0,0,1] location in the world.

4. Using Simulink or Python, click run on your opened file. The existing examples will move the QDrone slowly in X,Y,Z as defined by the existing sine waves.
    - Both files run at 200Hz and display cameras at 30Hz.
    - Both files take drone commands. In Simulink they are the `Drone Cmds` in the `DroneStack Comms` block. In Python, there is `cmd_x,cmd_y,cmd_z,cmd_yaw`.
    - Both files will display the following cameras: left, right, back, downward, RealSense RGB and RealSense Depth.
    - If you are using Python, the file includes comments as well as a section where you can modify or add code to help prevent breaking existing files. 
        - the variable simulationTime shows how long the code will run for. You can also stop it using Ctrl+C.

5. To stop everything:
    - Stop your Simulink or Python file. 
    - From your `Arlington_Competition` folder, run CleanUp.bat.  
    - Close Quanser Interactive Labs.

