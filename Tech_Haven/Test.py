import shelve
from AddProduct import *
from Product import *
# db = shelve.open('products.db', 'c')
# CPU_dict = {}
# CPU = AddProduct.AddProduct('/static/Images/Products/CPU/RYZEN3600.jpg', '3600', 'AMD RYZEN 3600', 'AMD\'s 3000 series 6-core, 12-thread 4.2Ghz processor', 240, 'AMD,RYZEN,3600')
# CPU_dict[CPU.get_product_id()] = CPU
# CPU = AddProduct.AddProduct('/static/Images/Products/CPU/RYZEN5600X.jpg', '5600X', 'AMD RYZEN 5600X', 'AMD\'s 5000 series 6-core, 12-thread 4.6Ghz processor', 280, 'AMD,RYZEN,5600X')
# CPU_dict[CPU.get_product_id()] = CPU
# CPU = AddProduct.AddProduct('/static/Images/Products/CPU/RYZEN5800X.jpg', '5800X', 'AMD RYZEN 5800X', 'AMD\'s 5000 series 8-core, 16-thread 4.7Ghz processor', 350, 'AMD,RYZEN,5800X')
# CPU_dict[CPU.get_product_id()] = CPU
# CPU = AddProduct.AddProduct('/static/Images/Products/CPU/RYZEN5900X.jpg', '5900X','AMD RYZEN 5900X', 'AMD\'s 5000 series 12-core, 24-thread 4.8Ghz processor', 490, 'AMD,RYZEN,5900X')
# CPU_dict[CPU.get_product_id()] = CPU
# db['CPU'] = CPU_dict
#
# db = shelve.open('products.db', 'c')
# RAM_dict = {}
# RAM = AddProduct.AddProduct('/static/Images/Products/RAM/LPX8.jpg', 'CVLPX8', 'Corsair Vengeance LPX 8GB 1x8GB', '1x8GB ram stick, 3200mhz', 50, 'Corsair,Vengeance,LPX,8GB')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/RAM/RGBPRO.jpg', 'CVRP16', 'Corsair Vengeance RGB PRO 16GB 2x8GB', '2x8GB ram sticks, 3200MHz', 100, 'Corsair,Vengeance,RGB,Pro16')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/RAM/Corsair-RGB-RS.jpg', 'CVRR64', 'Corsair Vengeance RGB RS 64GB 2x32GB', '2x32GB Ram stick, 3600Mhz', 360, 'Corsiar,Vengeance,RGB,RS,64')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/RAM/RGB-PRO-SL.jpg', 'CVRPS128', 'Corsair Vengeance RGB Pro SL 128GB 4x32GB', '4x32GB Ram stick, 3200Mhz', 750, 'Corsair,Vengeance,RGB,Pro,SL,128')
# RAM_dict[RAM.get_product_id()] = RAM
# db['RAM'] = RAM_dict

# db = shelve.open('products.db', 'c')
# RAM_dict = {}
# RAM = AddProduct.AddProduct('/static/Images/Products/GPU/ASUSGTX1050TI.PNG', 'AUGTX1050TI', 'Asus GeForce GTX 1050 TI', 'A classic GTX 1050 TI with a 4GB memory and a clock speed of 7008MHz', 300, 'ASUS,GTX,1050,TI')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/GPU/GigabyteAorusRXT3060TI.png', 'GIGARTX3060TI', 'Gigabyte Aorus GeForce RTX 3060-TI', 'Nvida RTX 3000 series, 12GB Memory with clock speed of 1807Mhz', 900, 'Gigabyte,Aorus,RTX,3060-TI')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/GPU/EVGARTX3070TI.png', 'EVRTX3070TI', 'EVGA RTX 3070 TI XC3', 'Nvida 3000 Series, 8GB GDDR6x Memory 1815mhz', 1200, 'EVGA-RTX-3070TI')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/GPU/ZotacRTX3080TITrinity.jpg', 'ZORTX3080TI', 'Zotac RTX 3080 TI Trinity', 'Nvida 3000 Series, 12GB GDDR6x Memory 1659mhz', 2300, 'Zotac-RTX-3080-TI')
# RAM_dict[RAM.get_product_id()] = RAM
# db['GPU'] = RAM_dict

