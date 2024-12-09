:spelling:ignore:`Visual Studio Code` (online)
**********************************************

Wenn immer in dieser Anleitung der Text mit dem **Coder Symbol** gekennzeichnet
ist, musst du zu deiner **Online-Sitzung von VS Code in deinem WEB-Browser**
wechseln.

.. image:: /_images/symbol-coder-server-bl.*
   :class: sidecar

Du erreichst **unsere Cloud Infrastruktur** über das Dashboard auf:

    |online_ide_entry|

Dort meldest du dich mit deinen persönlichen Zugangsdaten an und findest dann
über **Workspaces** in einer Liste einen Eintrag für dich. Wähle diesen aus
und du gelangst auf eine Übersicht mit einer Taste mit der Aufschrift
**code-server** (*nicht "VS Code Desktop" !!!*). Drücke diese.

.. only:: html

   .. list-table::
      :align: center
      :width: 80%
      :widths: 20, 80

      * - .. image:: /_images/coder/coder-dashboard-login.*
             :align: center
             :scale: 100%
        - .. image:: /_images/coder/coder-dashboard-workspace.*
             :align: center
             :scale: 100%

.. only:: rinoh

   .. list-table::
      :align: center
      :width: 80%

      * - .. image:: /_images/coder/coder-dashboard-login.*
             :align: center
             :scale: 33%
      * - .. image:: /_images/coder/coder-dashboard-workspace.*
             :align: center
             :scale: 100%

.. rst-class:: page-break

Daraufhin öffnet sich ein **neues WEB-Browser Fenster mit VS Code**. Bestätige
die **Vertrauenswürdigkeit** und schalte dir das **Terminal** im unteren Panel
ein. Wir empfehlen dir dringend, darin sofort in eine **Bash** zu wechseln.

.. only:: html

   .. list-table::
      :align: center
      :width: 80%
      :widths: 50, 50

      * - .. image:: /_images/coder/code-server-virgin.*
             :align: center
             :scale: 100%
        - .. image:: /_images/coder/code-server-bash.*
             :align: center
             :scale: 100%

.. only:: rinoh

   .. list-table::
      :align: center
      :width: 80%

      * - .. image:: /_images/coder/code-server-virgin.*
             :align: center
             :scale: 100%
      * - .. image:: /_images/coder/code-server-bash.*
             :align: center
             :scale: 100%

.. rst-class:: page-break

West Workspace
==============

.. compound::

   Nun kannst du in den vorbereiteten **West Workspace** wechseln, gebe ein::

      cd workspace
      ls -al

**Ab diesen Moment bist du vollständig arbeitsfähig und kannst Applikationen
mit Zephyr bauen oder selber welche entwickeln.**

.. compound::

   Gerne kannst du aber auch erst einmal deinen West Workspace erkunden
   und dein erstes West Kommando absetzen, so z.B.:

   .. parsed-literal::
      :class: code

      **west list** *--format "{name:12}{path:28}{revision:40}"*

   … oder nur ganz kurz :program:`west list`.

.. compound::

   Damit erhältst du deine Baseline, also eine wichtige Information für dein
   **Software Configuration Management**.

   .. list-table::
      :align: center
      :width: 80%

      * - .. image:: /_images/coder/code-server-west-list.*
             :align: center
             :scale: 100%

.. rst-class:: page-break

West Manifest
=============

Du kannst hier schon erkennen, dass die Softwarequellen von Zephyr aus einer
Seitenlinie stammen, Branch-Name |zephyr_branch|. Das **West Manifest** wird
von dem Projekt (Verzeichnis) :file:`bridle` vorgegeben, wie zu erwarten war.

.. compound::

   Du hast nun auch die Möglichkeit, das West Manifest genauer zu untersuchen.
   Gib dazu einfach mal folgendes ein:

   .. parsed-literal::
      :class: code

         **west manifest** *--path*
         **west manifest** *--resolve*
         **west manifest** *--validate*

.. compound::

   In der Tat, das West Manifest gehört dem Bridle Quellcode und ist die
   Datei :file:`/home/coder/workspace/bridle/west.yml`. Auch wird nun sichtbar,
   dass die Softwarequellen von Zephyr nicht nur aus einer Seitenlinie stammen,
   sondern auch noch aus einem anderen als dem offiziellen Git Repository. Es
   handelt sich um unseren Spiegel auf GitHub unter
   :file:`https://github.com/tiacsys/zephyr`.

   .. list-table::
      :align: center
      :width: 80%

      * - .. image:: /_images/coder/code-server-west-manifest.*
             :align: center
             :scale: 100%

.. vi: ft=rst ai ts=3 et sw=3 sta
