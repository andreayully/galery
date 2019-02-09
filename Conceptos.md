## Solución conceptual
- Se tiene un servicio web sobre https, por políticas de seguridad todas las cookies tienen las cabeceras httpsOnly true, same-origin strict y secure true. Bajo estas condiciones, explique de qué manera podría realizar peticiones tipo post a una aplicación de django sin usar el decorador @csrf_exempt.


  **R/:** En settings.py esta activado por defecto en el *MIDDLEWARE*. Para no utilizar el decorador *@csrf_exempt*, en cualquier template que realiza peticiones tipo *POST*, se utiliza el tag  **csrf_token** dentro del <form>

    ``` <form method="post">{% csrf_token %} ```

- Se tiene una aplicación web que permite al usuario subir vídeos en cualquier formato y calidad, estos vídeos deben poder reproducirse con html5 de manera fluida sin plugins adicionales. cómo solucionaría usted el problema? los criterios para la solución son: escalabilidad, uso de recursos computacionales, experiencia de usuario, disponibilidad de servicio.

  **R/** HTMl5 cuenta con la etiqueta   ``` <video> ``` que tiene como funcionalidad crear reproductor para visualizar videos en una página web y establece un estándar para embeber videos.

    ```
    <video width="600" height="400">
      <source src="video.mp4" type="video/mp4">
      </video>
      ```
