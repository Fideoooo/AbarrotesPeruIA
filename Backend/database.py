import pyodbc

class Database:
    def __init__(self):
        self.conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=XANIXIU;"
            "DATABASE=AbarrotesDB;"
            "Trusted_Connection=yes;"  # usa autenticación de Windows
        )

    def connect(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            return conn
        except Exception as e:
            print("Error de conexión:", e)
            return None

    def validar_usuario(self, username, password):
        conn = self.connect()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("EXEC sp_validar_usuario ?, ?", (username, password))
            user = cursor.fetchone()
            return user
        finally:
            conn.close()
    
    def obtener_productos(self):
        """Obtiene todos los productos activos con sus relaciones básicas"""
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            query = """
            SELECT 
                p.ProductoID, 
                p.Nombre, 
                p.Presentacion, 
                p.CodigoBarras, 
                c.Nombre AS Categoria, 
                m.Nombre AS Marca, 
                p.Precio
            FROM Productos p
            LEFT JOIN Categorias c ON p.CategoriaID = c.CategoriaID
            LEFT JOIN Marcas m ON p.MarcaID = m.MarcaID
            WHERE p.Estado = 1  -- Solo productos activos
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        finally:
            conn.close()

    def registrar_venta(self, detalles, empleado_id):
        """
        detalles = [
            {"ProductoID": 1, "Cantidad": 2},
            {"ProductoID": 5, "Cantidad": 1},
        ]
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            cursor = conn.cursor()

            # Insertar venta y capturar ID directamente con OUTPUT
            cursor.execute("""
                INSERT INTO Ventas (EmpleadoID, Total)
                OUTPUT INSERTED.VentaID
                VALUES (?, 0)
            """, empleado_id)

            venta_id_row = cursor.fetchone()
            if not venta_id_row:
                raise Exception("No se pudo obtener el ID de la venta.")
            venta_id = venta_id_row[0]

            # Insertar detalle
            for item in detalles:
                cursor.execute(
                    "INSERT INTO DetalleVenta (VentaID, ProductoID, Cantidad) VALUES (?, ?, ?)",
                    venta_id, item["ProductoID"], item["Cantidad"]
                )

            conn.commit()
            return True, venta_id

        except Exception as e:
            conn.rollback()
            
            msg = str(e)
            if "Stock insuficiente" in msg:
                msg = "No hay stock suficiente para completar la venta."
            else:
                #Para otro errores podrias dejar generico
                msg = "Ocurrio un error al registrar la venta."

            return False, msg

        finally:
            conn.close()

    def agregar_producto_con_camara(self, nombre, categoria_nombre, marca_nombre, presentacion, precio):
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            # Primero aseguramos IDs reales
            categoria_id = self.obtener_categoria_id(categoria_nombre)
            marca_id = self.obtener_marca_id(marca_nombre)

            # Verificar si ya existe el producto
            if self.producto_existe(nombre, categoria_id, marca_id, presentacion):
                return False, "El producto ya existe en la base de datos."

            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Productos (Nombre, CategoriaID, MarcaID, Presentacion, Precio, Estado, FechaRegistro)
                VALUES (?, ?, ?, ?, ?, 1, GETDATE())
            """, (nombre, categoria_id, marca_id, presentacion, precio))
            
            conn.commit()
            return True, "Producto agregado correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al agregar el producto: {str(e)}"
        finally:
            conn.close()
            
    # ----------------------------
    # NUEVO MÉTODO PARA VALIDAR DUPLICADOS
    # ----------------------------
    def producto_existe(self, nombre, categoria_id, marca_id, presentacion):
        conn = self.connect()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) 
                FROM Productos
                WHERE Nombre = ? AND CategoriaID = ? AND MarcaID = ? AND Presentacion = ?
            """, nombre, categoria_id, marca_id, presentacion)
            return cursor.fetchone()[0] > 0
        finally:
            conn.close()

    def obtener_categoria_id(self, nombre_categoria):
        """Obtiene el ID de la categoría, si no existe la crea"""
        conn = self.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT CategoriaID FROM Categorias WHERE Nombre = ?", (nombre_categoria,))
            row = cursor.fetchone()
            if row:
                return row[0]
            # Si no existe, crearla
            cursor.execute("INSERT INTO Categorias (Nombre) VALUES (?)", (nombre_categoria,))
            conn.commit()
            # Recuperar el ID insertado
            cursor.execute("SELECT SCOPE_IDENTITY()")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def obtener_marca_id(self, nombre_marca):
        """Obtiene el ID de la marca, si no existe la crea"""
        conn = self.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT MarcaID FROM Marcas WHERE Nombre = ?", (nombre_marca,))
            row = cursor.fetchone()
            if row:
                return row[0]
            # Si no existe, crearla
            cursor.execute("INSERT INTO Marcas (Nombre) VALUES (?)", (nombre_marca,))
            conn.commit()
            # Recuperar el ID insertado
            cursor.execute("SELECT SCOPE_IDENTITY()")
            return cursor.fetchone()[0]
        finally:
            conn.close()
        
    def obtener_categorias(self):
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            query = "SELECT CategoriaID, Nombre FROM Categorias"
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def obtener_marcas(self):
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT MarcaID, Nombre
                FROM Marcas
                WHERE Estado = 1
                ORDER BY MarcaID
            """)
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    
        
    def insertar_producto(self, producto):
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            # Si ya viene CategoriaID, úsalo; si no, búscalo por nombre
            if "CategoriaID" in producto:
                categoria_id = producto["CategoriaID"]
            else:
                categoria_id = self.obtener_categoria_id(producto["Categoria"])

            # Lo mismo para Marca
            if "MarcaID" in producto:
                marca_id = producto["MarcaID"]
            elif "Marca" in producto:
                if isinstance(producto["Marca"], int):  
                    marca_id = producto["Marca"]  # ya es un ID
                else:
                    marca_id = self.obtener_marca_id(producto["Marca"])  # es texto → busca ID
            else:
                return False, "Falta Marca o MarcaID"

            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Productos 
                (Nombre, CategoriaID, MarcaID, Presentacion, CodigoBarras, Precio, Estado, FechaRegistro)
                VALUES (?, ?, ?, ?, ?, ?, 1, GETDATE())
            """, (
                producto["Nombre"],
                categoria_id,
                marca_id,
                producto["Presentacion"],
                producto.get("CodigoBarras", None),
                producto["Precio"]
            ))

            conn.commit()
            return True, "Producto insertado correctamente."

        except Exception as e:
            conn.rollback()
            error_msg = str(e)

            # 🚨 Captura error de clave duplicada
            if "2627" in error_msg or "UQ_Producto" in error_msg:
                return False, "❌ Este producto ya existe en la base de datos. No es posible añadir"
            else:
                return False, f"Ocurrió un error al insertar el producto: {error_msg}"

        finally:
            conn.close()

    def actualizar_producto(self, producto):
        """
        Actualiza un producto existente.
        producto = {
            "ProductoID": int,
            "Nombre": str,
            "Presentacion": str,
            "CodigoBarras": str,
            "CategoriaID": int,
            "MarcaID": int,
            "Precio": float
        }
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Productos
                SET Nombre = ?, Presentacion = ?, CodigoBarras = ?, CategoriaID = ?, MarcaID = ?, Precio = ?
                WHERE ProductoID = ?
            """, (
                producto["Nombre"],
                producto["Presentacion"],
                producto["CodigoBarras"],
                producto["CategoriaID"],
                producto["MarcaID"],
                producto["Precio"],
                producto["ProductoID"]
            ))
            conn.commit()
            return True, "Producto actualizado correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al actualizar el producto: {str(e)}"
        finally:
            conn.close()

    def eliminar_producto(self, producto_id):
        """
        Desactiva un producto (soft delete) cambiando Estado a 0.
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Productos
                SET Estado = 0
                WHERE ProductoID = ?
            """, (producto_id,))
            conn.commit()
            return True, "Producto desactivado correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al desactivar el producto: {str(e)}"
        finally:
            conn.close()

        # ----------------------------
        # MÉTODOS PARA MARCAS
        # ----------------------------
    def agregar_marca(self, nombre):
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"
        try:
            cursor = conn.cursor()

            # Validar duplicado
            cursor.execute("SELECT COUNT(*) FROM Marcas WHERE Nombre = ?", (nombre,))
            if cursor.fetchone()[0] > 0:
                return False, "❌ La marca ya existe."

            cursor.execute("INSERT INTO Marcas (Nombre) VALUES (?)", (nombre,))
            conn.commit()
            return True, "Marca agregada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al agregar la marca: {str(e)}"
        finally:
            conn.close()

    def actualizar_marca(self, marca_id, nuevo_nombre):
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"
        try:
            cursor = conn.cursor()

            # Validar duplicado (excepto la misma marca)
            cursor.execute("""
                SELECT COUNT(*) 
                FROM Marcas 
                WHERE Nombre = ? AND MarcaID <> ?
            """, (nuevo_nombre, marca_id))
            if cursor.fetchone()[0] > 0:
                return False, "❌ Ya existe otra marca con ese nombre."

            cursor.execute("""
                UPDATE Marcas
                SET Nombre = ?
                WHERE MarcaID = ?
            """, (nuevo_nombre, marca_id))
            conn.commit()
            return True, "Marca actualizada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al actualizar la marca: {str(e)}"
        finally:
            conn.close()

    def eliminar_marca(self, marca_id):
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"
        try:
            cursor = conn.cursor()

            # Soft delete → si tu tabla tiene campo Estado
            cursor.execute("""
                UPDATE Marcas
                SET Estado = 0
                WHERE MarcaID = ?
            """, (marca_id,))
            conn.commit()
            return True, "Marca eliminada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al eliminar la marca: {str(e)}"
        finally:
            conn.close()
        
    # ----------------------------
