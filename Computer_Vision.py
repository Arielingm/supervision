import cv2
from ultralytics import YOLO
import supervision as sv
import numpy as np

# Configuración de la cámara IP
username = "admin"
password = "900-TIA2022-rn"
ip = "172.27.206.202"
ch = "5"
url=f"rtsp://{username}:{password}@{ip}:554/ISAPI/Streaming/channels/{ch}01/picture?snapShotImageType=JPEG"
# Cambiar a un archivo de video local o a una cámara web según sea necesario
# video = cv2.VideoCapture("/ruta/video/path")
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture(url) 

# Configuración del modelo YOLO
model=YOLO('yolov8n.pt')
# Configuración de objetos para la supervisión
byte_track = sv.ByteTrack()


# Definición de polígonos
P_ZONE_IN   = np.array([[610,264],[640,279],[604,512],[558,569],[202,421],
                        [199,361],[256,279],[296,269],[290,166],[321,178],
                        [321,178],[322,177],[320,323],[571,406]])
        
P_ZONE_OUT  = np.array([[323, 321],[322,321],[326,166],[614,232],[569,398]])

ZONE_IN     = sv.PolygonZone(P_ZONE_IN,(640,640))
ZONE_OUT    = sv.PolygonZone(P_ZONE_OUT,(640,640))

zone_annotor_in     = sv.PolygonZoneAnnotator(ZONE_IN,sv.Color.RED)
zone_annotor_out    = sv.PolygonZoneAnnotator(ZONE_OUT,sv.Color.BLUE)

# Definición de Linea
LINE_START  = sv.Point(240, 270)
LINE_END    = sv.Point(611,409)

Linea_count = sv.LineZone(start=LINE_START, end=LINE_END,triggering_anchors=[sv.Position.CENTER])
count       = sv.LineZoneAnnotator()

# Creación de Anotadores
bounding_box_annotator  = sv.BoundingBoxAnnotator()
label_annotator         = sv.LabelAnnotator(text_scale=0.4)
trace_annotator         = sv.TraceAnnotator()


# Bucle principal de supervisión
while video.isOpened():
    ret, frame =video.read()# Nos retorna un valor booleano y un fotograma del video
    if ret:
        frame       = cv2.resize(frame, (640, 640))
        results     = model(frame, verbose=False)[0]
        detections  = sv.Detections.from_ultralytics(results)
        detections  = detections[detections.class_id==0]
        detections  = byte_track.update_with_detections(detections=detections)
         # Acttualiza las Zonas y La lineeas
        ZONE_IN.trigger(detections=detections)
        ZONE_OUT.trigger(detections=detections)
        Linea_count.trigger(detections=detections)

        bounding_box_annotator.annotate(scene=frame,detections=detections)
        labels      = [f"#{tracker_id} {results.names[class_id]}" for class_id, tracker_id in 
                       zip(detections.class_id, detections.tracker_id)]
        # Anotadores visuales para el frame
        label_annotator.annotate(frame, detections=detections, labels=labels)
        trace_annotator.annotate(frame, detections)
        zone_annotor_in.annotate(frame)
        zone_annotor_out.annotate(frame)
        count.annotate(frame=frame, line_counter=Linea_count)
        cv2.imshow('supervision',frame)
        if(cv2.waitKey(1)==ord('q')): # Salir del bucle en cualquir momento si se presiona la tecla 'q' 
            break

    else:
        break
# Liberar recursos al finalizar
video.release()
cv2.destroyAllWindows()