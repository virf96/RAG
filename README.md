# Sistema RAG (Retrieval-Augmented Generation)

## Descripción

Este proyecto presenta una implementación de una arquitectura **Retrieval-Augmented Generation (RAG)**, cuyo objetivo es mejorar la calidad de las respuestas generadas por un modelo de lenguaje mediante la recuperación de información relevante desde una base de conocimiento.

La solución combina técnicas de procesamiento de documentos, generación de embeddings, búsqueda semántica y modelos de lenguaje para responder preguntas utilizando información específica del dominio, reduciendo las alucinaciones y proporcionando respuestas fundamentadas en documentos reales.

## Objetivos

* Implementar un flujo completo de un sistema RAG.
* Procesar y preparar documentos para su indexación.
* Generar embeddings para representar semánticamente el contenido.
* Almacenar e indexar los embeddings en una base vectorial.
* Recuperar el contexto más relevante para cada consulta.
* Generar respuestas utilizando un Large Language Model (LLM).
* Automatizar la validación del proyecto mediante GitHub Actions.

## Arquitectura

El flujo de trabajo del sistema se compone de las siguientes etapas:

1. **Ingesta de documentos**

   * Lectura de archivos (PDF, TXT, DOCX, Markdown, etc.).
   * Extracción del contenido.

2. **Preprocesamiento**

   * Limpieza del texto.
   * División en fragmentos (*chunking*).
   * Normalización del contenido.

3. **Generación de embeddings**

   * Conversión de cada fragmento en una representación vectorial utilizando un modelo de embeddings.

4. **Indexación**

   * Almacenamiento de los vectores en una base de datos vectorial.

5. **Recuperación (Retrieval)**

   * Búsqueda semántica de los fragmentos más relevantes para una consulta.

6. **Generación (Generation)**

   * Construcción del contexto.
   * Envío del contexto junto con la consulta al modelo de lenguaje.
   * Generación de una respuesta fundamentada en la información recuperada.

## Estructura del proyecto

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── embeddings/
├── notebooks/
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── embedding/
│   ├── retrieval/
│   ├── generation/
│   └── utils/
├── tests/
├── .github/
│   └── workflows/
├── Dockerfile
├── pyproject.toml
├── .gitignore
├── .env.example
└── README.md
```

## Tecnologías utilizadas

* Python
* LangChain o LlamaIndex
* OpenAI / Azure OpenAI / Modelos de código abierto
* Base de datos vectorial (FAISS, Chroma, Pinecone, Weaviate, Milvus, entre otras)
* Docker
* Git
* GitHub Actions

## Instalación

1. Clonar el repositorio.

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Acceder al directorio del proyecto.

```bash
cd <NOMBRE_DEL_PROYECTO>
```

3. Crear un entorno virtual.

```bash
python -m venv .venv
```

4. Activar el entorno.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

5. Instalar las dependencias.

```bash
pip install -e .
```

## Variables de entorno

Crear un archivo `.env` tomando como referencia `.env.example` y configurar las credenciales necesarias, por ejemplo:

* Clave del proveedor del modelo de lenguaje.
* Configuración de la base vectorial.
* Parámetros del modelo de embeddings.

## Ejecución

1. Cargar los documentos en la carpeta correspondiente.
2. Ejecutar el proceso de ingestión.
3. Generar los embeddings.
4. Indexar la información.
5. Ejecutar consultas sobre el sistema RAG.

## Integración continua

El proyecto incorpora **GitHub Actions** para automatizar tareas de integración continua, entre ellas:

* Instalación de dependencias.
* Validación de la estructura del proyecto.
* Ejecución de pruebas automatizadas.
* Verificación del formato y calidad del código.
* Validación previa a la integración mediante Pull Requests.

## Casos de uso

* Asistentes conversacionales especializados.
* Sistemas de preguntas y respuestas sobre documentación técnica.
* Búsqueda inteligente sobre bases documentales.
* Soporte interno para organizaciones.
* Consulta de manuales, políticas o procedimientos.

## Licencia

Este proyecto tiene fines educativos y demostrativos. Su propósito es mostrar una implementación completa de un sistema **Retrieval-Augmented Generation (RAG)** siguiendo buenas prácticas de ingeniería de software, procesamiento de documentos y automatización mediante GitHub Actions.
