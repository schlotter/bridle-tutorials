Button Beispiel über UART Console
*********************************

Wir wollen nun das :doc:`zephyr:samples/basic/button/README` Beispiel von
Zephyr mit Ausgaben über die UART Console bauen und überprüfen.

-----------------------------------------------------------------------------

Durchlaufe den bekannten Dreiklang: (1) bauen, (2) laden, (3) beobachten.

-----------------------------------------------------------------------------

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``button`` bauen und laden
======================================================================

Hole deine **Online-Sitzung von VS Code** in den Vordergrund.

-----------------------------------------------------------------------------

.. ..... BUILD ..............................................................

.. image:: /_images/symbol-coder-server-bl.*
   :class: sidecar

.. compound::

   **Baue die Zephyr UF2 Firmware**, gib ein:

   .. parsed-literal::
      :class: code

      west build -p -b |BOARD| |BUTTON_st|

-----------------------------------------------------------------------------

.. ..... FLASH ..............................................................

.. image:: /_images/symbol-rp2040-uf2-rd.*
   :class: sidecar

**Lade** dir die **Zephyr UF2 Firmware** herunter und lade diese anschließend
**auf dein MCU-Board**.

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``button`` benutzen
===============================================================

Hole deinen **Terminalemulator** in den Vordergrund.

-----------------------------------------------------------------------------

.. ..... ACTION .............................................................

.. image:: /_images/symbol-observe-or.*
   :class: sidecar

.. compound::

   **Beobachte die Ausgaben**, folgendes muss zu sehen sein:

   .. parsed-literal::
      :class: code

      |BOOTMSG_UART_ZS_BUTTON|

Die **Benutzer-LED an GP7 leuchtet, wenn**
die **Benutzer-Taste an GP20 gedrückt** ist.

.. only:: html

   .. include:: yourspace.rsti

.. admonition:: Nur für Mentoren
   :class: red-border bug
   :collapsible:

   :download:`GS-cytron_maker_pi_rp2040-uartcons-button.uf2
   </_assets/GS-cytron_maker_pi_rp2040-uartcons-button.uf2>`
   – als Not-Backup gedacht!

.. vi: ft=rst ai ts=3 et sw=3 sta
