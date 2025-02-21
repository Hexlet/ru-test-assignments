## Обратите внимание

Перед решением тестового задания заполните, пожалуйста, небольшую форму
отклика для интересующей вас вакансии по адресу: 

https://job.ivelum.com

После заполнения анкеты мы свяжемся с вами, ответим на ваши вопросы по вакансии 
и расскажем подробнее о наших проектах. По результатам этого общения мы можем
предложить вам попробовать сделать тестовое задание, которое описано ниже.
Присылайте ваше решение на адрес [job@ivelum.com](mailto:job@ivelum.com).


## Hacker™ News proxy

Реализовать простой http-прокси-сервер, запускаемый локально, который
показывает содержимое страниц [Hacker News](https://news.ycombinator.com).
Прокси должен модицифировать текст на страницах следующим образом: после
каждого слова из шести букв должен стоять значок «™». Пример™:

Исходный текст: https://news.ycombinator.com/item?id=13713480

```
The visual description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked it out.

Basically, each PDF contains a single large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format is
merely incidental here. Extracting out the two images shows two
JPG files with different contents (but different SHA-1 hashes
since the necessary prefix is missing). Each PDF consists of a
common prefix (which contains the PDF header, JPG stream
descriptor and some JPG headers), and a common suffix (containing
image data and PDF display commands).
```

Через ваш прокси™: http://127.0.0.1:8232/item?id=13713480

```
The visual™ description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked™ it out.

Basically, each PDF contains a single™ large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format™ is
merely™ incidental here. Extracting out the two images™ shows two
JPG files with different contents (but different SHA-1 hashes™
since the necessary prefix™ is missing). Each PDF consists of a
common™ prefix™ (which contains the PDF header™, JPG stream™
descriptor and some JPG headers), and a common™ suffix™ (containing
image data and PDF display commands).
```

Условия:
* последняя версия™ Python™
* страницы должны™ отображаться и работать полностью корректно, в точности так,
  как и оригинальные (за исключением модифицированного текста™);
* при навигации по ссылкам, которые ведут на другие™ страницы HN, браузер
  должен™ оставаться на адресе™ вашего™ прокси™;
* можно использовать любые общедоступные библиотеки, которые сочтёте нужным™;
* чем меньше™ кода, тем лучше. PEP8 — обязательно;
* если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл.

Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как 
насчет™ написания тестов™?

Присылайте ваше решение в виде ссылки™ на gist или на публичный репозиторий на 
GitHub™.


## Обратите внимание

Напомним порядок действий:

1. Пожалуйста, заполните форму отклика на сайте https://job.ivelum.com;
2. Мы свяжемся с вами, ответим на ваши вопросы по вакансии и расскажем про наши
   проекты. По результатам этого общения мы можем предложить вам попробовать 
   сделать тестовое задание, которое описано выше;
3. Присылайте ваше решение на [job@ivelum.com](mailto:job@ivelum.com).
