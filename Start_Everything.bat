start "" quarc_run -q -Q -t tcpip://localhost:17000 *.rt-win64

TIMEOUT /T 1

start "" quarc_run -q -Q -t tcpip://localhost:17000 *.rt-win64

TIMEOUT /T 1

start "" "QLabs\Quanser Interactive Labs.exe" -loadmodule Warehouse

TIMEOUT /T 10

python spawn_qdrone2.py

TIMEOUT /T 2

start "Virtual QDrone Model" "quarc_run" -r virtual_FlightStack.rt-win64

TIMEOUT /T 10

