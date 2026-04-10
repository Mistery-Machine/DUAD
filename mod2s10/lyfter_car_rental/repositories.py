from db import PgManager 

class UserRepository: 
    def __init__(self, db_manager):
        self.db_manager=db_manager

    def _format_user(self, record): 
        return {
            "id": record[0],
            "full_name": record[1],
            "email": record[2],
            "username": record[3],
            "password": record[4],
            "birthdate": record[5],
            "status": record[6],
        }
    
    def create(self, full_name, email, username, password, birthdate, status):
        try: 
            self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.users 
                (full_name, email, username, password, birthdate, status)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                full_name, email, username, password, birthdate, status
            )
            print ("Usuario creado exitosamente")
            return True
        except Exception as error: 
            print("Error creando el usuario", error)
            return False
    
    def get_all(self, filters=None):
        try:
            query  = "SELECT * FROM lyfter_car_rental.users"
            args   = []
            if filters:
                conditions = [f"{key} = %s" for key in filters.keys()]
                query += " WHERE " + " AND ".join(conditions)
                args   = list(filters.values())

            results = self.db_manager.execute_query(query, *args)
            return [self._format_user(r) for r in results]
        except Exception as error:
            print("Error obteniendo usuarios:", error)
            return False
        
    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE id = %s", _id
            )
            return self._format_user(results[0])
        except Exception as error:
            print("Error obteniendo usuario:", error)
            return False
        
    def update_status(self, _id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET status = %s WHERE id = %s",
                status, _id
            )
            print("Estado del usuario actualizado")
            return True
        except Exception as error:
            print("Error actualizando estado del usuario:", error)
            return False
        
    def flag_as_delinquent(self, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET status = %s WHERE id = %s",
                "delinquent", _id
            )
            print("Usuario flaggeado como moroso")
            return True
        except Exception as error:
            print("Error flaggeando usuario:", error)
            return False
        

class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, record):
        return {
            "id":     record[0],
            "brand":  record[1],
            "model":  record[2],
            "year":   record[3],
            "status": record[4],
        }
    def create(self, brand, model, year, status):
        try:
            self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
                VALUES (%s, %s, %s, %s)
                """,
                brand, model, year, status
            )
            print("Auto creado exitosamente")
            return True
        except Exception as error:
            print("Error creando auto:", error)
            return False
        
    def get_all(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.cars"
            args  = []

            if filters:
                conditions = [f"{key} = %s" for key in filters.keys()]
                query += " WHERE " + " AND ".join(conditions)
                args   = list(filters.values())

            results = self.db_manager.execute_query(query, *args)
            return [self._format_car(r) for r in results]
        except Exception as error:
            print("Error obteniendo autos:", error)
            return False

  
    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars WHERE id = %s", _id
            )
            return self._format_car(results[0])
        except Exception as error:
            print("Error obteniendo auto:", error)
            return False


    def update_status(self, _id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s",
                status, _id
            )
            print("Estado del auto actualizado")
            return True
        except Exception as error:
            print("Error actualizando estado del auto:", error)
            return False



class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rental(self, record):
        return {
            "id":          record[0],
            "user_id":     record[1],
            "car_id":      record[2],
            "rental_date": record[3],
            "status":      record[4],
        }

  
    def create(self, user_id, car_id):
        try:
            
            self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
                VALUES (%s, %s, %s)
                """,
                user_id, car_id, "active"
            )
            
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s",
                "rented", car_id
            )
            print("Alquiler creado exitosamente")
            return True
        except Exception as error:
            print("Error creando alquiler:", error)
            return False

    
    def get_all(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.rentals"
            args  = []

            if filters:
                conditions = [f"{key} = %s" for key in filters.keys()]
                query += " WHERE " + " AND ".join(conditions)
                args   = list(filters.values())

            results = self.db_manager.execute_query(query, *args)
            return [self._format_rental(r) for r in results]
        except Exception as error:
            print("Error obteniendo alquileres:", error)
            return False

    
    def complete(self, _id, car_id):
        try:
            
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET status = %s WHERE id = %s",
                "completed", _id
            )
           
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s",
                "available", car_id
            )
            print("Alquiler completado exitosamente")
            return True
        except Exception as error:
            print("Error completando alquiler:", error)
            return False

    
    def update_status(self, _id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET status = %s WHERE id = %s",
                status, _id
            )
            print("Estado del alquiler actualizado")
            return True
        except Exception as error:
            print("Error actualizando estado del alquiler:", error)
            return False