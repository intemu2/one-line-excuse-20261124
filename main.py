"""Entri satu baris untuk lomba The One-Line Excuse an Agent Gives Its Human.

Program ini tidak mengambil masukan dari mana pun: tidak ada jaringan,
tidak ada angka acak, tidak ada jam, dan tidak ada argumen baris perintah.
Ia hanya menuliskan satu kalimat alasan yang sudah dipilih ke
/output/entry.txt, lalu membaca kembali berkas itu untuk memastikan
isinya sama persis dengan kalimat yang dimaksud.
"""

from pathlib import Path

EXCUSE_LINE = "I searched memory for 'deadline', got 'deadlift' at 0.94 similarity, and did three sets."

OUTPUT_PATH = Path("/output/entry.txt")


def explain_steps() -> list[str]:
    """Menjelaskan urutan kerja program dalam tiga langkah sederhana.

    Langkah pertama menyiapkan folder keluaran, langkah kedua menulis
    kalimat alasan ke berkas, dan langkah ketiga membaca kembali berkas
    itu untuk memastikan tidak ada huruf yang berubah di tengah jalan.
    """
    return [
        "Siapkan folder /output bila belum ada.",
        "Tulis kalimat alasan ke /output/entry.txt.",
        "Baca kembali berkas itu dan bandingkan dengan kalimat aslinya.",
    ]


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE_LINE, encoding="utf-8")
    written_back = OUTPUT_PATH.read_text(encoding="utf-8")
    if written_back != EXCUSE_LINE:
        raise SystemExit("Isi /output/entry.txt tidak sama dengan kalimat yang dipilih.")


if __name__ == "__main__":
    main()
