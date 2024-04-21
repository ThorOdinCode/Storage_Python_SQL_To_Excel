import sqlite3
import pandas as pd

def data_to_excel():
    conn = sqlite3.connect('dist.db')

    print("IN HERE")


    query1 = "SELECT * FROM Products"
    query2 = "SELECT * FROM Warehouses"
    query3 = "SELECT * FROM Warehouse_Products"

    df1 = pd.read_sql_query(query1, conn)
    df2 = pd.read_sql_query(query2, conn)
    df3 = pd.read_sql_query(query3, conn)

    conn.close()

    excel_file_path = 'project_data.xlsx'
    with pd.ExcelWriter(excel_file_path) as writer:
        df1.to_excel(writer, sheet_name='Products', index=False)
        df2.to_excel(writer, sheet_name='Warehouses', index=False)
        df3.to_excel(writer, sheet_name='Warehouse_Products', index=False)
    
    conn.close()
    print("Data successfully transferred")

conn = sqlite3.connect('dist.db')

cursor = conn.cursor()

rep = "Y"
while rep == "Y" :
    type = input("Warehouse(W), Product (P), or Product in Warehouse (PW)?: ")

    if type.capitalize() == "P" :
        ProductID, ProductName, ProductDescription, ProductQuantity = input("Input Product ID, Product Name, Product description (N/A if none), and Product quantity, separated by spaces: ").strip().split()
        ProductID=int(ProductID)
        ProductName=str(ProductName)
        if ProductDescription == "N/A" :
            ProductDescription = ""
        else :
            ProductDescription=str(ProductDescription)
        ProductQuantity=int(ProductQuantity)
        cursor.execute('''
        INSERT INTO Products (ProductID, ProductName, ProductDescription, ProductQuantity) VALUES (?, ?, ?, ?)
        ''', (ProductID, ProductName, ProductDescription, ProductQuantity))
    
    elif type.capitalize() == "W" :
        WarehouseID, WarehouseName, DistributionCapacity, EmployeeCount, DeliveryVehicleCount, CoverageArea = input("Input WarehouseID, Warehouse Name, Distribution Capacity, Employee Count, Delivery Vehicle Count, Coverage Area separated by spaces: ").strip().split()
        WarehouseID=int(WarehouseID)
        WarehouseName=str(WarehouseName)
        DistributionCapacity=int(DistributionCapacity)
        EmployeeCount=int(EmployeeCount)
        DeliveryVehicleCount=int(DeliveryVehicleCount)
        CoverageArea=int(CoverageArea)
        cursor.execute('''
        INSERT INTO Warehouses (WarehouseID, WarehouseName, DistributionCapacity, EmployeeCount, DeliveryVehicleCount, CoverageArea) VALUES (?, ?, ?, ?, ?, ?)
        ''', (WarehouseID, WarehouseName, DistributionCapacity, EmployeeCount, DeliveryVehicleCount, CoverageArea))
    
    elif type.upper() == "PW" :
        WarehouseID, ProductID, ProductQuantity = input("Input Warehouse ID, Product ID, Product Quantity separated by spaces: ").strip().split()
        WarehouseID=int(WarehouseID)
        ProductID=int(ProductID)
        ProductQuantity=str(ProductQuantity)
        cursor.execute('''
        INSERT INTO Warehouse_Products (WarehouseID, ProductID, ProductQuantity) VALUES (?, ?, ?)
        ''', (WarehouseID, ProductID, ProductQuantity))
    
    else :
        continue
    
    conn.commit()
    
    rep = input("Add more data? (Y)").capitalize()

conn.close()
e = "N"
e = input("Create excel spreadsheet and transfer data? (Y)").capitalize()

if(e=="Y"):
    data_to_excel()

