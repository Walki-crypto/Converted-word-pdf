# README.md

# Convertidor Word → PDF
[![CI](https://github.com/Walki-crypto/Converted-word-pdf/actions/workflows/ci.yml/badge.svg)](https://github.com/Walki-crypto/Converted-word-pdf/actions/workflows/ci.yml)

Una pequeña aplicación de escritorio (CLI y GUI opcional) que convierte documentos **Microsoft Word (.docx)** a **PDF** manteniendo el formato, imágenes, tablas y estilos.

## Características
- **Sin dependencias de Microsoft Office**: funciona en Windows 10/11 usando solo librerías Python.
- **Interfaz de línea de comandos** (`python -m src.main <input.docx> [output.pdf]`).
- **GUI mínima** con Tkinter (`--gui`).
- Preserva estilos básicos (negrita, cursiva, subrayado, tamaños, fuentes y colores).
- Conversión a través de **ReportLab** (pure‑Python, sin dependencias nativas).

## Requisitos
- Python 3.9 o superior (recomendado 3.11).
- Windows 10/11.

## Instalación
```bash
# Clonar el repositorio (si aún no lo has hecho)
git clone <URL_DEL_REPOSITORIO>
cd "Convertidor de word a pdf"

# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
venv\Scripts\activate   # en PowerShell: .\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

> **Nota**: `WeasyPrint` necesita algunas dependencias del sistema (Cairo, Pango, GDK‑Pixbuf). En Windows el paquete `weasyprint` incluye binarios precompilados, por lo que normalmente no es necesario instalar nada extra.

## Uso – CLI
```bash
python -m src.main path\al\archivo.docx          # PDF se crea al lado del .docx
python -m src.main path\al\archivo.docx out.pdf  # Ruta de salida personalizada
```

## Uso – GUI
```bash
python -m src.main --gui
```
Se abrirá una ventana donde podrás seleccionar el archivo `.docx` y, opcionalmente, la ruta de salida.

## Empaquetado (opcional)
Si deseas distribuir un ejecutable único:
```bash
pip install pyinstaller
pyinstaller --onefile --name convertidor src/main.py
```
El ejecutable `convertidor.exe` aparecerá en la carpeta `dist`.

## Estructura del proyecto
```
Convertidor de word a pdf/
│   requirements.txt
│   README.md
│   .gitignore
│
└───src
    │   __init__.py
    │   converter.py   # lógica de conversión docx → HTML → PDF
    │   main.py        # CLI y GUI
```

## Contribuir
1. Haz un fork del proyecto.
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`).
3. Envía un Pull Request.

## Licencia
Este proyecto está bajo la licencia MIT.
