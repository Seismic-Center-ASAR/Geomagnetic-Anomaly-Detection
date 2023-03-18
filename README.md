# Geomagnetic-Anomaly-Detection
EN

Bpol.py will perform the frequency analysis of the geomagnetic data for a period of time defined in the code.

getdata.py will download the geomagnetic data for each day of the desired interval, one day per request. The data is saved in a text file. Each day will have the corresponding file and later we will combine the data from these text files into a single text file that will contain the data for the entire target interval. We will remove the header from the files whose content we add to the final file. When we have all the data from each day of the interval in a single text file, we import the final text file into Excel using standard delimitation, after which we save and export the data from Excel into a new file in CSV format. We will use this CSV file as input data, as a file to be read and analyzed by BPOL.PY but not before modifying in bpol.py the cancellation, monthly and start and end day of the imported data corresponding to the analyzed interval .
The BPOL method has been used for several decades in geomagnetic detection and analysis. It was first introduced by Kivelson and Russell in 1976 as a method of analyzing magnetometer data from spacecraft to study the Earth's magnetic field. Since then, it has been used in various applications, including the analysis of geomagnetic data from the ground to study space weather and earthquake precursors. While the basic principles of the BPOL method have remained the same, there have been advances in the techniques and tools used to apply it. An approach to seismic research and forecasting of the precursors was made here:
https://ui.adsabs.harvard.edu/abs/2021EGUGA..23.1078S/abstract

<img src="https://i.ibb.co/JHQLkCy/2004.png"></img>
<img src="https://i.ibb.co/9wmrzvr/2016.png"></img>
<img src="https://i.ibb.co/Z6qS2yv/2018.png"></img>
<img src="https://i.ibb.co/9V76Ttn/20230318.png"></img>

RO

Bpol.py va efectua analiza in frecventa a datelor geomagnetice pentru o perioada de timp definita in cod.

getdata.py va descarca datele geomagnetice pentru fiecare zi din intervalul dorit, cate o zi pe request. Datele sunt salvate intr-un fisier text. Fiecare zi va avea fisierul corespunzator iar ulterior vom combina datele din aceste fisiere text intr-un singur fisier text care va contine datele pentru intreg intervalul tinta. Vom elimina header-ul din fisierele a caror continut le adaugam in fisierul final. Cand avem intr-un singur fisier text toate datele din fiecare zi al intervalului importam fisierul text final in Excel folosind delimitare standard dupa care salvam  si exportam din Excel datele intr-un nou fisier in format CSV. Acest fisier CSV il vom utiliza ca si data input, ca si fisier care sa fie citit si analizat de BPOL.PY dar nu inainte de a modifica in bpol.py data anula, lunara si zi de inceput si sfarsit al datelor importate corespunzator intervalului analizat. 
Metoda BPOL a fost folosită de câteva decenii în detectarea și analiza geomagnetică. A fost introdus pentru prima dată de Kivelson și Russell în 1976 ca metodă de analiză a datelor magnetometrului de la nave spațiale pentru a studia câmpul magnetic al Pământului. De atunci, a fost folosit în diverse aplicații, inclusiv în analiza datelor geomagnetice de la sol pentru a studia vremea spațială și precursorii cutremurelor. În timp ce principiile de bază ale metodei BPOL au rămas aceleași, au existat progrese în tehnicile și instrumentele utilizate pentru aplicarea acesteia. O aproiere in cercetarea si prognoza seismica a precursorilor fost realizata aici:
https://ui.adsabs.harvard.edu/abs/2021EGUGA..23.1078S/abstract

<img src="https://i.ibb.co/JHQLkCy/2004.png"></img>
<img src="https://i.ibb.co/9wmrzvr/2016.png"></img>
<img src="https://i.ibb.co/Z6qS2yv/2018.png"></img>
<img src="https://i.ibb.co/9V76Ttn/20230318.png"></img>