# db = shelve.open('products.db', 'c')
# RAM_dict = {}
# RAM = AddProduct.AddProduct('/static/Images/Products/MOBA/A520m.png', 'A520', 'Gigabyte A520M', 'Gigabyte A520M', 70, 'Gigabyte,A520')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/MOBA/ASUS_TUF.png', 'ASUSTUFX570', 'ASUS X570 TUF', 'X570', 200, 'ASUSTUFX570')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/MOBA/MSIMEGX570.jpg style=width:200px; height:253px', 'MSIMEGX570', 'MSI MEG X570 ACE', '570', 400, 'MSI,MEG,X570,ACE')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/MOBA/b550.jpg style=width:200px; height:253px', 'ASROCKPGVelovctiaB550', 'ASROCK PG Velovctia B550', 'B550 Platform', 300, 'Asrock,PG Velovctia,B550,PG Velovctia')
# RAM_dict[RAM.get_product_id()] = RAM
# # RAM = AddProduct.AddProduct('', '', '', '', 0, '')
# # RAM_dict[RAM.get_product_id()] = RAM
# db['MOBA'] = RAM_dict

# db = shelve.open('products.db', 'c')
# RAM_dict = {}
# RAM = AddProduct.AddProduct('/static/Images/Products/PSU/EVGA220-650.png', 'EVGA220-650', 'EVGA 220-G5-650 X1', '650 Watt psu', 70, 'EVGA,220-G5-650,X1')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/PSU/Coolermastermwe750.jpg', 'COOLERMASTERMWE750','Cooler Master MWE GOLD 750w', '750watt', 200, 'Cooler,Master,MWE,Gold,750w')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/PSU/SEASONIC850.jpg', 'SEASONIC850PLAT', 'Seasonic Prime 850 Titanium SSR-850TR', 'X570', 299, 'Seasonic,850,Plat')
# RAM_dict[RAM.get_product_id()] = RAM
# RAM = AddProduct.AddProduct('/static/Images/Products/PSU/SEASONIC1000.jpg', 'SEASONICPRIME1000', 'Seasonic Prime 1000', 'X570', 500, 'SEASONICPRIME1000')
# RAM_dict[RAM.get_product_id()] = RAM
# db['PSU'] = RAM_dict
#
# db = db['Review-SEASONIC850PLAT']


# db = shelve.open('products.db', 'c')
# Storage_dict = {}
# Storage = AddProduct.AddProduct('/static/Images/Products/Storage/Crucial.jpg', 'CrucialSSD1TB', 'Crucial SSD 1 TB', '1TB of storage ', 80, 'Crucial,SSD,1,TB')
# Storage_dict[Storage.get_product_id()] = Storage
# Storage = AddProduct.AddProduct('/static/Images/Products/Storage/Samsung.jpg', 'Samsung870EVO2TB', 'Samsung 870 EVO 2TB', '2TB SSD', 200, 'Samsung,870,EVO,2TB')
# Storage_dict[Storage.get_product_id()] = Storage
# Storage = AddProduct.AddProduct('/static/Images/Products/Storage/Samsung.jpg', 'Samsung870QVO4TBSSD', 'Samsung 870 QVO 4TB SSD', '4TB SSD', 400, 'Samsung,870,QVO,4TB,SSD')
# Storage_dict[Storage.get_product_id()] = Storage
# Storage = AddProduct.AddProduct('/static/Images/Products/Storage/Samsung.jpg', 'Samsung870QVO8TBSSD', 'Samsung 870 QVO 8TB SSD', '8TB SSD', 1000, 'Samsung,870,QVO,8TB,SSD')
# Storage_dict[Storage.get_product_id()] = Storage
# db['Storage'] = Storage_dict

db = shelve.open('register.db', 'c')

try:
    #Store the user_dictionary with the users copy from the register database
    users_dict = db['Users']
except:

    #Display error if database is not found
    print("Error in retrieving Users from register.db.")

#an empty list to store emails and mobile number
registered_Email = []
registered_Mobile_Number = []
# # i = 2
# # while i < 20:
# #     users_dict.pop(i)
# #     i += 1
# #examine each key in the user dictionary that has been extracted.
for key in users_dict:

    #set user with the users email address
    user = users_dict.get(key)
    print(str(key) + ' '+ user.get_email())
    #appends the list of registered email with the currently entered email address
    registered_Email.append(user.get_email())
    registered_Mobile_Number.append(user.get_mobile_number())
db['Users'] = users_dict

print(registered_Email)
print(registered_Mobile_Number)

# list = []
# form_name_list = []
# db = shelve.open('products.db', 'c')
# for product_type in db:
#     for product_id in db[product_type]:
#         list.append(product_id)
#         form_name_list.append(db[product_type][product_id].get_form_name())
# print(list)
# print(form_name_list)
