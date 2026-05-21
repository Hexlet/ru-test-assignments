SQL query parser

In SQL, the most syntactically complex and tricky query is probably the SELECT query. It has explicit and implicit joins, groupings,
subqueries, sorting and truncation of selects - all this beauty can occur repeatedly even in one single
select query.

For example, like this:

```sql
SELECT * FROM book
```

or like this:

```sql
SELECT author.name, count(book.id), sum(book.cost) 
FROM author 
LEFT JOIN book ON (author.id = book.author_id) 
GROUP BY author.name 
HAVING COUNT(*) > 1 AND SUM(book.cost) > 500
LIMIT 10;
```

Please write a parser for an arbitrary SELECT query, representing it as a class of approximately this structure:

```java
class Query {
	private List<String> columns;
	private List<Source> fromSources;
	private List<Join> joins;
	private List<WhereClause> whereClauses;
	private List<String> groupByColumns;
	private List<Sort> sortColumns;
	private Integer limit;
	private Integer offset;
}
```

The structure of this class is not a requirement, but a guide to action :)
If you have invented a class that reflects the SQL query structure better than the one given here - feel free to use your solution.

What constructs the parser must support in a mandatory way:

* Enumeration of sample fields explicitly (with aliases) or *
* Implicit join of several tables (select * from A,B,C)
* Explicit join of tables (inner, left, right, full join)
* Filter conditions (where a = 1 and b > 100)
* Subqueries (select *from (select* from A) a_alias)
* Grouping by one or several fields (group by)
* Sorting by one or more fields (order by)
* Selection truncation (limit, offset)

What can be ignored:

* Complementing selections (union and union all)
* CTE
* Window functions

Some details:

* The assignment should be done in Kotlin or Java (version 21 or higher).
* The assignment must have a working main() method, to demonstrate how it works
* If you have any questions, feel free to write to <join-ecom@lightspeedhq.com>.
* The completed assignment should be posted on GitHub
