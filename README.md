# Geophysikalische-Signalverarbeitung

Material zu der Vorlesung "Geophysikalische Signalverarbeitung" (SS 2019)
Institut für Geowissenschaften (Abteilung Geophysik), Christian-Albrechts-Universität Kiel

[Homepage "Geophysikalische Signalverarbeitung"](https://danielkoehnsite.wordpress.com/blog/geophysikalische-signalverarbeitung/)

Die Inhalte der folgenden Jupyter Notebooks können gemäß der CC BY-NC-SA 4.0 Lizenz, verwendet und modifiziert werden:

[https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Kapitel 8: Korrelation von Signalen

## [Vorlesung 1](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/1_Korrelation_corr_coeff.ipynb): Korrelationskoeffizient

Um die Ähnlichkeit von Zeitreihen zu untersuchen, müssen zunächst Maße definiert werden. In dieser Vorlesung diskutiere ich Vor- und Nachteile von Korrelationskoeffizienten und erläutere deren Anwendungen auf 
Zeitreihen unterschiedlicher Komplexität.

## [Vorlesung 2](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/2_Korrelation_KKF_AKF.ipynb): Kreuz- und Autokorrelation

In dieser Vorlesung führen wir als Maß einer Korrelation von zwei Signalen gegenüber einer Zeitverschiebung die Kreuzkorrelationsfunktion (KKF) ein. Ähnliche oder periodisch wiederkehrende Signale innerhalb 
einer Zeitreihe lassen sich mit der Autokorrelationsfunktion (AKF) identifizieren.

## [Vorlesung 3](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/3_Korrelation_AKF_Beispiele.ipynb): AKF-Beispiele

Nachdem wir die KKF und AKF als Maße für die Korrelation zwischen Zeitreihen gegenüber einer Zeitverschiebung eingeführt hatten, soll im folgenden die AKF und deren Eigenschaften anhand einiger Beispiele 
illustriert werden.

## [Vorlesung 4](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/4_Korrelation_vibroseis_match_filter.ipynb): Vibroseismik und Korrelationsfilter

Als erstes Anwendungsbeispiel der AKF und KKF in der Geophysik analysieren wir das Konzept des Vibroseismikverfahrens anhand von synthetischen Zeitreihen und Felddaten.

## [Vorlesung 5](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/5_Korrelation_AKF_seismic_trace_ghost.ipynb): AKF einer seismischen Spur

Als elementares, geophysikalisches Anwendungsbeispiel der Autokovarianzfunktion betrachten wir die AKF einer seismischen Spur mit bzw. ohne Ghost und diskutieren deren 
Eigenschaften im Frequenzbereich.

## [Vorlesung 6](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/6_Korrelation_Multiplets_detection.ipynb): Detektion von Multiplets

Multiplets sind seismische Ereignisse mit gleicher bzw. ähnlicher Wellenform. Treten an einer Station Multiplets auf, können die relativen Einsatzzeiten zwischen zwei Ereignissen 
mittels Kreuzkorrelation bestimmt werden.

## [Vorlesung 7](http://nbviewer.ipython.org/urls/github.com/daniel-koehn/Geophysikalische-Signalverarbeitung/tree/master/7_Korrelation_Phase_vel_estimation_of_surface_waves.ipynb): Bestimmung der Phasengeschwindigkeit der Grundmode von Oberflächenwellen

Die Dispersion von Oberflächenwellen läßt sich theoretisch durch eine Frequenzabhängigkeit der Phasengeschwindigkeit erklären. Da tieffrequente Anteile der Oberflächenwelle tiefer 
in den Untergrund eindringen, als höherfrequente, liefert das Phasengeschwindigkeits-Frequenzspektrum Informationen über die tiefenabhängige Geschwindigkeitsverteilung in der 
Erde. Eine Möglichkeit zur Bestimmung von Dispersionskurven basiert auf der KKF von Seismogrammen, die an zwei unterschiedlichen Stationen aufgezeichnet wurden. Wir diskutieren 
die Berechnung und Inversion von Dispersionskurven für Europa, den Mittelmeerraum und den Mittleren Osten im Detail.

Im Verlauf der Vorlesung werde ich weitere Notebooks hinzufügen.

Daniel Köhn

Kiel, 18.06.2019
