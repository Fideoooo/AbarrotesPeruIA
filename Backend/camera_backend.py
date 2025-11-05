from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import torch
import time
from ultralytics import YOLO
from Backend.database import Database

class CameraThread(QThread):
    producto_detectado_signal = pyqtSignal(dict)  # Emite info del producto detectado

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        self.model = YOLO(r"F:\Tesis\Datasets\runs\detect\train\weights\best.pt")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tiempo_confirmacion = 5  # segundos

    def parse_producto(self, nombre_detectado):
        partes = nombre_detectado.split("_")

        if len(partes) == 4:
            nombre = partes[0]
            categoria = partes[1]
            marca = partes[2]
            presentacion = partes[3]
        else:
            #fallback si no cumple
            nombre = nombre_detectado
            categoria = "Desconocida"
            marca = "Desconocida"
            presentacion = "N/A"

        return {
            "nombre": nombre,
            "categoria": categoria,
            "marca": marca,
            "presentacion": presentacion
        }

    def run(self):
        cap = cv2.VideoCapture(0)
        ultimo_producto = None
        tiempo_inicio = None

        while self.running:
            ret, frame = cap.read()
            if not ret:
                continue

            resultados = self.model.predict(frame, imgsz=640, conf=0.85)
            anotaciones = resultados[0].plot()
            cv2.imshow("DETECCIÓN Y SEGMENTACIÓN", anotaciones)

            # Tomamos la primer detección si hay
            if len(resultados[0].boxes) > 0:
                box = resultados[0].boxes[0]
                cls_id = int(box.cls[0])
                nombre_detectado = resultados[0].names[cls_id]

                producto = self.parse_producto(nombre_detectado)

                # Comparar con último producto detectado
                if ultimo_producto == nombre_detectado:
                    if tiempo_inicio is None:
                        tiempo_inicio = time.time()
                    elif time.time() - tiempo_inicio >= self.tiempo_confirmacion:
                        self.running = False  # Congela cámara
                        self.producto_detectado_signal.emit(producto)
                        tiempo_inicio = None
                        ultimo_producto = None
                        # Espera que la GUI reanude la cámara
                else:
                    ultimo_producto = nombre_detectado
                    tiempo_inicio = time.time()
            else:
                ultimo_producto = None
                tiempo_inicio = None

            if cv2.waitKey(1) & 0xFF == 27:
                self.running = False
                break

        cap.release()
        cv2.destroyAllWindows()