from opcua.common import methods
from opcua import Client
from opcua import ua

client = Client("opc.tcp://192.168.118.33:4840")
client.connect()


parent = client.get_node('ns=3;s="OPCMethod_SetMachSpeed_DB_1"')
method = parent.get_child("3:Method")
inputs = method.get_child("InputArguments")


parent.call_method(method, ua.Variant(25, ua.VariantType.Int16))


# parent_node_id = 'ns=3;s=DataBlocksInstance'
# parent_node_id = 'ns=3;s="OPCMethod_SetMachSpeed_DB".Method'
# method_node_id = 'ns=3;s="OPCMethod_SetMachSpeed_DB"'
# method_browse_name = '3:Method'

# # objects_node = client.get_objects_node()
# parent_node = client.get_node(parent_node_id)
# method_node = client.get_node(method_node_id)

# methods.call_method(parent_node, method_browse_name, 1)
# # objects_node.call_method(method_browse_name)


# parent = client.get_node("ns=2;i=10875")
# method = parent.get_child("0:AddComment")
# inputs = method.get_child("0:InputArguments").get_value()
# print("inputArgs are: ", inputs)        
# sas = str.encode("hello")
# arguments = [ua.Variant(stringTest,ua.VariantType.ByteString),ua.Variant("comment",ua.VariantType.String)]
# res = parent.call_method(method, *arguments)



# client = Client("opc.tcp://opcua.demo-this.com:51210/UA/SampleServer")
# client.connect()

# parent = client.get_node('ns=2;i=10755')
# method = parent.get_child("2:ScalarMethod1")
# inputs = method.get_child("InputArguments")

# parent.call_method(method, 
#     True, 
#     ua.Variant(0, ua.VariantType.SByte), 
#     ua.Variant(0, ua.VariantType.Byte), 
#     ua.Variant(0, ua.VariantType.Int16), 
#     ua.Variant(0, ua.VariantType.UInt16), 
#     ua.Variant(0, ua.VariantType.Int32), 
#     ua.Variant(0, ua.VariantType.UInt32), 
#     ua.Variant(0, ua.VariantType.Int64),
#     ua.Variant(0, ua.VariantType.UInt64), 
#     ua.Variant(0, ua.VariantType.Float), 
#     ua.Variant(0, ua.VariantType.Double)
# )
