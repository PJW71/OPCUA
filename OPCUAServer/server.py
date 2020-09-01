from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://0.0.0.0:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")
   
Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)
OnOff = Param.add_variable(addspace, "OnOff", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()
OnOff.set_writable()

server.start()
print("Server started at {}".format(url))

# Read OnOff node
var = server.get_node("ns=2;i=5")


while True:
    Temperature = randint(10, 50)
    Pressure = randint(200, 999)
    TIME = datetime.datetime.now()
    
    # print(Temp.get_value(),Press.get_value(),Time.get_value(), var.get_value())
    
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    # print(Temp.get_value(),Press.get_value(),Time.get_value(), var.get_value())
    
    time.sleep(0.1)
    
    # print(server.activate_session())
