# Результаты работы фильтров

Обрабатываемое изображение:
![test_image](https://github.com/nagibinau/IDE-Group-26/blob/master/test_image.jpg)

Результат плохого фильтра:
![bad_filter_result](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/bad_filter_result.jpg)

Результат улучшенного фильтра:
![fixed_filter_result](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/fixed_filter_result.jpg)


# Время работы фильтров

Улучшенный фильтр с вводом входных параметров: <br>
![filter_time](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/filter_time.png)

Плохой фильтр без ввода параметров: <br>
![bad_filter_time](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/bad_filter_time.png)

Улучшенный фильтр без ввода параметров: <br>
![filter_with_filename_time](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/filter_with_filename_time.png)

Плохой фильтр отрабатывает быстрее, чем улучшенный фильтр с вводом данных, но это объясняется как раз-таки вводом входных параметров, из-за которых большая часть времени уделена ожиданию ввода данных от пользователя. <br>
Если сравнивать плохой фильтр и улучшенный фильтр без ввода параметров, то видим ощутимую разницу.

# Результы тестов

![doctests_results](https://github.com/nagibinau/IDE-Group-26/blob/master/images_after_filtering/doctests_results.png)
