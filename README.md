# Assignment
Using the StarWars API (https://swapi.tech/) create a simple full-stack web application to support the following end-user functionality:

- An authenticated user should be able to view a list of Starships in a `<table>`
- Using a `<select>`, an authenticated user should be able to choose a Starship `manufacturer` from a list
- When a Starship `manufacturer` is selected the `<table>` should display only the Starships for the selected `manufacturer`
- If no `manufacturer` is selected the `<table>` should display all Starships

# Notes and Technical Requirements:
- You are free to use any language and framework you’d like (.net code, node js, Micronaut, Flask, ruby on rails, etc).
- The solution should require Authentication.  We do not have any specific requirements for the approach and the solution does not need to account for inviting or signing up users, static user credentials are fine.
- The solution will not be evaluated on visual style, so you do not need to spend time styling unless you want to (browser defaults are fine).
- The solution does not need to be deployed anywhere, localhost is fine.
- If the solution uses an API it should respond with JSON data
- Client libraries exist for the StarWars API. We request that you do not use these libraries library to interact with the StarWars API
- Open-source packages other than the StarWars client libraries can be used but are not required to complete this assignment.

# Solution

The Star Wars API provided contains a soft rate-limit of 5 calls every 15 minutes, in order to develop a webapp using the Star Wars data it is necessary to first extract the information into a more usable format, this might be stored as a relational database or a csv.
After we extract the data using a static script, we can develop the webapp using flask since the frontend is not relevant to the challenge and localhost is acceptable.
The app contains a login with static credentials (user: user, password: 1234).