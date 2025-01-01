# **Project Documentation**
## 1. General Presentation
### **Project Title**
**Fort Boyard Riddle Game**
### **Contributors**

| Name | Role |
Pelathe Erwan developper
Baaoui Nassim developper
### **Description**
The **Fort Boyard Riddle Game** is a console-based interactive application inspired by the famous TV game show. Players are challenged with riddles, manage team selections, and solve puzzles to "win keys" and ultimately enter the treasure room. It's designed with simple Python logic and aims to recreate the excitement of the show's challenges.
### **Key Features**
- **Riddle Challenge**: Answer Père Fouras' riddles and earn keys.
- **Team Selection**: Choose your player for each challenge based on roles.
- **Adaptive Gameplay**: Players have a limited number of attempts and clues for puzzles.
- **Dynamic Data**: Riddles and challenges are loaded dynamically using JSON files.

### **Technologies Used**
- **Programming Language**: Python 3.3
- **Libraries**:
    - `json`: For managing riddles and clues data.
    - `random`: For random selection in challenges.
    - 'time': For sleep in different games

- **Tools**:
    - JetBrains PyCharm: Code editor and IDE.
    - Github: Co-working.
### **Installation**
#### **How to Clone the Repository**
1. Make sure Git is installed on your computer.
2. Clone the repository using the following command:
   git clone https://github.com/F1ja/fort_boyard_project
3. Navigate to the project folder:
     cd fort_boyard_project
4. Make sure you have the required data structure:
   - JSON files (e.g., `PFRiddles.json`, `TRClues.json`) should be in the `Data/` folder.
### **How to Use**
#### **Run the Application**
Run the main script in your terminal:
main.py
#### **Example Use Case**
Once you start the game:
1. Follow the instructions to select your player from the list.
2. Answer 'Père Fouras' riddles using the prompts provided, attempt to beat game masters at different minigames.
3. Collect keys and attempt to win!

## 2. Technical Documentation
### **Game Algorithm**
Here is the general algorithm for the game:
1. **Load Data**:
    - Load riddles and clues data from JSON files.
INcomplet
2. **Rules and Team Selection**:
    - Display the rules of the game.
    - Display the list of available players.
    - Team creation, based on player choices, up to 3.

3. **Challenge Loop**:
    - Display the game menu, allowing the user to select a type of challenge
    - Allow the user to select a player based on their role, the user will play as the chosen player.
    - Display the randomly chosen challenge (in the type of challenge selected)
    - The user attempts to win the challenge.
    - If yes, award a key.
    - If no, reduce the remaining attempts.

4. **Treasure Room**:
    - Once all three keys have been obtained:
    - Display collected keys/clues.
    - Allow the user to guess the final code-word based on clues.
5. **Recording Results**
    - Saving game history in history.txt file 

### **Functions**
Here are some of the main function prototypes:
1. **`load_riddles(file)`**
    - **Role**: Loads riddles from a JSON file.
    - **Parameters**:
        - `file`: Path to the JSON file.

    - **Returns**: A list of riddle dictionaries.

2. **`choose_player(team)`**
    - **Role**: Allows the user to select a player from a team.
    - **Parameters**:
        - `team`: List of players (as dictionaries).

    - **Returns**: The selected player dictionary.

3. **`pere_fouras_riddles()`**
    - **Role**: Implements Père Fouras' riddle gameplay.
    - **Parameters**: None.
    - **Returns**: `True` if the player wins, `False` otherwise.

4. **`treasure_room()`**
    - **Role**: Challenges the player to guess the treasure code-word.
    - **Parameters**: None.
    - **Returns**: None.
### **Input and Error Management**
- Input Values:
    - All user inputs are processed using basic validation (e.g., verifying numeric inputs for selecting players).
    - Case-insensitivity is handled for string inputs (like riddle answers).

- Error Management:
    - The `try-except` blocks handle edge cases, such as invalid inputs.
    - The code assumes the JSON file exists and contains properly formatted entries.

#### **Known Bugs**
- If the JSON file is missing or corrupted, the game crashes without error handling.
- The assumption of 3 riddles per game can cause index errors if fewer riddles are provided.

## 3. Logbook
Watch commits

### **Task Distribution**

| Team Member | Task |

| Pelathe Erwan | . |
| Baaoui Nassim | . |



**Missing**
4. Testing and Validation
o Test strategies :
§ Specific test cases and results.
§ Screenshots showing the tests in action.
