# Teddy Bear's Story Stages
class Stage:
    IDLE = "idle"                   # Resting, waiting for start
    ASKING_HELP = "asking_help"     # Seeking help (playing audio + expression)
    WAITING = "waiting"             # Waiting for help (10s countdown)
    THANKING = "thanking"           # Expressing gratitude
    DISAPPOINT = "disappoint"       # Expressing disappointment

# Action Commands for Teddy Bear 
class Action:
    NEUTRAL = "neutral"             # Show neutral face
    SAD = "sad"                     # Show sad face + play help-seeking audio
    HAPPY = "happy"                 # Show happy face + play thank-you audio
    DISAPPOINT = "disappoint"       # Show disappointed face + play disappointment audio

# story type Run
story_type = "sad"                  # Narrative type: 'sad' or 'restrained'
waiting_seconds = 10                # Duration to wait for help
