Familiarizarse con los datos (limpios)
    return resumen de los datos (ej. cantidad de datos, formato, tamaño, formato de las labels, histograma de labels)

Familiarizarte con el problema
    Que es lo que quiero resolver?
    De que manera lo quiero resolver
    Que metricas voy a usar para evaluar si resuelvo bien o mal el problema
    Definir valores de las metricas para considerar el problema "resuelto"
    return un primer modelo a partir del cual puedo iterar
    
    + metricas de cuan bien el modelo soluciona el problema

Armamos el pipeline para entrenar y crear el modelo final
    Levantamos los datos
    Entreno el modelo
    Evaluamos el modelo
    return pipeline de trabajo

Iteramos el modelo inicial
    return modelo a usar en produccion

Durante produccion... ¿que m... pasa?
    -le dan uso a la aplicacion + el modelo
    - Seguramente aparecen problemas o comentarios, posibles mejoras
    - Se generan datos del uso del modelo en produccion que tenemos que elegir que guardar y como.

    return 
        (algo que me hace volver a iterar al paso ??
        Usar los datos que generamos en produccion para evaluar la performance del modelo (segun las metricas ya definidas.). 
        Si esta por debajo de lo satisfactorio hay que iterar:
        Agregar mas datos?
        Probar con otras arquitecturas?
        Cambiar algo en el entrenamiento? Cambiar los parametros del entrenamiento (epocas, learning rate, momentum), probar con otro algoritmo de optimizacion?
        or
        algo que me dice, listo, vamos a otro proyecto)



Lo que va a produccion es el modelo + alguna manera de recopilar los datos
lo que va a produccion es el modelo + alguna manera de que me vuelva un output para poder iterar sobre el proceso. Datos, mediciones, metricas
lo que va a produccion es el modelo + algunas metricas que se evaluan en produccion, + datos que me vuelven para poder iterar sobre el proceso. Datos sobre las evaluaciones del modelo + entrevistas/charlas con al gente que lo usa.


