import sqlite3

conn = sqlite3.connect('dist.db')
conn.execute('PRAGMA foreign_keys = ON')

cursor = conn.cursor()

cursor.execute(''' DROP TABLE IF EXISTS Warehouses''')
cursor.execute(''' DROP TABLE IF EXISTS Products''')
cursor.execute(''' DROP TABLE IF EXISTS Warehouse_Products''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT NOT NULL,
    ProductDescription TEXT,
    ProductQuantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Warehouses (
    WarehouseID INTEGER PRIMARY KEY,
    WarehouseName TEXT NOT NULL,
    DistributionCapacity INTEGER NOT NULL,
    EmployeeCount INTEGER NOT NULL,
    DeliveryVehicleCount INTEGER NOT NULL,
    CoverageArea INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Warehouse_Products (
    WarehouseID INTEGER,
    ProductID INTEGER,
    ProductQuantity INTEGER NOT NULL,
    CONSTRAINT WarehouseID FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID),
    CONSTRAINT ProductID FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    UNIQUE (WarehouseID, ProductID)
)              
''')

conn.commit()

conn.close()

print("Database and tables created successfully.")