# MÉTODOS PARA CATEGORÍAS
# ----------------------------
    def agregar_categoria(self, nombre):
        """
        Agrega una nueva categoría a la base de datos.
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"
        try:
            cursor = conn.cursor()

            # Validar duplicado
            cursor.execute("SELECT COUNT(*) FROM Categorias WHERE Nombre = ?", (nombre,))
            if cursor.fetchone()[0] > 0:
                return False, "❌ La categoría ya existe."

            cursor.execute("INSERT INTO Categorias (Nombre) VALUES (?)", (nombre,))
            conn.commit()
            return True, "Categoría agregada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al agregar la categoría: {str(e)}"
        finally:
            conn.close()


    def actualizar_categoria(self, categoria_id, nuevo_nombre):
        """
        Actualiza el nombre de una categoría existente.
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"
        try:
            cursor = conn.cursor()

            # Validar duplicado (excepto la misma categoría)
            cursor.execute("""
                SELECT COUNT(*) 
                FROM Categorias 
                WHERE Nombre = ? AND CategoriaID <> ?
            """, (nuevo_nombre, categoria_id))
            if cursor.fetchone()[0] > 0:
                return False, "❌ Ya existe otra categoría con ese nombre."

            cursor.execute("""
                UPDATE Categorias
                SET Nombre = ?
                WHERE CategoriaID = ?
            """, (nuevo_nombre, categoria_id))
            conn.commit()
            return True, "Categoría actualizada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al actualizar la categoría: {str(e)}"
        finally:
            conn.close()


    def eliminar_categoria(self, categoria_id):
        """
        Desactiva una categoría (soft delete) cambiando Estado a 0.
        """
        conn = self.connect()
        if not conn:
            return False, "Error de conexión"

        try:
            cursor = conn.cursor()
            # Suponiendo que la tabla Categorias tiene un campo 'Estado'
            cursor.execute("""
                UPDATE Categorias
                SET Estado = 0
                WHERE CategoriaID = ?
            """, (categoria_id,))
            conn.commit()
            return True, "Categoría eliminada correctamente."
        except Exception as e:
            conn.rollback()
            return False, f"Ocurrió un error al eliminar la categoría: {str(e)}"
        finally:
            conn.close()


    def obtener_categorias(self):
        """
        Obtiene todas las categorías activas.
        """
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT CategoriaID, Nombre
                FROM Categorias
                WHERE Estado = 1
                ORDER BY CategoriaID
            """)
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    # ----------------------------
    # MÉTODOS PARA VENTAS E HISTÓRICO
    # ----------------------------
    def obtener_empleados(self):
        """
        Retorna lista de empleados activos para filtros.
        """
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT EmpleadoID, Nombre
                FROM Empleados
                WHERE Estado = 1
                ORDER BY Nombre
            """)
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_ventas(self, fecha_ini, fecha_fin, empleado_id=None):
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()

            query = """
                SELECT v.VentaID,
                       v.FechaVenta,
                       e.Nombre AS Empleado,
                       v.Total
                FROM Ventas v
                INNER JOIN Empleados e ON v.EmpleadoID = e.EmpleadoID
                WHERE v.FechaVenta BETWEEN ? AND ?
            """
            params = [fecha_ini, fecha_fin]

            if empleado_id:
                query += " AND v.EmpleadoID = ?"
                params.append(empleado_id)

            query += " ORDER BY v.FechaVenta DESC"

            cursor.execute(query, params)
            rows = cursor.fetchall()   # ✅ primero guardamos
            return rows
        finally:
            conn.close()

    def obtener_detalle_venta(self, venta_id):
        """
        Retorna detalle de una venta con productos.
        """
        conn = self.connect()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.Nombre, dv.Cantidad, p.Precio, (dv.Cantidad * p.Precio) AS Subtotal
                FROM DetalleVenta dv
                INNER JOIN Productos p ON dv.ProductoID = p.ProductoID
                WHERE dv.VentaID = ?
            """, (venta_id,))
            return cursor.fetchall()
        finally:
            conn.close()

#TODOESTO ES PARA VER STOCK
    def get_all_products(self):
        """Devuelve todos los productos"""
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            query = """
            SELECT 
                ProductoID,
                Nombre,
                Presentacion,
                CodigoBarras,
                Categoria,
                Marca,
                Precio
            FROM Productos
            """
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"[ERROR get_all_products] {e}")
            return []
        finally:
            conn.close()

    def search_products(self, nombre):
        """Busca productos por nombre parcial"""
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            query = """
            SELECT 
                ProductoID,
                Nombre,
                Presentacion,
                CodigoBarras,
                Categoria,
                Marca,
                Precio
            FROM Productos
            WHERE Nombre LIKE ?
            """
            cursor.execute(query, (f"%{nombre}%",))
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"[ERROR search_products] {e}")
            return []
        finally:
            conn.close()

    def obtener_inventario_completo(self):
        """Devuelve ProductoID, Nombre y StockActual del inventario."""
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            query = """
            SELECT i.ProductoID, p.Nombre, i.StockActual
            FROM Inventario i
            INNER JOIN Productos p ON i.ProductoID = p.ProductoID
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"[ERROR obtener_inventario_completo] {e}")
            return []
        finally:
            conn.close()

    def buscar_inventario_por_nombre(self, nombre):
        """Busca en el inventario por nombre de producto (coincidencia parcial)."""
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            query = """
            SELECT i.ProductoID, p.Nombre, i.StockActual
            FROM Inventario i
            INNER JOIN Productos p ON i.ProductoID = p.ProductoID
            WHERE p.Nombre LIKE ?
            """
            cursor.execute(query, (f"%{nombre}%",))
            return cursor.fetchall()
        except Exception as e:
            print(f"[ERROR buscar_inventario_por_nombre] {e}")
            return []
        finally:
            conn.close()

    def agregar_stock(self, producto_id, cantidad):
        """Suma una cantidad positiva al stock de un producto existente."""
        if cantidad <= 0:
            print("[ERROR agregar_stock] La cantidad debe ser mayor que cero.")
            return False

        conn = self.connect()
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            query = """
            UPDATE Inventario
            SET StockActual = StockActual + ?
            WHERE ProductoID = ?
            """
            cursor.execute(query, (cantidad, producto_id))
            conn.commit()

            if cursor.rowcount == 0:
                print("[WARN agregar_stock] No se encontró el producto especificado.")
                return False

            print(f"[INFO] Stock actualizado correctamente (+{cantidad}).")
            return True

        except Exception as e:
            print(f"[ERROR agregar_stock] {e}")
            return False

    def registrar_movimiento(self, producto_id, cantidad, tipo_movimiento, empleado_id):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO MovimientosInventario (ProductoID, Cantidad, TipoMovimiento, FechaMovimiento, EmpleadoID)
                    VALUES (?, ?, ?, GETDATE(), ?)
                """, (producto_id, cantidad, tipo_movimiento, empleado_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"[ERROR registrar_movimiento] {e}")
            return False