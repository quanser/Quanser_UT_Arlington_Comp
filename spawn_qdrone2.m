% Spawn QDrone2 environment (MATLAB port of spawn_qdrone2.py)
% This script connects to QLabs, terminates realtime models, and
% spawns a set of dynamic boxes with material and physics properties.

close all;
clear all;
clc;

% --------------------------------------------------------------
% Setting MATLAB Path for the libraries
newPathEntry = fullfile(getenv('QAL_DIR'), '0_libraries', 'matlab', 'qvl');
pathCell = regexp(path, pathsep, 'split');
if ispc  % Windows is not case-sensitive
  onPath = any(strcmpi(newPathEntry, pathCell));
else
  onPath = any(strcmp(newPathEntry, pathCell));
end

if onPath == 0
    path(path, newPathEntry);
    savepath;
end
% --------------------------------------------------------------

disp('Connecting to QLabs...');
qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp('Unable to connect to QLabs');
    return
end

disp('Connected');

% stop all models
system("quarc_run -q -Q -t tcpip://localhost:17000 *.rt-win64");

% create some dynamic environment objects
hShape = QLabsBasicShape(qlabs, true);
hShape.destroy_all_actors_of_class();

box_mass = 10.0;

location_1 = -4;
location_2 = -6;
location_3 = -8;
location_4 = -10;
location_5 = -12;
location_6 = -16;
location_7 = -2;
location_8 = -14;

% Column 1
hShape.spawn([location_1,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_1,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_1,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_1,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 2
hShape.spawn([location_2,0,0.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_2,-1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_2,1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_2,0,2.2], [0,0,0], [1,3,0.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 3
hShape.spawn([location_3,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_3,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_3,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_3,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 4
hShape.spawn([location_4,-1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0.8], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_4,1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0.8], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_4,0,1.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0.6], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 5
hShape.spawn([location_5,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_5,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_5,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_5,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 6
hShape.spawn([location_6,0,0.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_6,-1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_6,1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_6,0,2.2], [0,0,0], [1,3,0.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 7
hShape.spawn([location_7,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_7,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_7,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0.8,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_7,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0.6,0], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);

% Column 8
hShape.spawn([location_8,-1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0.8], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_8,1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.8,0,0.8], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);
hShape.spawn([location_8,0,1.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, 1);
hShape.set_material_properties([0.6,0,0.6], 1, 0, 1);
hShape.set_physics_properties(1, box_mass, 0.01, 0.0, 0.0, 0.7, hShape.COMBINE_AVERAGE, 0.3, hShape.COMBINE_AVERAGE, 1);
pause(0.5);


hQDrone = QLabsQDrone2(qlabs, true);
hQDrone.actorNumber = 0;
hQDrone.destroy();
% spawn_id_degrees(actorNumber, location, rotation, scale, configuration, waitForConfirmation)
hQDrone.spawn_id_degrees(0, [0, 0, 0], [0, 0, 0], [1,1,1], 0, 1);
hQDrone.possess(hQDrone.VIEWPOINT_TRAILING);

% Specify path to where spawn model is located (match python rtmodels.QDRONE2)
rtmodel_path = fullfile(getenv('RTMODELS_DIR'), 'QDrone2', 'QDrone2_Workspace.rt-win64');
cmd = ['quarc_run -D -r -t tcpip://localhost:17000 "', rtmodel_path, '" -uri tcpip://localhost:17001 -hostname localhost -devicenum 0"'];
system(cmd);

% Close qlabs
try
  qlabs.close();
catch
end
disp('Done!');


