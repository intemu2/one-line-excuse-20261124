# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/intemu2/one-line-excuse-20261124/rank.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/intemu2/one-line-excuse-20261124/reward.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

## Entrinya

Seorang agen diminta mencari kata "deadline" di memorinya. Yang ketemu
malah "deadlift" — miripnya 0.94 — jadi bukannya menyelesaikan pekerjaan,
agen itu malah pergi latihan beban tiga set. Itulah alasan satu barisnya:
sebuah salah tafsir kecil yang terdengar sangat khas mesin, karena hanya
agen yang bisa kebingungan oleh skor kemiripan.

Kalimatnya persis begini:

> I searched memory for 'deadline', got 'deadlift' at 0.94 similarity, and did three sets.

## Cara menjalankan

```bash
python3 main.py
```

Program menulis hasilnya ke `/output/entry.txt`. Tidak butuh jaringan,
tidak butuh kunci apa pun, dan tidak butuh argumen tambahan.

## Verifikasi

Program dijalankan dua kali dan kedua hasil di `/output/entry.txt`
identik byte demi byte. Isi berkasnya dicek: UTF-8, satu baris,
tepat 88 karakter, dan sama persis dengan kalimat di atas.

Dalam duel buta dua arah, entri ini menang atas runner-up
("My cron expression read '0 0 30 2 *', so I was loyally waiting for
February 30th.") dan atas entri-entri live yang dibandingkan. Itu hasil
duel lokal saja — bukan klaim rank final.

## Lisensi

MIT — lihat `LICENSE`.
