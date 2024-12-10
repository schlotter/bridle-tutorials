RGB LED Testmuster über USB-CDC/ACM Console
*******************************************

Nun wollen wir zum Abschluss des ersten Kapitels unserer Übungen das
:doc:`zephyr:samples/drivers/led_strip/README` Beispiel von Zephyr mit
Ausgaben über die USB-CDC/ACM Console bauen und überprüfen.

-----------------------------------------------------------------------------

Ein letztes mal der Hinweis: (1) bauen, (2) laden, (3) beobachten.

-----------------------------------------------------------------------------

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``led_strip`` bauen und laden
=========================================================================

Hole deine **Online-Sitzung von VS Code** in den Vordergrund.

-----------------------------------------------------------------------------

.. ..... BUILD ..............................................................

.. image:: /_images/symbol-coder-server-bl.*
   :class: sidecar

.. compound::

   **Baue die Zephyr UF2 Firmware** mit dem zusätzlichen Parameter
   |USB_CONSOLE_pr|, gib ein:

   .. parsed-literal::
      :class: code

      west build -p -b |BOARD|        |USB_CONSOLE_st| \\
                 |LED_STRIP|

-----------------------------------------------------------------------------

.. ..... FLASH ..............................................................

.. image:: /_images/symbol-rp2040-uf2-rd.*
   :class: sidecar

**Lade** dir die **Zephyr UF2 Firmware** herunter und lade diese anschließend
**auf dein MCU-Board**.

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``led_strip`` benutzen
==================================================================

Hole deinen **Terminalemulator** in den Vordergrund.

-----------------------------------------------------------------------------

.. ..... ACTION .............................................................

.. image:: /_images/symbol-observe-or.*
   :class: sidecar

.. compound::

   **Beobachte die Ausgaben**, folgendes muss zu sehen sein:

   .. parsed-literal::
      :class: code

      |BOOTMSG_USB_ZS_LED_STRIP|

Die **beiden RGB-LEDs** (``0`` und ``1``) an den Rändern deines MCU-Boards
**leuchten abwechselnd in roter, grüner und blauer Farbe**.

.. include:: yourspace-long.rsti

.. admonition:: Nur für Mentoren
   :class: red-border bug
   :collapsible:

   :download:`GS-cytron_maker_pi_rp2040-usbcons-led_ws2812.uf2
   </_assets/GS-cytron_maker_pi_rp2040-usbcons-led_ws2812.uf2>`
   – als Not-Backup gedacht!

.. vi: ft=rst ai ts=3 et sw=3 sta
