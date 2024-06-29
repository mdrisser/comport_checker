import serial.tools.list_ports
from rich.console import Console

console = Console(width=80)
ports = []

for port in serial.tools.list_ports.comports():
    ports.append(port.name)

if(len(ports) == 0):
    console.print()
    console.print("No COM Ports currently in use.", style="red on white")
    console.print()
else:
    console.print()
    for port in ports:
        print(f"[yellow bold]{port.device}:[/yellow bold] [white]{port.description}[/white]")
    
    console.print()