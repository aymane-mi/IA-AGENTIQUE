"""Prepare la base documentaire locale de tourisme au Maroc.

Les PDF sont deja fournis dans data/pdfs/. Ce script verifie simplement leur presence.
Lancer avec : uv run python download_pdfs.py
"""
from pathlib import Path

PDF_DIR = Path(__file__).resolve().parent / "data" / "pdfs"


def main() -> None:
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError("Aucun PDF trouve dans data/pdfs/.")
    print("Base documentaire tourisme presente :")
    for pdf in pdfs:
        print(f"- {pdf.name} ({pdf.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
