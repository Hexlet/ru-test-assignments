# Первое тестовое задание

## Условие задачи

Дана последовательность:

```text
1
11
21
1211
111221
312211
13112221
```

Необходимо написать программу на Ruby, которая генерирует последовательность такого рода. Для реализации программы нужно использовать функции из стандартной библиотеки Ruby. Программа должна быть построена по принципам объектно-ориентированной архитектуры, использовать классы. Желательно, чтобы для программы были написаны автоматические тесты.

Код готового приложения должен быть размещён на [GitHub](http://github.com) в репозитории с публичным доступом.

## Второе тестовое задание

### Условие задачи

Необходимо создать web-приложение "Календарь событий", реализующее следующие функции:

* Пользователи могут зарегистрироваться, указав email и пароль (обязательно) и полное имя (необязательно);
* Зарегистрированный пользователь может изменить свой email, пароль и полное имя;
* Зарегистрированный пользователь может просмотреть список своих событий в календаре;
* Зарегистрированный пользователь может просмотреть список всех событий в календаре;
* Зарегистрированный пользователь видит в интерфейсе ссылку "Создать событие", при переходе по ссылке пользователь должен видеть форму для создания нового события;
* События имеют название (обязательно) и дату (обязательно);
* Событие может быть повторяющимся каждый день, каждую неделю, каждый месяц, каждый год;
* Зарегистрированный пользователь может кликнуть на собственное событие в календаре и перейти на страницу с формой для редактирования события;
* Зарегистрированный пользователь может кликнуть на любое событие в календаре и перейти на страницу с описанием события;

### Особенности реализации

* При выполнении обоих тестовых заданий руководствуйтесь [Ruby Style Guide](https://github.com/bbatsov/ruby-style-guide) и [Rails Style Guide](https://github.com/bbatsov/rails-style-guide);
* Необходимо использовать Ruby версии >= 2.5, Rails >= 5.1;
* Желательно, чтобы для приложения были написаны автоматические тесты;
* Готовое приложение должно быть развернуто на [Heroku](https://heroku.com);
* Код приложения должен быть размещён на [GitHub](http://github.com) в репозитории с публичным доступом;
* Пользовательский интерфейс можно реализовать так, как считаете нужным, использование Twitter Bootstrap или Zurb Foundation будет дополнительным плюсом;
* Дополнительно реализуйте какую-нибудь полезную функциональность и напишите почему эта функциональность, по Вашему мнению, полезна.

## Дополнительное тестовое задание

### Условие задачи

Необходимо разработать web-приложение "Форма обратной связи" на основе данных user stories.

Требуется:

* Использовать [rails-base](https://github.com/fs/rails-base) как основу проекта.
* Сделать простой приятный дизайн.
* Задеплоить разработанное приложение на Heroku.
* При необходимости - использовать стандартные для компании библиотеки (Devise, Pundit / ActivePolicy, Draper, Interactor, Simple Form)
* Все user story покрыть автоматическими тестами (RSpec, Capybara, ChromeDriver)

```text
As Visitor I want to leave feedback
  When I open New Feedback page
  Then I see form with required fields: name, email, text
  When I fill all 3 fields
  And When I click "Submit feedback"
  I should see message "Feedback was successfully send!"
  And email with feedback sent to admin@example.com

As User I want to see pre-filled name and email in feedback form
  Given I am authenticated as John Smith (john@example.com)
  When I open New Feedback page
  Then I should see name field pre-filled with "John Smith"
  And I should see email field pre-filled with "john@example.com"

As Admin User I want to see list of all Feedbacks
  Given I am authenticated as Admin (admin@example.com)
  And there are Feedbacks in database
  When I open Feedbacks page
  Then I see table with list of all feedbacks sorted by "newest first"
  And I see pagination under the table

As Admin User I want to search through feedbacks
  Given I am authenticated as Admin (admin@example.com)
  And there are feedback with text "Hello" from John Smith (john@example.com) in database
  And there are feedback with text "Help" from Michael Brown (misha@example.com) in database
  When I open Feedbacks page
  Then I see Search Form with text input and submit button
  When I fill search input with "john"
  Then I see feedback from John Smith
  And I do not see feedback from Michael
  When I fill search input with "Help"
  Then I see feedback from Michael
  And I do not see feedback from John Smith
```
