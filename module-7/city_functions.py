"""
city_functions.py
CSD-325 Module 7 Assignment
Student: Tara Rai
Date: 02/07/2026

Function to format city and country information with optional population and language parameters.
"""

def city_country(city, country, population=None, language=None):
    """
    Return a formatted string of the form 'City, Country' with optional
    population and language information.
    
    Args:
        city (str): Name of the city
        country (str): Name of the country
        population (int, optional): Population of the city. Defaults to None.
        language (str, optional): Primary language spoken. Defaults to None.
    
    Returns:
        str: Formatted location string in one of these formats:
            - "City, Country"
            - "City, Country - population xxx"
            - "City, Country - population xxx, Language"
    """
    # Start with basic city, country format with proper capitalization
    location = f"{city.title()}, {country.title()}"
    
    # Add population if provided (format with commas for thousands)
    if population is not None:
        location += f" - population {population:,}"
    
    # Add language if provided
    if language is not None:
        location += f", {language.title()}"
    
    return location


# Demonstration of function calls (executed when file runs directly)
if __name__ == "__main__":
    # Call 1: City and Country only
    print(city_country("santiago", "chile"))
    
    # Call 2: City, Country, and Population
    print(city_country("paris", "france", population=2161000))
    
    # Call 3: City, Country, Population, and Language
    print(city_country("tokyo", "japan", population=13960000, language="japanese"))