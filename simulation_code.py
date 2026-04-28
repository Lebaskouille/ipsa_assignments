# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:48:26 2026

@author: leomo
"""

# -*- coding: utf-8 -*-

from itertools import permutations

tasks = [
    {'name': 'τ1', 'C': 2.1, 'T': 10},
    {'name': 'τ2', 'C': 3,   'T': 10},
    {'name': 'τ3', 'C': 2,   'T': 20},
    {'name': 'τ4', 'C': 2,   'T': 20},
    {'name': 'τ5', 'C': 2,   'T': 40},
    {'name': 'τ6', 'C': 2,   'T': 40},
    {'name': 'τ7', 'C': 3,   'T': 80},
]

hyperperiod = 80



def generate_jobs():
    jobs = []
    for t in tasks:
        nb = hyperperiod // t['T'] # Number of repetition of the task over the hyperperiod
        for k in range(nb):
            # Duplication of the task to test the schedule
            jobs.append({'name': t['name'], 'C': t['C'], 'T': t['T'], 'start':  t['T'] * k, 'deadline': t['T'] * (k + 1)})
    return jobs




# This function simulate the proposed schedule (FP, EDF, SPF)
def simulation(critere):
    jobs = generate_jobs()
    time = 0
    total_waiting = 0

    while jobs:
        available = [j for j in jobs if j['start'] <= time] # We are listing every task that could be started at the actual time
        
        if not available: # If no tasks can start now
            time = min(j['start'] for j in jobs) # We are looking for the next time a task will want to start.
            continue

        chosen = min(available, key=critere) # We choose the task to do in priority (depends on the critere and/or the permutation)
        waiting = time - chosen['start'] # Waiting time for the task
        total_waiting += waiting # Compute for the choice of the best schedule
        time += chosen['C'] # Update of the time at the end of the task

        if time > chosen['deadline']: # If the task exceeds the deadline
            return None

        jobs.remove(chosen) # We delete it from the list of task to be processed

    return total_waiting




# Definition of the function used to simulate the chosen scheduling over the entire duration of the hyperperiod
# The code is essentially the same as the other one, it simply displays the tasks in order
# That's why I didn't comment this function
def simulation_for_display(priorites):
    priorite_map = {t['name']: i for i, t in enumerate(priorites)}
    jobs = generate_jobs()
    time = 0
    total_waiting = 0

    print(f"\n{'t':>6} | {'tâche':>4} | {'end':>6} | {'deadline':>8} | {'waiting':>7}")
    print("-" * 45)

    while jobs:
        available = [j for j in jobs if j['start'] <= time]

        if not available:
            start = time
            time = min(j['start'] for j in jobs)
            idle_duration = time - start
            print(f"{start:>6.2f} | {'IDLE':>4} | {time:>6.2f} | {'total time : ' + str(round(idle_duration, 2)):>16}")       
            continue

        chosen = min(available, key=lambda j, p=priorite_map: p[j['name']])

        waiting = time - chosen['start']
        total_waiting += waiting
        start = time
        time += chosen['C']

        print(f"{start:>6.2f} | {chosen['name']:>4} | {time:>6.2f} | {chosen['deadline']:>8} | {waiting:>7.2f}")

        jobs.remove(chosen)

    print(f"\nAttente totale : {total_waiting:.2f}")




# Earliest Deadline First (EDF) Methode
def EDF(job):
    return job['deadline']

# Smallest Period First (SPF) methode
def SPF(job):
    return job['T']





best_fp = None
best_waiting_fp = float('inf')
best_schedule_fp = None

for perm in permutations(tasks):
    # Retrieving the studied priority order via indices
    priorite_map = {t['name']: i for i, t in enumerate(perm)}
    critere = lambda j, p=priorite_map: p[j['name']]

    waiting = simulation(critere) # We simulate and retrieve the waiting time
    
    # If the schedule works and is better than the ones before, we keep it
    if waiting is not None and waiting < best_waiting_fp:
        best_waiting_fp = waiting
        best_fp = perm

# We are only printing the results
print("Best Fixed Priority :")
for t in best_fp:
    print(f"  {t['name']}  C={t['C']}  T={t['T']}")
print(f"Total waiting : {best_waiting_fp:.2f}")







# Now we test EDF and SPF methods
algos = {'EDF': EDF, 'SPF': SPF}
resultats = {}

for nom, critere in algos.items(): # For every methode
    print(f"\n{nom} :")
    waiting = simulation(critere) # We simulate with the critere of the methode
    
    # Only printing to see the results
    if waiting is not None:
        print("No missed deadline")
        print(f"Total waiting : {waiting:.2f}")
        print(f"   Not better than Fixed Priority ({best_waiting_fp:.2f})")
        resultats[nom] = (waiting, True)
    else:
        print("Not schedulable with this algorithm")
        resultats[nom] = (None, False)

    

# With the best scheduling found, each task is displayed in detail over time
simulation_for_display(best_fp)