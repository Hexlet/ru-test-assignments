Тестовое задание по написанию кода на Java для Jira-плагинов

Задание 1

1. Установить триальную версию Jira Data Center Software 9.12.13;
2. Установить плагин, используя Atlassian SDK;
3. Добавить таблицу через Active Objects, наполнить ее данными, добавить в UI (например, в Issue Tab Panel) Dropdown компонент AUI с иконкой, который опциями выводит данные из этой таблицы;
4. Добавить (либо отдельным элементом, либо совместно с предыдущим пунктом) AUI-Dialog2 и кастомизировать его на свое усмотрение.

Справочная информация:

* Create a HelloWorld plugin project (гайд от Atlassian)
* Getting started with Active Objects (гайд от Atlassian)
* Atlassian UI (ссылка на систему UI-компонентов)
* Issue Tab Panel (инструкция на портале Developer Atlassian)

________________

Задание 2
Test Task: Design a Class Diagram in UML
Objective:
Create a class diagram in UML to demonstrate your understanding of object-oriented programming (OOP) and SOLID principles. This task will help evaluate your ability to structure code logically, adhering to best practices in software design.
Scenario:
You are tasked with designing a basic Library Management System. This system will manage Books, Members, Borrowing, and Returns. Consider the following requirements:

1. Books can be added to the library. Each book has an ISBN, title, author, publication date, and a list of genres.
2. Members should be able to register in the system with basic details like name, contact information, and membership ID. Members can borrow books and return them after a set period.
3. Each Borrowing Transaction must be recorded with the date of borrowing and the due date for return. A book can be borrowed by one member at a time and must be returned before it can be borrowed by another.
4. The system should send reminders to members who fail to return a book on time.
Requirements:
5. Design a UML class diagram to represent the main entities and their relationships in this system.
6. Apply SOLID principles to ensure your design is scalable, maintainable, and follows good software design practices.
7. Clearly indicate the following in your diagram:
   * Class names, attributes, and key methods
   * Associations between classes (e.g., composition, aggregation, inheritance)
   * Access modifiers (public, private) where appropriate
8. Provide a brief explanation of how your design follows SOLID principles.

Bonus Points:

* Consider potential extensions to the system, such as adding more media types (e.g., DVDs, magazines) or handling multiple copies of the same book. Mention how your design would support these extensions without breaking existing functionality.
