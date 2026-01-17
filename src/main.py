# src/main.py
"""Entry point for the Word to PDF converter.
Provides a command‑line interface and an optional simple GUI.
"""

import argparse
import sys
from pathlib import Path

from .converter import convert_docx_to_pdf


def run_cli():
    parser = argparse.ArgumentParser(
        description="Convert Microsoft Word (.docx) files to PDF preserving formatting."
    )
    parser.add_argument(
        "input",
        type=str,
        help="Path to the input .docx file"
    )
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        help="Optional path for the output PDF. If omitted, PDF is created beside the input file."
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch a minimal graphical interface instead of the CLI."
    )
    args = parser.parse_args()

    if args.gui:
        launch_gui()
        return

    try:
        pdf_path = convert_docx_to_pdf(args.input, args.output)
        print(f"SUCCESS: PDF generado en: {pdf_path}")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


def launch_gui():
    """Very small Tkinter GUI – select file, optional output, show progress."""
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
    except ImportError:
        print("Tkinter no está disponible en este entorno.")
        sys.exit(1)

    root = tk.Tk()
    root.title("Convertidor Word → PDF")
    root.geometry("400x150")

    def select_input():
        path = filedialog.askopenfilename(
            title="Selecciona un archivo .docx",
            filetypes=[("Documentos Word", "*.docx")],
        )
        if path:
            input_var.set(path)

    def start_conversion():
        inp = input_var.get()
        out = output_var.get() or None
        if not inp:
            messagebox.showerror("Error", "Debe seleccionar un archivo .docx.")
            return
        try:
            pdf_path = convert_docx_to_pdf(inp, out)
            messagebox.showinfo("Éxito", f"PDF creado en:\n{pdf_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    input_var = tk.StringVar()
    output_var = tk.StringVar()

    tk.Label(root, text="Archivo .docx:").pack(pady=(10, 0))
    tk.Entry(root, textvariable=input_var, width=40).pack(pady=2)
    tk.Button(root, text="Buscar...", command=select_input).pack(pady=2)

    tk.Label(root, text="Salida PDF (opcional):").pack(pady=(10, 0))
    tk.Entry(root, textvariable=output_var, width=40).pack(pady=2)

    tk.Button(root, text="Convertir", command=start_conversion, bg="#4CAF50", fg="white").pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    run_cli()
