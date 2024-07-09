# SpareRoomTask
Task provided by SpareRoom as part of their hiring process:

## The Task
You are implementing a simple checkout system, there are four products available, each with a price per unit. Some products have a special price when bought in certain quantities (e.g. 3 of product A costs 140, not 150). Implement a checkout system that consumes a data source like this "[{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}]", and returns the sub total when queried.

Make sure your solution includes everything that it would in a production environment, i.e. verifying results / testing, documentation.

Please provide your solution in a git repo. e.g. github, bitbucket, etc.

### Pricing Dataset

ItemCode A: UnitPrice = 50; SpecialPrice = 3 for 140
ItemCode B: UnitPrice = 35; SpecialPrice = 2 for 60
ItemCode C: UnitPrice = 25; SpecialPrice = N/A
ItemCode D: UnitPrice = 12; SpecialPrice = N/A

## Implementation
The solution is implemented in Python and includes the following:
- Validation checks for item codes and quantities.
- Function to validate and reformat product codes.
- Calculation of subtotal based on pricing dataset.
- Unit tests using the 'unittest' framework.
