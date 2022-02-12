# Timetable-Solve-with-Genetic-Algorithm
The use of Genetic Algorithm in various work schedules.
This program takes the problem of scheduling tasks in the form of working at day and at night or 2 shifts.
If you are going to apply it to the problem You must know and understand the conditions of work and factors together.

What are the conditions? 
1.	Everyone must work no more than 5 days a week.
2.	Everyone cannot stop for more than 2 days in a row.
3.	1 working day 1 shift.
4.	Not working the night shift to the day shift.
5.	And do not have duplicate names in the same shift.

When you know the conditions, next you should know how to configure fitness.

Fitness: We use Fitness Error because direct Error values are low objecttive values instead of high fitness values. So it can be confusing. Therefore, choose to be the fitness value of the Error value instead.

How to Calculate Fitness values? It will be used to check points and deduct points. By giving weight as a criterion, when the condition is violated, points will be deducted according to the specified weight, etc.
