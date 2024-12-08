Durchführung (allgemein)
************************

Wir werden im Folgenden drei Beispiele von Zephyr benutzen. Dabei durchläufst
du immer wieder die selben drei Schritte:
(1) UF2 Firmware **bauen**,
(2) UF2 Firmware auf das MCU-Board **hochladen**,
(3) Ausführung auf dem MCU-Board **beobachten**.

Dieser Dreiklang wird dir nun häufiger begegnen. Daher findest du hier nur
Informationen und Abbildungen zum prinzipiellen Ablauf. So findest du hier keine
konkreten Namen eines MCU-Boards oder Beispiels. Vielmehr werden wir dafür nur
symbolische Platzhalter benutzen, z.B. ``<board_name>``.

#. UF2 Firmware **bauen**

   .. compound::

      Benutze deine **Online-Sitzung von VS Code in deinem WEB-Browser**, um eine
      **Zephyr UF2 Firmware** zu bauen.

      .. image:: /_images/symbol-coder-server-bl.*
         :class: sidecar

   .. compound::

      Dazu navigierst du **im unteren Panel in das Terminal** mit der offenen
      Bash Sitzung und gibst mindestens folgendes ein:

      .. parsed-literal::
         :class: code

         **west build** -p *-b <board_name> <path_to_zephyr_app_or_sample_or_test>*

   .. compound::

      Nach erfolgreicher Übersetzung wirst du über den integrierten **Datei
      Explorer** (auf der linken Seite) in einem Unterordner deines **West
      Workspace** die soeben gebaute *Zephyr UF2 Firmware* finden. Der genaue
      Dateiname, relative zum *West Workspace*, lautet:

         :file:`build/zephyr/zephyr.uf2`

   .. compound::

      Dieser Name ist immer so, egal welche Applikation gegen welche Art
      von Hardware gebaut wurde. Diese UF2 Datei wirst du immer aus deiner
      virtuellen Entwicklungsumgebung (online, im WEB-Browser) auf deinen
      lokalen Host-PC herunterladen, denn nur dieser hat eine reale Verbindung
      über USB zu deinem MCU-Board. Mache das also und speicher dir diese
      UF2 Datei an einem Ort ab, an dem du sie im nächsten Schritt auch
      gleich wieder findest:

      .. list-table::
         :align: center
         :width: 80%

         * - .. image:: /_images/coder/code-server-uf2-download.*
                :align: center
                :scale: 100%

#. UF2 Firmware auf das MCU-Board **hochladen**

   .. compound::

      Versetze dein MCU-Board wieder in den *UF2 Upload-Modus* (Bootloader).

      .. image:: /_images/symbol-rp2040-uf2-rd.*
         :class: sidecar

   .. compound::

      Kopiere die zuvor gebaute **Zephyr UF2 Firmware** :file:`zephyr.uf2`
      in das Laufwerk :file:`RPI-RP2` von deinem Host-PC aus. Nach Erfolg
      **startet dein MCU-Board neu** (Reset).

      .. list-table::
         :align: center
         :width: 80%

         * - .. image:: /_images/doing/w11-rpi-rp2-zephyr-copy.*
                :align: center
                :scale: 100%

#. Ausführung auf dem MCU-Board **beobachten**

   .. compound::

      Wenn immer in dieser Anleitung der Text mit dem **Auge** gekennzeichnet
      ist, musst du dich deinem **MCU-Board** zuwenden.

      .. image:: /_images/symbol-observe-or.*
         :class: sidecar

   .. compound::

      Ausgaben an der Console oder zu erwartende Aktionen an der Hardware
      können nur dort passieren.

.. vi: ft=rst ai ts=3 et sw=3 sta
