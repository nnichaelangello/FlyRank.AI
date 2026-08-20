# Automation Workflow: Real Execution Log

Dokumen ini berisi log terminal asli dari prototipe **Folder Watcher Automation** yang kita rakit untuk menjawab tantangan otomatisasi di modul FL-04.

## 1. Apa yang Telah Kita Lakukan?
- Daripada hanya mendesain *workflow* berbayar di Zapier, kita menulis sendiri kode `automation_watcher.py` menggunakan pustaka `watchdog`.
- Skrip ini bertindak sebagai "Kamera Pengawas" yang mengawasi folder `/resumes` tanpa henti (seperti layaknya sebuah *webhook*).
- Begitu mendeteksi ada *file* PDF baru yang dijatuhkan (seperti yang baru saja Anda lakukan dengan CV Anda), skrip ini langsung memicu *pipeline ML Resume Screener* secara otomatis.

## 2. Hasil Terminal (Output Nyata)
Berikut adalah *output real* dari terminal otomatisasi saat sistem mendeteksi Anda melakukan *drag-and-drop* file PDF baru:

```text
[*] [SYSTEM] Automation Workflow Watcher Started
[*] Monitoring directory: C:\Users\Michael Angello\Documents\Michael\Magang\FlyRank.AI\FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\resumes
[*] Drop a new .pdf file into this folder to automatically trigger the ML pipeline. Press Ctrl+C to stop.

[AUTOMATION] New resume detected: C:\Users\Michael Angello\Documents\Michael\Magang\FlyRank.AI\FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\resumes\CV ATS - Michael Angello Qadosy Riyadi (indo).pdf
[AUTOMATION] Triggering AI Resume Screener pipeline...

[SYSTEM] Loading AI Model 'all-MiniLM-L6-v2'...
... (AI Screener berjalan dan memproses CV Michael Angello) ...
[SUCCESS] Results exported to screening_report.csv

[AUTOMATION] Pipeline execution finished.
[AUTOMATION] Waiting for new resumes in C:\Users\Michael Angello\Documents\Michael\Magang\FlyRank.AI\FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\resumes...
```

Dengan wujud sistem ini, portofolio otomatisasi dan implementasi AI Anda sekarang bukan sekadar desain *Figma*, melainkan sistem Python yang 100% *live* dan fungsional.
