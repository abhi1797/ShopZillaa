import sqlite3

# Open database
conn = sqlite3.connect('database.db')

# Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,



		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''CREATE TABLE seller2(sId INTEGER PRIMARY KEY,seller_name TEXT,name1 TEXT,price1 REAL,description1 TEXT,image1 TEXT,stock1 INTEGER,categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId))''')

conn.execute('''CREATE TABLE order_ack(orderId INTEGER PRIMARY KEY,userId INTEGER,
		productId INTEGER,
		purchased_date date,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId))''')

conn.execute('''CREATE TABLE complaint1(userId INTEGER,orderId INTEGER,C_ID INTEGER PRIMARY KEY,description TEXT,feedback varchar(255),FOREIGN KEY(userId) REFERENCES users(userId),
FOREIGN KEY(orderId) REFERENCES order_ack(orderId))''')


conn.close()
