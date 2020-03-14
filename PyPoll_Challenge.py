# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources','election_results.csv')
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Initialize the candidate list
candidate_options = []

# Initialize the county list
county_options = []

# Declare the candidate votes dictionary
candidate_votes = {}

# Declare the county votes dictionary
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county turnout
winning_county_name = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Print the county name from each row
        county_name = row[1]
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county
        if county_name not in county_options:

            # Add the county name to the county list
            county_options.append(county_name)

            # Begin traacking that county's vote count
            county_votes[county_name] = 0

        # Add a vote to that county's count
        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal
    election_results = (

        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n'
        f'County Votes:\n')
    
    print(election_results, end='')

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the count
    # Iterate through the county list
    for county in county_votes:

        # Retrieve vote count of a county
        c_votes = county_votes[county]

        # Calculate the percentage of votes
        c_votes_percentage = float(c_votes) / float(total_votes) * 100

        # Print out each county's name, vote count and percentage of 
        # votes to the terminal
        county_results = (f'{county}: {c_votes_percentage:.1f}% ({c_votes:,})\n')

        print(county_results)

        # Save the county results to our text file
        txt_file.write(county_results)

        # Determine largest county turnout
        if (c_votes > winning_county_count) and (c_votes_percentage > winning_county_percentage):

            # If true then set winning_county_count = c_votes and 
            # winning_county_percentage = c_votes_percentage
            winning_county_count = c_votes
            winning_county_percentage = c_votes_percentage

            # And, set largest county turnout equal to county
            winning_county_name = county

     # Print out largest county turn out
    largest_county_turnout_summary = (
        f'-------------------------\n'
        f'Largest County Turnout: {winning_county_name}\n'
        f'-------------------------\n')

    print(largest_county_turnout_summary)

    # Save the largest county turnout to the text file
    txt_file.write(largest_county_turnout_summary)


    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
        
        print(candidate_results)
        
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percentage = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set winning_candidate equal to the candidate
            winning_candidate = candidate

    # To do: print out the winning candidate, vote count and percentage to terminal

    winning_candidate_summary = (
        f'---------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'---------------------------\n')

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)











