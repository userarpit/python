import pandas as pd
from datetime import datetime, timedelta
import random

def generate_round_robin_schedule(teams):
    """
    Generates a round-robin schedule for an even number of teams using the circle method.
    The order of matches within a round is consistent (e.g., Team 1's match first).
    """
    num_teams = len(teams)
    if num_teams % 2 != 0:
        teams.append("BYE") # Add a dummy team for odd number of teams
        num_teams += 1

    schedule = []
    # Create a mutable list for rotation.
    # Keep the first team conceptually fixed for pairing against rotating last team.
    
    fixed_team = teams[0]
    rotating_teams = list(teams[1:]) # Copy for mutable operations

    # For N teams, there are N-1 rounds
    for round_num in range(num_teams - 1):
        round_matches = []
        
        # Match the fixed team with the last rotating team
        round_matches.append((fixed_team, rotating_teams[-1]))

        # Pair the remaining teams (from top half with bottom half)
        for i in range(num_teams // 2 - 1):
            round_matches.append((rotating_teams[i], rotating_teams[len(rotating_teams) - 2 - i]))
        
        schedule.append(round_matches)

        # Rotate the 'rotating_teams' list for the next round
        # The last element moves to the beginning
        last_rotated = rotating_teams.pop()
        rotating_teams.insert(0, last_rotated)
    
    # Filter out "BYE" matches if a dummy team was added
    if "BYE" in teams:
        final_schedule = []
        for round_matches in schedule:
            filtered_round = []
            for team1, team2 in round_matches:
                if team1 != "BYE" and team2 != "BYE":
                    filtered_round.append((team1, team2))
            if filtered_round: # Only add if there are actual matches
                final_schedule.append(filtered_round)
        return final_schedule
    return schedule

def create_full_tournament_schedule(teams, start_datetime_str):
    """
    Generates the full tournament schedule with dates, times, and handles the
    "no team plays first match in consecutive week" and "shuffle order within week" constraints.
    """
    match_duration = timedelta(minutes=40)
    matches_per_week = 6
    num_rounds_base = len(teams) - 1 # 11 rounds for 12 teams
    total_weeks = num_rounds_base * 2 # 22 weeks total

    # Convert start_datetime_str to datetime object
    start_datetime = datetime.strptime(start_datetime_str, '%d %B %Y at %I:%M %p IST')

    # Generate the base round-robin pairings (these are fixed pairings for each round)
    full_round_robin_pairings = generate_round_robin_schedule(teams)
    
    detailed_schedule = []
    current_week_date = start_datetime
    
    # Track the team that played the very first match (6:00 PM slot) of the previous week
    previous_week_first_match_team = None

    # List to store the specific shuffled order of matches for each of the first 'num_rounds_base' weeks
    # This is needed to ensure the second half weeks have a DIFFERENT shuffle order
    original_shuffled_orders = []

    for week_idx in range(total_weeks):
        # Determine which base round pairings to use (cycles through 0 to num_rounds_base - 1)
        base_round_idx = week_idx % num_rounds_base
        
        # Get the matches for the current round from the base pairings
        matches_for_current_round = list(full_round_robin_pairings[base_round_idx])

        # --- Shuffling Logic ---
        current_week_shuffled_matches = list(matches_for_current_round) # Create a mutable copy

        if week_idx < num_rounds_base: # For the first half (weeks 1 to 11)
            random.shuffle(current_week_shuffled_matches)
            original_shuffled_orders.append(list(current_week_shuffled_matches)) # Store the exact shuffled order
        else: # For the second half (weeks 12 to 22)
            target_original_shuffled_order = original_shuffled_orders[base_round_idx]
            attempts = 0
            max_attempts = 100 # Safety break for shuffle
            
            # Keep shuffling until the order is different from the corresponding original week's order
            while attempts < max_attempts:
                random.shuffle(current_week_shuffled_matches)
                # Compare as lists of tuples (order matters for comparison)
                if current_week_shuffled_matches != target_original_shuffled_order:
                    break
                attempts += 1
            
            if attempts == max_attempts:
                print(f"Warning: Could not find a different shuffle for Week {week_idx + 1} (corresponding to Week {base_round_idx + 1}). Matched original order after {max_attempts} attempts. This is highly improbable.")
        
        # --- "No team plays first match in consecutive week" Constraint Logic ---
        # This logic applies to the *already shuffled* current_week_shuffled_matches
        if week_idx > 0:
            current_first_match_team_candidate = current_week_shuffled_matches[0][0]
            
            if current_first_match_team_candidate == previous_week_first_match_team:
                swapped = False
                # Try to find another match in this week's round whose first team is different
                for i in range(1, len(current_week_shuffled_matches)):
                    candidate_team_A = current_week_shuffled_matches[i][0]
                    if candidate_team_A != previous_week_first_match_team:
                        # Swap the default first match with this suitable candidate match
                        current_week_shuffled_matches[0], current_week_shuffled_matches[i] = \
                            current_week_shuffled_matches[i], current_week_shuffled_matches[0]
                        swapped = True
                        break
                if not swapped:
                    # Fallback: If no suitable swap found (unlikely for 12 teams, but good to handle)
                    print(f"Warning: Could not fully satisfy 'no consecutive first match' constraint for Week {week_idx + 1}.")
                    # The current_first_match_team_candidate will remain previous_week_first_match_team.

        # After potential reordering, record the team playing the first match of THIS week
        previous_week_first_match_team = current_week_shuffled_matches[0][0]

        # Schedule the 6 matches for the current week using the finalized order
        current_match_time = current_week_date
        for match_num, (team1, team2) in enumerate(current_week_shuffled_matches):
            detailed_schedule.append({
                'Week': week_idx + 1,
                'Match_Order_in_Week': match_num + 1, # 1 to 6
                'Date': current_week_date.strftime('%d-%m-%Y'),
                'Start Time': current_match_time.strftime('%I:%M %p IST'),
                'End Time': (current_match_time + match_duration).strftime('%I:%M %p IST'),
                'Team A': team1,
                'Team B': team2
            })
            current_match_time += match_duration
        
        # Move to the next week (add 7 days)
        current_week_date += timedelta(weeks=1)

    return pd.DataFrame(detailed_schedule)

# --- Team Names ---
teams = [
    "Ektarfa FC (TeamSkeet)",
    "BKFC",
    "Bon Bon FC (Supa)",
    "Cell Kraft FC (Riza)",
    "H&H Boyz",
    "Kanhaiya's Physio FC (Beast)",
    "Procure FC (Carnage)",
    "Propex FC (Galacticos)",
    "Reckon FC (FUTURE)",
    "Sapphire Seven",
    "Sarco FC (LUFC)",
    "Sarthak Singapore FC (Silverbacks)"
]

# Updated start_date_time_str to include the year
start_date_time_str = "29 June 2025 at 06:00 PM IST" # Format to match datetime.strptime

# Generate the schedule
schedule_df = create_full_tournament_schedule(teams, start_date_time_str)

# Display the schedule
print("Tournament Schedule:")
print(schedule_df)
schedule_df.to_csv('tournament_schedule.csv', index=False)

# --- Verification of "No team plays first match in consecutive week" constraint ---
print("\n--- Constraint Verification (First Match Team per Week) ---")
first_match_teams_per_week = schedule_df[schedule_df['Match_Order_in_Week'] == 1]['Team A'].tolist()
print(f"Teams playing the first match (6:00 PM slot) of each week: {first_match_teams_per_week}")

consecutive_violations = []
for i in range(1, len(first_match_teams_per_week)):
    if first_match_teams_per_week[i] == first_match_teams_per_week[i-1]:
        consecutive_violations.append(f"Week {i} and {i+1}: {first_match_teams_per_week[i]} plays first match consecutively.")

if not consecutive_violations:
    print("Constraint 'No team should play first match in consecutive week' is satisfied.")
else:
    print("Constraint Violations Found:")
    for violation in consecutive_violations:
        print(violation)

# --- Verification of "Different shuffle order for weeks 12-22 compared to 1-11" ---
print("\n--- Constraint Verification (Shuffle Order in Second Half) ---")
# Extract matches for first half
first_half_matches = [
    [tuple(row[['Team A', 'Team B']].values) for _, row in schedule_df[schedule_df['Week'] == week].iterrows()]
    for week in range(1, 12)
]
# Extract matches for second half
second_half_matches = [
    [tuple(row[['Team A', 'Team B']].values) for _, row in schedule_df[schedule_df['Week'] == week].iterrows()]
    for week in range(12, 23)
]

shuffle_violations = []
for i in range(len(first_half_matches)):
    # The pairings for first_half_matches[i] should be IDENTICAL to second_half_matches[i]
    # (after sorting to ignore internal shuffle for pairing comparison)
    # But the shuffle order must be different
    
    # Check if pairings are identical (ignoring order within the match tuple for robust comparison)
    sorted_first_half_pairings = sorted([tuple(sorted(match)) for match in first_half_matches[i]])
    sorted_second_half_pairings = sorted([tuple(sorted(match)) for match in second_half_matches[i]])
    
    if sorted_first_half_pairings != sorted_second_half_pairings:
        shuffle_violations.append(f"Week {i+1} and Week {i+1+11}: Pairings are NOT identical.")
    
    # Check if the shuffle order is different
    if first_half_matches[i] == second_half_matches[i]:
        shuffle_violations.append(f"Week {i+1} and Week {i+1+11}: Shuffle order IS identical.")

if not shuffle_violations:
    print("Constraint 'Shuffle order in weeks 12-22 does not match 1-11' is satisfied (and pairings are identical).")
else:
    print("Shuffle Order Constraint Violations Found:")
    for violation in shuffle_violations:
        print(violation)
