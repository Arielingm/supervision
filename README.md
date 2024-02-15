# Proyecto de Conteo de Personas en Local Comercial (Demo)

Este proyecto es una simplificación de un sistema de conteo de personas en un local comercial de TIA S.A. El propósito es poner a prueba las capacidades de la librería Supervision y explorar su funcionalidad en el contexto de programación de proyectos de visión por computadora.

## Librerías Utilizadas

- **OpenCV (opencv-python==4.9.0.80)** 
- **Supervision (supervision==0.18.0)** 
- **Ultralytics (ultralytics==8.1.9)** 

## Funcionalidades y Clases Principales

### LineZone

Esta clase es responsable de contar el número de objetos que cruzan una línea predefinida en el video. Se utiliza para evaluar el flujo de personas entrando o saliendo del local.

### PolygonZone

La clase `PolygonZone` se encarga de definir una zona poligonal dentro de un fotograma para detectar objetos. Puede ser utilizada para identificar la presencia de personas en áreas específicas del local.

## Uso y Adaptabilidad

El código proporcionado es una demostración básica y puede ser adaptado para diferentes escenarios y proyectos. La implementación de las clases `LineZone` y `PolygonZone` muestra cómo utilizar estas funcionalidades para el conteo y la detección de objetos en un entorno específico.

## Requisitos

Asegúrate de tener las siguientes versiones de las librerías instaladas:

- opencv-python==4.9.0.80
- supervision==0.18.0
- ultralytics==8.1.9

## Demostración

![Video de Demostración](video_demostracion.gif)

Para ver el video completo, puedes descargarlo [aquí]([enlace_del_video.mp4](https://youtube.com/shorts/c1dGFykvpVU?feature=share)).

---

Este proyecto fue creado como parte de una exploración de la librería Supervision y puede servir como punto de partida para proyectos más complejos de visión por computadora. ¡Diviértete explorando y mejorando este código para tus propias necesidades!
