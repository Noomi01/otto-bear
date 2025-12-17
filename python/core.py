import config 

# Hardware  Functions 
def experiment_started():
    # Return True when the experiment is remotely started
    return False  

def help_detected():
    # Return True when camera confirms a complete 'putting chestnut' action
    return False  

def audio_finished():
    # Return True when the currently playing audio clip ends
    return False  

def waiting_timeout():
    #Return True when the waiting timer reaches waiting_seconds(10s)
    return False  

# Teddy Bear's Runtime Memory
current_stage = config.Stage.IDLE  # Current story stage
next_action = config.Action.NEUTRAL  # Next action to execute

# Core State Machine
def update_story():
    # Update bear's state and actions based on contract signals
    global current_stage, next_action

    # 1. Idle-Wait for start signal
    if current_stage == config.Stage.IDLE:
        if experiment_started():
            current_stage = config.Stage.ASKING_HELP
            # send SAD action command (sad expression)
            next_action = config.Action.SAD
            print(f"Experiment started! Narrative style: '{config.story_type}', Action: {next_action}")
            # play the corresponding help audio based on config.story_type

    # 2. Asking Help- Wait for help audio to finish playing
    elif current_stage == config.Stage.ASKING_HELP:
        if audio_finished():
            current_stage = config.Stage.WAITING
            print(f"Entering {config.waiting_seconds} second waiting period, maintaining expression")

    # 3. Waiting-Detect help or timeout
    elif current_stage == config.Stage.WAITING:
        if help_detected():  # Help received
            current_stage = config.Stage.THANKING
            next_action = config.Action.HAPPY
            print(f"Help detected! Executing action: {next_action}")
        elif waiting_timeout():  # Timeout, no help
            current_stage = config.Stage.DISAPPOINT
            next_action = config.Action.DISAPPOINT
            print(f"Waiting timeout. Executing action: {next_action}")

    # 4. Thanking- Reset after thank-you audio finishes
    elif current_stage == config.Stage.THANKING:
        if audio_finished():
            current_stage = config.Stage.IDLE
            next_action = config.Action.NEUTRAL
            print("Thank-you complete, story reset, waiting for next start.")

    # 5. Disappointed-Reset after disappointment audio finishes
    elif current_stage == config.Stage.DISAPPOINT:
        if audio_finished():
            current_stage = config.Stage.IDLE
            next_action = config.Action.NEUTRAL
            print("Disappointment complete, story reset, waiting for next start.")