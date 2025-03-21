# PortScan #

Das Skript führt einen TCP-Port-Scan durch, bei dem es die SYN, RST und FIN Flags im TCP-Protokoll verwendet, um zu bestimmen, ob bestimmte Ports auf einem Zielhost offen oder geschlossen sind.

Was es tut:

- SYN-Scan:
SYN (Synchronize) ist ein Flag, das in einem TCP-Paket gesetzt wird, um eine Verbindung zu initiieren. Wenn das Skript ein SYN-Paket an einen bestimmten Port auf dem Zielhost sendet, wartet es auf eine Antwort.
Offener Port: Wenn der Zielport offen ist, antwortet der Zielhost mit einem SYN+ACK (Synchronize + Acknowledge) Paket. Das Skript interpretiert diese Antwort als Bestätigung, dass der Port offen ist.

- RST-Flag (Reset):
Wenn der Zielport geschlossen ist, wird der Zielhost mit einem RST (Reset) Paket antworten. Das bedeutet, dass der Port nicht für Verbindungen verfügbar ist, und das Skript zeigt an, dass der Port geschlossen ist.

- RST-Paket senden:
Nachdem das Skript ein SYN+ACK erhalten hat, sendet es ein RST-Paket zurück an den Zielhost. Das RST-Flag wird verwendet, um die Verbindung sofort zu schließen. Dies geschieht, um die Verbindung zu beenden, ohne dass eine vollständige TCP-Dreifach-Handshakes notwendig ist.


Es scannt die Ports gründlich und zeigt auch wirklich welche Ports offen/filtert sind oder geschlossen. Das ist die Perfekte eigenschaft von SYN/ACK


pip install scapy
