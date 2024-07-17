# Terrain Recognition System using Satellite Images

## Overview
This project is a Terrain Recognition System that accurately identifies various terrains—such as sandy, rocky, grassy, and marshy—from satellite images. Developed as a college mini project by a team of four members including myself, Jaswanth, Pradyumn, and Chandana, it includes an integrated chatbot feature hosted using Streamlit. This system enhances terrain-related activities by providing precise analysis and classification of environmental landscapes.

## Features
- Classifies terrains into four categories: Sandy, Rocky, Grassy, and Marshy.
- Includes a chatbot interface for user interaction.
- Uses a pre-trained model for terrain detection.

## Getting Started
### Prerequisites
- Python 3.x
- Required libraries: Flask, TensorFlow, Keras, Streamlit, dotenv, chainlit, numpy, keras.preprocessing, threading, langchain, HuggingFaceHub, PromptTemplate, LLMChain

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/shirtpanttie/MiniProject.git
    cd MiniProject
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
1. Ensure the pre-trained model (`model.keras`) is in the project directory.
2. Generate your Hugging Face API token:
    - Sign up or log in to [Hugging Face](https://huggingface.co/).
    - Navigate to your [account settings](https://huggingface.co/settings/tokens).
    - Create a new token and copy it.
3. Add the Hugging Face API token to the `.env` file:
    - Create a `.env` file in the project directory if it doesn't exist.
    - Add the following line to the `.env` file:
      ```bash
      HUGGINGFACE_API_TOKEN=Your_HugginfFace_token_here_without_quotes_
      ```
4. Run the Flask application:
    ```bash
    python app.py
    ```
5. Open your browser and navigate to `http://127.0.0.1:5000/`.
6. To start the Streamlit chatbot, run:
    ```bash
    chainlit run langchainlogic.py -w --port 8000
    ```


## Project Structure
- `app.py`: Main application file.
- `detect.py`: Contains terrain detection logic.
- `langchainlogic.py`: Implements a chatbot using the langchain library and integrates a Hugging Face model from a specified repository.
- `templates/`: HTML templates for the web interface.
- `static/`: The images that are given as input are usually saved here , can also include css files.
- `model.keras`: Pre-trained model for terrain recognition.
- `Terrainrecg done.ipynb`: Jupyter Notebook for model training and testing.
- `.env`: Used to store your Huggingface Hub API Token
- `chainlit.md `: You can include the chatbot startup message here

## Project Preview

![Home Page](screenshots/Home%20Page.png)  
*Figure 1: Home Page.*

![Terrain Recognition Input](screenshots/Terrain%20Recognition%20Input.png)  
*Figure 2: Interface for terrain recognition input.*

![Terrain Recognition Output](screenshots/Terrain%20Recognition%20Results.png)  
*Figure 3: Terrain Recognition results.*

![Chatbot Home Page](screenshots/ChatBot%20Home%20Page.png)  
*Figure 4: Chatbot Home Page.*

![Chatbot Reply](screenshots/ChatBot%20Reply.png)  
*Figure 5: Chatbot Reply to a query.*


