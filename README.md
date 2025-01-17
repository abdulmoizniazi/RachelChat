# RachelChat  

RachelChat is an AI-powered chatbot application that integrates modern technologies to deliver voice and text-based conversational experiences.  

## Features  

- **Frontend**: Built with [Vite](https://vitejs.dev/) for a fast and efficient development experience.  
- **Backend**: Powered by [FastAPI](https://fastapi.tiangolo.com/) for robust and scalable backend support.  
- **Language Model**: Integrates OpenAI's large language model (LLM) for intelligent conversation generation.  
- **Voice-to-Text**: Utilizes OpenAI's Whisper model to seamlessly convert user voice inputs into text.  
- **Text-to-Voice**: Employs [ElevenLabs AI](https://elevenlabs.io/) for generating natural and expressive voice responses.  

## Project Structure  

```plaintext
RachelChat/
├── backend/  
│   ├── main.py            # FastAPI application entry point  
│   ├── functions/         # Utility functions  
│   │   ├── openai_requests.py  # Handles OpenAI API interactions  
│   │   ├── database.py         # Database-related functions  
│   │   ├── text_to_speech.py   # Eleven AI integration  
│   ├── stored_data.json    # Example data storage  
│   ├── .env                # Environment variables (not included in repo)  
├── frontend/  
│   ├── src/  
│   │   ├── App.tsx              # Main application component  
│   │   ├── components/          # React components (e.g., Title, RecordIcon)  
│   │   ├── index.css            # Styles  
│   │   ├── main.tsx             # React entry point  
│   ├── public/  
│   │   ├── vite.svg             # Vite logo  
│   ├── vite.config.ts           # Vite configuration file  
├── README.md             # Project documentation  
```

## Getting Started  

### Prerequisites  
- Node.js and npm/yarn  
- Python 3.9+  
- FastAPI and its dependencies  
- OpenAI API key and ElevenLabs API key  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/RachelChat.git  
   cd RachelChat  
   ```  

2. **Backend**:  
   - Navigate to the `backend` directory:  
     ```bash  
     cd backend  
     ```  
   - Create and activate a virtual environment:  
     ```bash  
     python -m venv .venv  
     source .venv/bin/activate  # For Linux/macOS  
     .venv\Scripts\activate     # For Windows  
     ```  
   - Install dependencies:  
     ```bash  
     pip install -r requirements.txt  
     ```  
   - Set up the `.env` file with your API keys:  
     ```plaintext  
     OPENAI_API_KEY=your_openai_api_key  
     ELEVENAI_API_KEY=your_elevenlabs_api_key  
     ```  
   - Start the FastAPI server:  
     ```bash  
     uvicorn main:app --reload  
     ```  

3. **Frontend**:  
   - Navigate to the `frontend` directory:  
     ```bash  
     cd frontend  
     ```  
   - Install dependencies:  
     ```bash  
     npm install  
     ```  
   - Start the development server:  
     ```bash  
     npm run dev  
     ```  

### Usage  

1. Access the application in your browser at `http://localhost:3000`.  
2. Use voice input to interact with the chatbot or type directly into the interface.  
3. Enjoy the seamless text and voice-based interactions powered by AI.  

## Technologies Used  

- **Frontend**: React, Vite, Tailwind CSS  
- **Backend**: FastAPI  
- **AI Models**: OpenAI GPT, OpenAI Whisper, ElevenLabs AI  

## Contributing  

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.  

## License  

This project is licensed under the [MIT License](LICENSE).  
