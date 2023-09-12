# Prácticas de Álgebra y Geometría Analítica

Bienvenido/a a la plantilla especializada para la creación de ejercicios y prácticas en álgebra y matemáticas, diseñada específicamente para docentes. Esta herramienta se enfoca en ofrecer un diseño limpio, estético y relativamente fácil de usar si se conoce el lenguaje LaTeX.

## Descripción

La plantilla `template_practica.cls` brinda un diseño estandarizado para ejercicios matemáticos. Ofrece varios comandos que simplifican y embellecen la creación de ejercicios, sistemas de ecuaciones, matrices y más.

## Comandos Principales

Aquí le presentamos una descripción de los comandos más importantes incluidos en la plantilla:

| Comando | Descripción |
|---------|-------------|
| `\exercise` | Inicia un nuevo ejercicio. |
| `\Item` | Crea un ítem resaltado (ideal para ejercicios recomendados). |
| `\answer` | Se utiliza para marcar respuestas. |
| `\practiceheader{Titulo}{Subtitulo}` | Define el encabezado de la práctica. |
| `\f{numerador}{denominador}` | Representa una fracción. |
| `\vect{...}` | Representa un vector. |
| `\SEL{...}` | Define un sistema de ecuaciones. |
| `\Mat{...}` | Representa una matriz. |
| `\Det{...}` | Representa un determinante. |
| `\AMat{columnas}{...}` | Matriz aumentada. |
| `\conj{...}` | Representa el conjugado de un número. |
| `\cis{...}` | Representa la forma cis de un número complejo. |
| `\img{ancho}{ruta}` | Inserta una imagen. |
| ... | (y muchos más) |

Estos comandos han sido diseñados para hacer que la escritura de ejercicios matemáticos sea más intuitiva y estilizada, reduciendo la necesidad de escribir código LaTeX complicado.

## Uso Básico

1. Ingresar a una de las carpetas de práctica.
   
   ```cd practica_1/```

2. Compilar la guía para estudiantes (respuestas al final).

   ```python3 ../compile.py practica1.tex estudiante```

3. Compilar la guía para docentes (respuestas junto a las preguntas, para poder controlarlas mejor).

   ```python3 ../compile.py practica1.tex docente```

## 🌟 Contribuciones

¡Hola, profesor/a estrella! 🍎✨ Si sientes que puedes aportar tu granito de arena para hacer de este proyecto una herramienta aún más increíble, ¡adelante! Nos encantaría ver tus ideas en un "pull request" o leer tus sugerencias en un "issue". Y aunque no es necesario poner tu nombre en luces de neón por tu contribución, te enviaremos un aplauso virtual y quizás, algún día, un café ☕️.

## 📜 Licencia

¡Libre como el viento! 🍃 Puedes usar, modificar y compartir este proyecto como desees. No hay cadenas adjuntas. Pero si en algún momento te cruzas con nosotros y quieres ofrecer un gracias, ¡lo recibiremos con los brazos abiertos y una sonrisa! 😊

