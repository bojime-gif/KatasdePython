{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c9f57b93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'H': 1, 'o': 1, 'l': 2, 'a': 2, 'q': 1, 'u': 1, 'e': 1, 't': 1}\n"
     ]
    }
   ],
   "source": [
    "# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados. #\n",
    "\n",
    "def frecuencia_letras(cadena):\n",
    "    frecuencia = {}\n",
    "    for letra in cadena:\n",
    "        if letra != \" \":\n",
    "            if letra in frecuencia:\n",
    "                frecuencia[letra] +=1\n",
    "            else:\n",
    "                frecuencia[letra] =1\n",
    "    return frecuencia\n",
    "\n",
    "texto = \"Hola que tal\"\n",
    "resultado = frecuencia_letras(texto)\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7324e5e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La lista original antes de obtener el doble de cada numero es: [1, 2, 3, 4, 5]\n",
      "El resultado de la funcion map despues de convertirlo a lista es [2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map() #\n",
    "\n",
    "def lista_numeros(num):\n",
    "    return num*2\n",
    "\n",
    "numeros = [1,2,3,4,5]\n",
    "print(f\"La lista original antes de obtener el doble de cada numero es: {numeros}\")\n",
    "\n",
    "resultado_map = map(lista_numeros,numeros)\n",
    "\n",
    "lista_resultado_map = list(map(lista_numeros,numeros))\n",
    "print(f\"El resultado de la funcion map despues de convertirlo a lista es {lista_resultado_map}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fe84f72c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['lampara']\n"
     ]
    }
   ],
   "source": [
    "# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan \n",
    "# la palabra objetivo. #\n",
    "\n",
    "def lista_palabras(lista, objetivo):\n",
    "    coincidencias = []\n",
    "    for palabra in lista:\n",
    "        if objetivo in palabra:\n",
    "            coincidencias.append(palabra)\n",
    "    return list(coincidencias)\n",
    "\n",
    "ejemplo = [\"escritorio\", \"lampara\", \"silla\", \"ordenador\", \"teclado\"]\n",
    "palabra_objetivo = \"lampara\"\n",
    "\n",
    "resultado_objetivo = lista_palabras(ejemplo, palabra_objetivo)\n",
    "print(resultado_objetivo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a69f8125",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[70, 55, 5, 8]\n"
     ]
    }
   ],
   "source": [
    "# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map() #\n",
    "\n",
    "def restar(a, b):\n",
    "    return a-b\n",
    "\n",
    "lista1 = [80, 60, 20, 10]\n",
    "lista2 = [10, 5, 15, 2]\n",
    "\n",
    "resultado = list(map(restar, lista1, lista2))\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6cca292",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4.625, 'suspenso')\n"
     ]
    }
   ],
   "source": [
    "# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será \"aprobado\", de lo contrario, será \"suspenso\". La función debe devolver una tupla que contenga la media y el estado. #\n",
    "\n",
    "def calculo_media (nota, nota_aprobado = 5):\n",
    "    media = sum(nota) / len(nota)\n",
    "\n",
    "    if media >= nota_aprobado:\n",
    "        estado = \"aprobado\"\n",
    "    else:\n",
    "        estado = \"suspenso\"\n",
    "    return media, estado\n",
    "\n",
    "notas = [8, 4, 2, 9, 4, 6, 3, 1]\n",
    "resultado = calculo_media(notas)\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6406649a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El factorial de 8 es: 40320\n"
     ]
    }
   ],
   "source": [
    "# 6. Escribe una función que calcule el factorial de un número de manera recursiva. #\n",
    "\n",
    "def factorial(n):\n",
    "    if n == 0 or n ==1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n * factorial(n-1)\n",
    "\n",
    "numer = 8\n",
    "result = factorial(numer)\n",
    "\n",
    "print(f\"El factorial de {numer} es: {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "312eb5f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['(1, 2)', '(3, 4)', '(5, 6)']\n"
     ]
    }
   ],
   "source": [
    "# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map() #\n",
    "\n",
    "mi_tupla = [(1, 2), (3, 4), (5,6)]\n",
    "\n",
    "lista_string = list(map(str, mi_tupla))\n",
    "\n",
    "print(lista_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c99b9fcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No se puede dividir por cero\n"
     ]
    }
   ],
   "source": [
    "# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no. #\n",
    "\n",
    "try:\n",
    "\n",
    "    numero1 = int(input(\"Dime un número\"))\n",
    "    numero2 = int(input(\"Dime otro número\"))\n",
    "    division = numero1 / numero2\n",
    "\n",
    "    print(f\"El resultado de la división es {division} \")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Por favor, ingrese un número válido\")\n",
    "\n",
    "except ZeroDivisionError:\n",
    "    print(\"No se puede dividir por cero\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e826160d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mascotas permitidas: ['Perro', 'Gato', 'Periquito', 'Oso Hormiguero']\n"
     ]
    }
   ],
   "source": [
    "# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es [\"Mapache\", \"Tigre\", \"Serpiente Pitón\", \"Cocodrilo\", \"Oso\"].Usa la función filter() #\n",
    "\n",
    "def mascotas_permitidas(lista_mascotas):\n",
    "    mascotas_prohibidas = [\"Mapache\", \"Tigre\", \"Serpiente Pitón\", \"Cocodrilo\", \"Oso\"]\n",
    "\n",
    "    permitidas = filter (lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)\n",
    "\n",
    "    return list(permitidas)\n",
    "\n",
    "lista_mascotas_ejemplo = [\"Perro\", \"Gato\", \"Periquito\", \"Tigre\", \"Oso Hormiguero\", \"Mapache\"]\n",
    "resultado = mascotas_permitidas(lista_mascotas_ejemplo)\n",
    "print(f\"Mascotas permitidas: {resultado}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "e5954fc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El promedio es 2.0\n"
     ]
    }
   ],
   "source": [
    "# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente. #\n",
    "\n",
    "class ListaVaciaError(Exception):\n",
    "    pass\n",
    "\n",
    "def funcion(numeros):\n",
    "    if not numeros:\n",
    "        raise ListaVaciaError (\"No se puede calcular el promedio porque la lista está vacia\")\n",
    "    return sum(numeros) / len(numeros)\n",
    "\n",
    "lista_numeros_ejemplo = [1, 2, 3]\n",
    "\n",
    "try:\n",
    "    promedio = funcion(lista_numeros_ejemplo)\n",
    "    print(f\"El promedio es {promedio}\")\n",
    "except ListaVaciaError as error:\n",
    "    print(f\"La lista está vacia\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7a62199b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Entrada no válida La edad debe estar entre 0 y 120 años\n"
     ]
    }
   ],
   "source": [
    "# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente. #\n",
    "\n",
    "def preguntar_edad():\n",
    "\n",
    "    try: \n",
    "        edad = int(input(\"Dime tu edad: \"))\n",
    "\n",
    "        if edad < 0 or edad > 120:\n",
    "            raise ValueError(f\"La edad debe estar entre 0 y 120 años\")\n",
    "\n",
    "    except ValueError as e:\n",
    "        print(f\"Error: Entrada no válida {e}\")\n",
    "\n",
    "    else:\n",
    "        print(f\"Tu edad es {edad}\")\n",
    "\n",
    "preguntar_edad()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "dfdbbf59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 3, 3]\n"
     ]
    }
   ],
   "source": [
    "# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() #\n",
    "\n",
    "def longitud_frase(frase):\n",
    "    palabras = []\n",
    "    palabra_actual = \"\"\n",
    "\n",
    "    for caracter in frase:\n",
    "        if caracter != \" \":\n",
    "            palabra_actual += caracter\n",
    "        elif palabra_actual:\n",
    "            palabras.append(palabra_actual)\n",
    "            palabra_actual = \"\"\n",
    "\n",
    "    if palabra_actual:\n",
    "        palabras.append(palabra_actual)\n",
    "\n",
    "    return palabras\n",
    "\n",
    "def longitud_palabras(frase):\n",
    "    palabras =longitud_frase(frase)\n",
    "\n",
    "    return list(map(len, palabras))\n",
    "\n",
    "texto = \"Hola que tal\"\n",
    "print(longitud_palabras(texto))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "61361904",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('A', 'a'), ('O', 'o'), ('H', 'h'), ('L', 'l')]\n"
     ]
    }
   ],
   "source": [
    "# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() #\n",
    "\n",
    "def mayusminus(texto):\n",
    "    tuplas = map(lambda c: (c.upper(), c.lower()), set(texto))\n",
    "    return list(tuplas)\n",
    "\n",
    "ejemplo1 = \"hola\" \n",
    "print(mayusminus(ejemplo1))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "06826542",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palabras que empiezan por a: ['Avion', 'Astronauta', 'Arbol', 'Asterisco']\n"
     ]
    }
   ],
   "source": [
    "# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter() #\n",
    "\n",
    "def filtro_por_letra(lista_palabras, letra):\n",
    "    letra = letra.lower()\n",
    "    palabras_filtradas = filter (lambda palabra: palabra.lower().startswith(letra), lista_palabras)\n",
    "\n",
    "    return list(palabras_filtradas)\n",
    "\n",
    "palabras_ejemplo = [\"Avion\", \"Astronauta\", \"Arbol\", \"Pan\", \"Huevos\", \"Asterisco\"]\n",
    "letra_busqueda = \"a\"\n",
    "\n",
    "resultado = filtro_por_letra(palabras_ejemplo, letra_busqueda)\n",
    "print(f\"Palabras que empiezan por {letra_busqueda}: {resultado}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e6f97ca7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 13, 23, 83]\n"
     ]
    }
   ],
   "source": [
    "# 15. Crea una función lambda que sume 3 a cada número de una lista dada. #\n",
    "\n",
    "def suma_tres(numeros):\n",
    "    resultado = map(lambda x: x +3, numeros)\n",
    "    return list(resultado)\n",
    "\n",
    "lista_ejemplo1 = [4, 10, 20, 80]\n",
    "lista_suma = suma_tres(lista_ejemplo1)\n",
    "print(lista_suma)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1931d269",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palabras con más de 4: ['frase', 'ejemplo', 'estamos', 'utilizando', 'ejercicio', 'dieciseis']\n"
     ]
    }
   ],
   "source": [
    "# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter() #\n",
    "\n",
    "def palabra_mas_larga(texto, n):\n",
    "    palabras = texto.split()\n",
    "\n",
    "    resultado_filter = filter(lambda palabra: len(palabra) > n, palabras)\n",
    "\n",
    "    return list(resultado_filter)\n",
    "\n",
    "frase = \"Esta es una frase de ejemplo que estamos utilizando para el ejercicio dieciseis\"\n",
    "longitud_minima = 4\n",
    "\n",
    "resultado = palabra_mas_larga(frase, longitud_minima)\n",
    "\n",
    "print(f\"Palabras con más de {longitud_minima}: {resultado}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7865cccb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista de digitos: ['8', '7', '4', '1', '2', '3', '6']\n"
     ]
    }
   ],
   "source": [
    "# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce() #\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "def digitos_a_numero(lista):\n",
    "\n",
    "    return reduce (lambda acc, x: acc * 10 + x, lista)\n",
    "\n",
    "lista_digitos2 = list(\"8741236\")\n",
    "print(\"Lista de digitos:\", lista_digitos2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "890af36e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'nombre': 'Joan', 'edad': 24, 'calificacion': 93}, {'nombre': 'Julia', 'edad': 44, 'calificacion': 91}, {'nombre': 'Kevin', 'edad': 50, 'calificacion': 95}]\n"
     ]
    }
   ],
   "source": [
    "# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter() #\n",
    "\n",
    "mi_diccionario = [\n",
    "    {\"nombre\": \"Joan\", \"edad\": 24, \"calificacion\": 93},\n",
    "    {\"nombre\": \"Pepe\", \"edad\": 18, \"calificacion\": 24},\n",
    "    {\"nombre\": \"Julia\", \"edad\": 44, \"calificacion\": 91},\n",
    "    {\"nombre\": \"Anastasia\", \"edad\": 33, \"calificacion\": 89},\n",
    "    {\"nombre\": \"Kevin\", \"edad\": 50, \"calificacion\": 95},\n",
    "]\n",
    "\n",
    "def filtrar_notas(estudiantes):\n",
    "    resultado_filter = filter(lambda estudiante: estudiante[\"calificacion\"] >= 90, estudiantes)\n",
    "\n",
    "    return list(resultado_filter)\n",
    "\n",
    "comprobacion = filtrar_notas(mi_diccionario)\n",
    "print(comprobacion)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6d718960",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "# 19. Crea una función lambda que filtre los números impares de una lista dada. #\n",
    "\n",
    "def es_impar(lista):\n",
    "    impares = []\n",
    "    for elemento in lista:\n",
    "        if elemento% 2 != 0:\n",
    "            impares.append(elemento)\n",
    "        else:\n",
    "            pass\n",
    "    return impares\n",
    "\n",
    "lista_prueba = [1, 4, 3, 7, 9, 10]\n",
    "lista_impares = es_impar(lista_prueba)\n",
    "print(lista_impares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5bc04e56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista de enteros: [8, 5, 42, 0, -8]\n"
     ]
    }
   ],
   "source": [
    "# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter() #\n",
    "\n",
    "def filtrar_enteros(lista):\n",
    "    resultado_filter = filter(lambda x: isinstance(x, int), lista)\n",
    "    return list(resultado_filter)\n",
    "\n",
    "\n",
    "lista_integer_string = [8, \"hola\", 5, \"Python\", 42, \"100\", 0, -8]\n",
    "lista_enteros = filtrar_enteros(lista_integer_string)\n",
    "\n",
    "print(f\"Lista de enteros: {lista_enteros}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "91a9e187",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "64\n"
     ]
    }
   ],
   "source": [
    "# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda #\n",
    "\n",
    "cubo = lambda x: x**3\n",
    "print(cubo(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "777610a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1920\n"
     ]
    }
   ],
   "source": [
    "# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() . #\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "def producto_total(lista):\n",
    "    return reduce(lambda acc, x: acc * x, lista)\n",
    "\n",
    "numeros = [4, 6, 8, 10]\n",
    "resultado = producto_total(numeros)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e5726b12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estoy haciendo el ejercicio 23\n"
     ]
    }
   ],
   "source": [
    "# 23. Concatena una lista de palabras.Usa la función reduce() . #\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "lista_palabras2 = [\"Estoy\", \"haciendo\", \"el\", \"ejercicio\", \"23\"]\n",
    "\n",
    "texto = reduce(lambda acc, x: acc + \" \" + x, lista_palabras2)\n",
    "\n",
    "print(texto)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "46943c4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "570\n"
     ]
    }
   ],
   "source": [
    "# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() . #\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "lista_valores = [800, 200, 20, 10]\n",
    "\n",
    "def diferencia_total(lista):\n",
    "    return reduce(lambda acc, x: acc - x, lista)\n",
    "\n",
    "resultado = diferencia_total(lista_valores)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "922e0a61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada. #\n",
    "\n",
    "def contar_caracteres(texto):\n",
    "    texto_sin_espacios = texto.replace(\" \", \"\")\n",
    "    return len(texto_sin_espacios)\n",
    "\n",
    "prueba = \"Me llamo Borja\"\n",
    "resultado = contar_caracteres(prueba)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8e168c7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "# 26. Crea una función lambda que calcule el resto de la división entre dos números dados. #\n",
    "\n",
    "resto = lambda a, b: a % b\n",
    "\n",
    "print(resto(20, 2))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b153b5a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40.0\n"
     ]
    }
   ],
   "source": [
    "# 27. Crea una función que calcule el promedio de una lista de números. #\n",
    "\n",
    "def promedio(lista):\n",
    "    return sum(lista) / len(lista)\n",
    "\n",
    "numeros = [10, 80, 50, 20]\n",
    "\n",
    "calcular_promedio = promedio(numeros)\n",
    "print(calcular_promedio)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "09facc3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada. #\n",
    "\n",
    "def primer_duplicado(lista):\n",
    "    visto = set()\n",
    "\n",
    "    for elemento in lista:\n",
    "        if elemento in visto:\n",
    "            return elemento\n",
    "        visto.add(elemento)\n",
    "\n",
    "    return None\n",
    "\n",
    "numeros = [8, 22, 6, 7, 22, 8, 4]\n",
    "\n",
    "resultado = primer_duplicado(numeros)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ae7a45b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "####8745\n"
     ]
    }
   ],
   "source": [
    "# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro. #\n",
    "\n",
    "def enmascarar(elemento):\n",
    "    texto = str(elemento)\n",
    "\n",
    "    return \"#\" * (len(texto) -4) + texto[-4:]\n",
    "\n",
    "datos = 19838745\n",
    "resultado = enmascarar(datos)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7e28a3f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¿Asco y Saco son anagramas?: True\n",
      "¿Sergio y Riesgo son anagramas?: True\n",
      "¿Hola y Adios son anagramas?: False\n"
     ]
    }
   ],
   "source": [
    "# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden. #\n",
    "\n",
    "def son_anagramas(palabra1, palabra2):\n",
    "    p1 = str(palabra1).lower().replace(\" \", \"\")\n",
    "    p2 = str(palabra2).lower().replace(\" \", \"\")\n",
    "\n",
    "    return sorted(p1) == sorted(p2)\n",
    "\n",
    "ejemplos = [\n",
    "    (\"Asco\", \"Saco\"),\n",
    "    (\"Sergio\", \"Riesgo\"),\n",
    "    (\"Hola\", \"Adios\")\n",
    "]\n",
    "\n",
    "for p1, p2 in ejemplos:\n",
    "    es_anagrama = son_anagramas(p1, p2)\n",
    "    print(f\"¿{p1} y {p2} son anagramas?: {es_anagrama}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e3f19efa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El nombre Carlos está presente en la lista\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción. #\n",
    "\n",
    "def buscar_nombre():\n",
    "    preguntar_nombre = input(\"Introduce una serie de nombres separados por comas: \")\n",
    "\n",
    "    nombres = [nombre.strip() for nombre in preguntar_nombre.split(\",\")]\n",
    "\n",
    "    nombre_a_buscar = input(\"Escribe el nombre que quieres buscar: \")\n",
    "\n",
    "    if nombre_a_buscar in nombres:\n",
    "        print(f\"El nombre {nombre_a_buscar} está presente en la lista\")\n",
    "    else:\n",
    "        raise ValueError (f\"El nombre {nombre_a_buscar} no está presente en la lista\")\n",
    "\n",
    "prueba = buscar_nombre()\n",
    "print(prueba)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2b4e749b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ejecutivo\n"
     ]
    }
   ],
   "source": [
    "# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí. #\n",
    "\n",
    "empleados = {\n",
    "    \"Julián Ramírez\": \"Ejecutivo\",\n",
    "    \"Adrián Pérez\": \"Operario\",\n",
    "    \"Antonio López\": \"Director\",\n",
    "    \"Esteban Martínez\": \"Secretario\",\n",
    "}\n",
    "\n",
    "def buscar_empleado(nombre, lista_empleados):\n",
    "    return lista_empleados.get(nombre, f\"La persona {nombre} no trabaja aquí\")\n",
    "\n",
    "print(buscar_empleado(\"Julián Ramírez\", empleados))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e054c9b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9, 22, 8]\n"
     ]
    }
   ],
   "source": [
    "# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas. #\n",
    "\n",
    "lista1 = [8, 20, 3]\n",
    "lista2 = [1, 2, 5]\n",
    "\n",
    "sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))\n",
    "\n",
    "resultado = sumar_listas(lista1, lista2)\n",
    "\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c272b3b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- INFORMACIÓN DEL ÁRBOL ---\n",
      "Longitud del tronco: 2\n",
      "Número de ramas:    2\n",
      "Longitudes ramas:   [2, 1]\n"
     ]
    }
   ],
   "source": [
    "# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol. Código a seguir: 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas. 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad. 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas. 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes. 5. Implementar el método quitar_rama para eliminar una rama en una posición específica. 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas. Caso de uso: 1. Crear un árbol. 2. Hacer crecer el tronco del árbol una unidad. 3. Añadir una nueva rama al árbol. 4. Hacer crecer todas las ramas del árbol una unidad. 5. Añadir dos nuevas ramas al árbol. 6. Retirar la rama situada en la posición 2. 7. Obtener información sobre el árbol. #\n",
    "\n",
    "class Arbol:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.tronco = 1\n",
    "        self.ramas = []\n",
    "\n",
    "    def crecer_tronco(self):\n",
    "        self.tronco +=1\n",
    "\n",
    "    def nueva_rama(self):\n",
    "        self.ramas.append(1)\n",
    "\n",
    "    def crecer_ramas(self):\n",
    "        self.ramas = [longitud + 1 for longitud in self.ramas]\n",
    "\n",
    "    def quitar_rama(self, posicion):\n",
    "        if 0 <= posicion < len(self.ramas):\n",
    "            self.ramas.pop(posicion)\n",
    "        else:\n",
    "            print(f\"Error: la posicion {posicion} no existe en las ramas\")\n",
    "\n",
    "    def info_arbol(self):\n",
    "        return {\n",
    "            \"longitud_tronco\": self.tronco,\n",
    "            \"numero_ramas\": len(self.ramas),\n",
    "            \"longitudes_ramas\": self.ramas\n",
    "        }\n",
    "\n",
    "# --- CASO DE USO ---\n",
    "# 1. Crear un árbol\n",
    "mi_arbol = Arbol()\n",
    "\n",
    "# 2. Hacer crecer el tronco una unidad\n",
    "mi_arbol.crecer_tronco()\n",
    "\n",
    "# 3. Añadir una nueva rama\n",
    "mi_arbol.nueva_rama()\n",
    "\n",
    "# 4. Hacer crecer todas las ramas una unidad\n",
    "mi_arbol.crecer_ramas()\n",
    "\n",
    "# 5. Añadir dos nuevas ramas\n",
    "mi_arbol.nueva_rama()\n",
    "mi_arbol.nueva_rama()\n",
    "\n",
    "# 6. Retirar la rama situada en la posición 2 (índice 2)\n",
    "mi_arbol.quitar_rama(2)\n",
    "\n",
    "# 7. Obtener información sobre el árbol\n",
    "info = mi_arbol.info_arbol()\n",
    "\n",
    "print(\"--- INFORMACIÓN DEL ÁRBOL ---\")\n",
    "print(f\"Longitud del tronco: {info[\"longitud_tronco\"]}\")\n",
    "print(f\"Número de ramas:    {info[\"numero_ramas\"]}\")\n",
    "print(f\"Longitudes ramas:   {info[\"longitudes_ramas\"]}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cb74e317",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saldo inicial -> Alicia: 100, Bob: 50\n",
      "\n",
      "Se ha agregado 20 a bob. Su nuevo saldo es 70\n",
      "Transferencia realizada correctamente desde <__main__.UsuarioBanco object at 0x0000022D4391A350> a alicia\n",
      "Ha retirado 50. Su nuevo saldo es 130\n",
      "\n",
      "Saldo final -> Alicia: 130, Bob: 70\n"
     ]
    }
   ],
   "source": [
    "# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. Código a seguir: 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False . 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse. 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse. 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario. Caso de uso: 1. Crear dos usuarios: \"Alicia\" con saldo inicial de 100 y \"Bob\" con saldo inicial de 50, ambos con cuenta corriente. PROYECTO LÓGICA: Katas de Python 3 2. Agregar 20 unidades de saldo de \"Bob\". 3. Hacer una transferencia de 80 unidades desde \"Bob\" a \"Alicia\". 4. Retirar 50 unidades de saldo a \"Alicia\". #\n",
    "\n",
    "class UsuarioBanco:\n",
    "    def __init__(self, nombre, saldo, cuenta=True):\n",
    "        self.nombre = nombre\n",
    "        self.saldo = saldo\n",
    "        self.cuenta = cuenta\n",
    "\n",
    "    def retirar_dinero(self, cantidad):\n",
    "        if cantidad <=0:\n",
    "            raise ValueError(\"La cantidad a retirar debe ser mayor que 0\")\n",
    "\n",
    "        if cantidad > self.saldo:\n",
    "            raise ValueError(f\"Saldo insuficiente. Su saldo actual es {self.saldo}\")\n",
    "\n",
    "        self.saldo -= cantidad\n",
    "        print(f\"Ha retirado {cantidad}. Su nuevo saldo es {self.saldo}\")\n",
    "\n",
    "    def transferir_dinero(self, otro_usuario, cantidad):\n",
    "        if cantidad <= 0:\n",
    "            raise ValueError(\"La cantidad a transferir debe ser mayor que 0\")\n",
    "\n",
    "        self.saldo += cantidad\n",
    "        print(f\"Transferencia realizada correctamente desde {otro_usuario} a {self.nombre}\")\n",
    "\n",
    "\n",
    "    def agregar_dinero(self, cantidad):\n",
    "        if cantidad <= 0:\n",
    "            raise ValueError(\"La cantidad a agregar deber ser mayor que 0\")\n",
    "\n",
    "        self.saldo += cantidad\n",
    "        print(f\"Se ha agregado {cantidad} a {self.nombre}. Su nuevo saldo es {self.saldo}\")\n",
    "\n",
    "# --- CASO DE USO ---\n",
    "\n",
    "# 1. Crear usuarios\n",
    "alicia = UsuarioBanco(\"alicia\", 100, cuenta=True)\n",
    "bob = UsuarioBanco(\"bob\", 50, cuenta=True)\n",
    "\n",
    "print(f\"Saldo inicial -> Alicia: {alicia.saldo}, Bob: {bob.saldo}\\n\")\n",
    "\n",
    "# 2. Agregar 20 unidades de saldo a Bob\n",
    "bob.agregar_dinero(20)\n",
    "\n",
    "# 3. Transferencia de 80 unidades desde Bob a Alicia\n",
    "# (Nota: Alicia recibe la transferencia desde Bob)\n",
    "try:\n",
    "    alicia.transferir_dinero(bob, 80)\n",
    "except ValueError as e:\n",
    "    print(f\"Error en transferencia: {e}\")\n",
    "\n",
    "# 4. Retirar 50 unidades de saldo a Alicia\n",
    "alicia.retirar_dinero(50)\n",
    "\n",
    "print(f\"\\nSaldo final -> Alicia: {alicia.saldo}, Bob: {bob.saldo}\")    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a472fb60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 1. CONTAR PALABRAS ---\n",
      "{'estoy': 1, 'probando': 1, 'el': 1, 'ejercicio': 1, '37': 1}\n",
      "\n",
      "--- 2. REEMPLAZAR PALABRAS ---\n",
      "Original: Estoy probando el ejercicio 37\n",
      "Resultado: Estoy probando el enunciado 37\n",
      "\n",
      "--- 3. ELIMINAR PALABRA ---\n",
      "Original: Estoy probando el ejercicio 37\n",
      "Resultado: Estoy el ejercicio 37\n"
     ]
    }
   ],
   "source": [
    "# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . Código a seguir: 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario. 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras. 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada. 4. Crear la función procesar_texto que tome un texto, una opción(entre \"contar\", \"reemplazar\", \"eliminar\") y un número de argumentos variable según la opción indicada. Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto #\n",
    "\n",
    "def contar_palabras(texto):\n",
    "    palabras = texto.lower().split()\n",
    "    frecuencias = {}\n",
    "    for palabra in palabras:\n",
    "        palabra_limpia = palabra.strip(\".,;:!?()\")\n",
    "        frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1\n",
    "    return frecuencias\n",
    "\n",
    "def reemplazar_palabras(texto, palabra_original, palabra_nueva):\n",
    "    return texto.replace(palabra_original, palabra_nueva)\n",
    "\n",
    "def eliminar_palabra(texto, palabra_a_eliminar):\n",
    "    palabras = texto.split()\n",
    "    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]\n",
    "    return \" \".join(palabras_filtradas)\n",
    "\n",
    "def procesar_texto(texto, opcion, *args):\n",
    "    if opcion == \"contar\":\n",
    "        return contar_palabras(texto)\n",
    "\n",
    "    elif opcion == \"reemplazar\":\n",
    "        if len(args) < 2:\n",
    "            raise ValueError(\"La opción 'reemplazar' requiere dos argumentos: palabra_original y palabra_nueva.\")\n",
    "        return reemplazar_palabras(texto, args[0], args[1])\n",
    "\n",
    "    elif opcion == \"eliminar\":\n",
    "        if len(args) < 1:\n",
    "            raise ValueError(\"La opción 'eliminar' requiere un argumento: palabra_a_eliminar.\")\n",
    "        return eliminar_palabra(texto, args[0])\n",
    "\n",
    "    else:\n",
    "        raise ValueError(f\"Opción '{opcion}' no válida. Usa 'contar', 'reemplazar' o 'eliminar'.\")\n",
    "\n",
    "\n",
    "# --- CASO DE USO ---\n",
    "texto_ejemplo = \"Estoy probando el ejercicio 37\"\n",
    "\n",
    "print(\"--- 1. CONTAR PALABRAS ---\")\n",
    "resultado_contar = procesar_texto(texto_ejemplo, \"contar\")\n",
    "print(resultado_contar)\n",
    "\n",
    "print(\"\\n--- 2. REEMPLAZAR PALABRAS ---\")\n",
    "resultado_reemplazar = procesar_texto(texto_ejemplo, \"reemplazar\", \"ejercicio\", \"enunciado\")\n",
    "print(f\"Original: {texto_ejemplo}\")\n",
    "print(f\"Resultado: {resultado_reemplazar}\")\n",
    "\n",
    "print(\"\\n--- 3. ELIMINAR PALABRA ---\")\n",
    "resultado_eliminar = procesar_texto(texto_ejemplo, \"eliminar\", \"probando\")\n",
    "print(f\"Original: {texto_ejemplo}\")\n",
    "print(f\"Resultado: {resultado_eliminar}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "16588732",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Es de día\n"
     ]
    }
   ],
   "source": [
    "# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario. #\n",
    "\n",
    "def momento_dia(hora):\n",
    "\n",
    "    if hora < 0 or hora > 23:\n",
    "        return \"Hora incorrecta, el valor debe estar entre 0 y 23\"\n",
    "\n",
    "    if 6 <= hora <=12:\n",
    "        return \"Es de día\"\n",
    "    elif 13 <= hora <=20:\n",
    "        return \"Es de tarde\"\n",
    "    else:\n",
    "        return \"Es de noche\"\n",
    "\n",
    "try:\n",
    "    entrada = input(\"Indica la hora en formato de 24h: \").strip()\n",
    "    hora_usuario = int(entrada)\n",
    "\n",
    "    resultado = momento_dia(hora_usuario)\n",
    "    print(resultado)\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Error: Por favor, introduce un número entero válido\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2c2d1a9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "muy bien\n"
     ]
    }
   ],
   "source": [
    "# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: - 0 - 69 insuficiente - 70 - 79 bien - 80 - 89 muy bien - 90 - 100 excelente #\n",
    "\n",
    "def calificacion_estudiante(nota):\n",
    "\n",
    "    if nota < 0 or nota > 100:\n",
    "        return \"Valor inválido, por favor introduce una calificación entre 0 y 100\"\n",
    "\n",
    "    if 0 <= nota <=69:\n",
    "        return \"insuficiente\"\n",
    "    elif 70 <= nota <=79:\n",
    "        return \"bien\"\n",
    "    elif 80 <= nota <=89:\n",
    "        return \"muy bien\"\n",
    "    else:\n",
    "        return \"excelente\"\n",
    "\n",
    "try:\n",
    "    entrada = input(\"Indica tu calificación: \").strip()\n",
    "    calificacion = int(entrada)\n",
    "\n",
    "    resultado = calificacion_estudiante(calificacion)\n",
    "    print(resultado)\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Error: Por favor, introduce un número entero válido\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6e01ff49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El área del rectangulo con datos (8, 20) es: 160.00\n",
      "El área del circulo con datos (8,) es: 201.06\n",
      "El área del triangulo con datos (4, 6) es: 12.00\n"
     ]
    }
   ],
   "source": [
    "# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser \"rectangulo\" , \"circulo\" o \"triangulo\" ) y datos (una tupla con los datos necesarios para calcular el área de la figura). #\n",
    "\n",
    "import math\n",
    "\n",
    "def calcular_area (figura, datos):\n",
    "\n",
    "    if figura == \"rectangulo\":\n",
    "        if len(datos) < 2:\n",
    "            raise ValueError(\"Para un rectangulo se necesitan dos datos: (base, altura)\")\n",
    "        base, altura = datos[0], datos[1]\n",
    "        return base * altura\n",
    "\n",
    "    elif figura == \"circulo\":\n",
    "        if len(datos) < 1:\n",
    "            raise ValueError(\"Para un circulo se necesita 1 dato: radio\")\n",
    "        radio = datos[0]\n",
    "        return math.pi * (radio**2)\n",
    "\n",
    "    elif figura == \"triangulo\":\n",
    "        if len(datos) < 2:\n",
    "            raise ValueError(\"Para un triángulo se necesitan 2 datos: (base, altura).\")\n",
    "        base, altura = datos[0], datos[1]\n",
    "        return (base * altura) / 2\n",
    "\n",
    "    else:\n",
    "        raise ValueError(f\"Figura '{figura}' no reconocida. Usa 'rectangulo', 'circulo' o 'triangulo'.\")\n",
    "\n",
    "\n",
    "ejemplos = [\n",
    "    (\"rectangulo\", (8, 20)),\n",
    "    (\"circulo\", (8,)),\n",
    "    (\"triangulo\", (4, 6)),\n",
    "]\n",
    "\n",
    "for fig, vals in ejemplos:\n",
    "    area = calcular_area(fig, vals)\n",
    "    print(f\"El área del {fig} con datos {vals} es: {area:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6fea256c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Cupón aplicado! Se aplicará un descuento de 2.00€\n",
      "\n",
      "--- RESUMEN DE COMPRA ---\n",
      "Precio original: 20.00€\n",
      "Descuento:       -2.00€\n",
      "Precio final:    18.00€\n"
     ]
    }
   ],
   "source": [
    "# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 1. Solicita al usuario que ingrese el precio original de un artículo. 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python. #\n",
    "\n",
    "def monto_final():\n",
    "    precio_original = float(input(\"Indica el precio original del artículo en €: \"))\n",
    "\n",
    "    if precio_original <= 0:\n",
    "        print(\"El precio debe ser un número positivo\")\n",
    "\n",
    "        return\n",
    "    cupon = (input(\"¿Tienes un cupón de descuento? (si/no): \").strip().lower())\n",
    "\n",
    "    descuento = 0.0\n",
    "\n",
    "    if cupon in [\"si\", \"si\", \"s\"]:\n",
    "        valor_cupon = float(input(\"Indica el valor del cupón en €: \"))\n",
    "\n",
    "        if valor_cupon > 0:\n",
    "\n",
    "            descuento = min(valor_cupon, precio_original)\n",
    "            print(f\"¡Cupón aplicado! Se aplicará un descuento de {descuento:.2f}€\")\n",
    "\n",
    "        else:\n",
    "            print(\"El valor del cupón no es válido. Debe ser mayor a 0. No se aplicará descuento\")\n",
    "\n",
    "    elif cupon in [\"no\", \"n\"]:\n",
    "        print(\"No se aplicará ningún descuento\")\n",
    "\n",
    "    else:\n",
    "        print(\"Respuesta no reconocida. Se procesará la compra sin descuento\")\n",
    "\n",
    "    precio_final = precio_original - descuento\n",
    "    print(\"\\n--- RESUMEN DE COMPRA ---\")\n",
    "    print(f\"Precio original: {precio_original:.2f}€\")\n",
    "    print(f\"Descuento:       -{descuento:.2f}€\")\n",
    "    print(f\"Precio final:    {precio_final:.2f}€\")\n",
    "\n",
    "try:\n",
    "    monto_final()\n",
    "except ValueError:\n",
    "    print(\"Error: Por favor, ingresa un número válido para los montos.\") \n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
