class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create a dictionary to store net population changes per year.
        diff = {}
        for birth, death in logs:
            # Increase population at birth year.
            diff[birth] = diff.get(birth, 0) + 1
            # Decrease population at death year.
            diff[death] = diff.get(death, 0) - 1

        # Variables to track current population, maximum population, and the earliest year with that max.
        current_population = 0
        max_population = 0
        result_year = 0

        # Process the years in sorted order.
        for year in sorted(diff.keys()):
            current_population += diff[year]
            # Update if we have a new maximum.
            if current_population > max_population:
                max_population = current_population
                result_year = year

        return result_year