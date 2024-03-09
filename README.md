# HeadHunter_Geocoding

После реалицазции трех алгоритмов, мы видим вот такую красоту


![image](https://github.com/ilshatich/HeadHunter_Geocoding/assets/128620807/b7186bae-2150-47b8-a152-ea83db8a82e4)

Если рассматривать скорость программ, то:
1. SimpleQueryGeocoder     --  O(n), так как у нас время зависит от кол-ва данных.
2. SimpleTreeGeocoder      --  O(n^3), так как нужно проходиться по каждой стране, городе и области.
3. MemorizedTreeGeocoder   --  O(n+m+k), однако стоит учесть, что в данном алгоритме мы используем словарь => возмножно просесть по памяти.
