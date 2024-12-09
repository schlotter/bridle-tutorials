.. _demo-zephyr-basic-servo:

Servomotor hin und her bewegen
##############################

.. sidebar:: Ziel

   Übersetzen, programmieren und spielen mit dem Zephyr Basic Beispiel
   :doc:`zephyr:samples/basic/servo_motor/README`

.. topic:: Übersicht

   Erinnere dich bitte an :ref:`die zurückliegende Übung <hs-cli-pwm-servo>`,
   als du mit dem Zephyr Shell Kommando :bcy:`pwm` die Servomotoren manuell
   in Bewegung versetzt hast. Nun werden wir ein Zephyr Standard Beispiel für
   einen Servomotor dazu benutzen. Dieses nutzt ebenso den Devicetree als Basis
   für die Deklaration konkreter Hardware. Im Gegensatz zu den vorangegangenen
   Beispielen wirst du nun aber keinen eigenen Devicetree Overlay schreiben.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   **Zephyr** kennt **seit Version 3.5** das Konzept der :ref:`zephyr:snippets`.

   .. rubric:: Snippets für Devicetree und Kconfig

   Snippets bieten dir die Möglichkeit, aus einem Projekt heraus
   **allgemeingültige** (das ist wichtig) **Devicetree Overlays** und
   **Kconfig Artefakte** als Dateien fertig vorzugeben, also mit dem Projekt
   zu pflegen und zu revisionieren. Zephyr bietet dir dann einen Zugriff auf
   diese Dateien zum Build-Zeitpunkt und sorgt für die Anwendung dieser
   *"Schnipsel"* im richtigen Moment an allerletzter Stelle der Konfiguration.

   .. admonition:: Gut zu wissen
      :class: good-to-know info

      **Snippets** übernehmen beim Aufruf von :program:`west build …` das
      umständliche setzen der Umgebungsvariable
      :makevar:`EXTRA_DTC_OVERLAY_FILE` und / oder
      :makevar:`EXTRA_CONF_FILE` – immer dann,
      **wenn ein Shield (noch) fehlt oder nie praktikabel sein wird.**

   .. rubric:: Servomotoren über PWM im Devicetree

   Auf Ebene deines MCU-Boards *Cytron – Maker Pi RP2040* werden bereits die
   für alle 4 Servomotoren benutzten PWM Kanäle deklariert – du erinnerst dich
   an :ref:`die zurückliegende Übung <hs-cli-pwm-servo>`?

   Was dort noch nicht gesagt wurde, auch die 4 Servomotoren selbst werden
   deklarativ vorbereitet, um diese gezielt in einer Zephyr Applikation,
   wie dieser hier, benutzen zu können.

   .. compound::

      Das sieht im Devicetree deines MCU-Boards folgendermaßen aus:

      .. code-block:: DTS

         / {
           pwm_servo_motors {
             compatible = "pwm-servos";
             status = "okay";

             pwm_servo0: pwm_servo_0 {
               pwms = <&pwm 12 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
               label = "PWM_SERVO_0";
             };
             pwm_servo1: pwm_servo_1 {
               pwms = <&pwm 13 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
               label = "PWM_SERVO_1";
             };
             pwm_servo2: pwm_servo_2 {
               pwms = <&pwm 14 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
               label = "PWM_SERVO_2";
             };
             pwm_servo3: pwm_servo_3 {
               pwms = <&pwm 15 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
               label = "PWM_SERVO_3";
             };
           };
         };

   Einem Systemarchitekt ist sicher schon in der zurückliegenden PWM Übung
   aufgefallen, dass Servomotoren *"Geräteeigenschaften"* besitzen – die
   Impulse für die jeweiligen Winkelpositionen oder Drehrichtungen werden
   in Realität Bauform abhängig sein und je nach Typ und Größe der Motoren
   und Hersteller andere Bedingungen an die PWM stellen.

   Kurz gesagt: *"Geräteeigenschaften"* müssen **als spezifische Parameter**
   in den Build einer Applikation einfließen, **dürfen aber neimals Teil
   des Devicetree eines Boards oder Shields sein!** Snippets bieten genau
   hierfür einen Lösungsansatz.

   .. rubric:: Geräteeigenschaften im Devicetree

   Für das nun benutzte Zephyr Standard Beispiel fehlen also die Parameter
   für die maximal und minimal erlaubten Impulsdauern im Devicetree.

   .. compound::

      Genau dafür stellt dir Bridle einen fertigen *"Schnipsel"* zur Verfügung,
      abgelegt innerhalb deines West Workspace unter
      :file:`bridle/snippets/pwm-servo` und das sortiert
      nach jeweils unterstützen Boards, also:

         :file:`bridle/snippets/pwm-servo/boards/cytron_maker_pi_rp2040.overlay`.

   .. compound::

      Der Inhalt lautet:

      .. code-block:: DTS

         servo: &pwm_servo0 {
           compatible = "pwm-servo";
           min-pulse = <PWM_USEC(500)>;
           max-pulse = <PWM_USEC(2500)>;
         };

   Die Verwaltung von Zephyr Snippets erfolgt wiederum rein deklarativ über
   semantisch geschützte YAML Dateien. Hierdurch bereitet dir Bridle also den
   rein symbolischen Snippet-Namen ``pwm-servo`` auf, den du mit dem Aufruf
   von :program:`west build … -S pwm-servo …` nur noch benutzen musst.

   .. admonition:: Gut zu wissen
      :class: good-to-know info

      Das ist übrigens dasselbe Prinzip, das du ständig mit der Angabe von
      :program:`west build … -S usb-console …` für die USB-CDC/ACM Console
      benutzt.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
