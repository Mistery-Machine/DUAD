import psycopg2

class PgManager: 
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name =db_name
        self.user =user 
        self.password=password
        self.host=host 
        self.port=port

        self.connection = self.create_connection()
        if self.connection:
            self.cursor=self.connection.cursor()
            print("Conexion exitosa a la base de datos")

    def create_connection(self):
        try: 
            connection = psycopg2.connect(
                dbname =self.db_name,
                user = self.user, 
                password=self.password,
                host =self.host,
                port=self.port, 
            )
            return connection
        except Exception as error: 
            print("Error conectando con la base de datos", error)
            return None
    
    def close_connection(self):
        if self.cursor: 
            self.cursor.close()
        if self.connection:
            self.connection.close
        print("Conexion cerrada")
    
    def execute_query(self, query, *args): 
        self.cursor.execute(query, args if args else None)
        self.connection.commit()

        if self.cursor.description: 
            return self.cursor.fetchall()
        return None
        